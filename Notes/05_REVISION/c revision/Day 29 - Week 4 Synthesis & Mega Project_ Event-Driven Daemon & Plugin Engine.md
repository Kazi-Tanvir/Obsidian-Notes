---
tags:
  - c
  - week-4-synthesis
  - mega-project
  - systems-programming
  - posix-daemon
  - unix-domain-sockets
  - non-blocking-io
  - dynamic-plugins
date: 2026-09-20
day: 29
---

# Day 29: Week 4 Synthesis & Mega Project: Event-Driven Daemon & Plugin Engine

---

## 1. Quick Reference & Cheat Sheet (Week 4 Synthesis)

### Week 4 Core Systems Foundations

- **Multi-File Build Systems & Header Hygiene:**

  - Headers contain only declarations (extern int g_val;), types, and static inline functions. Never define non-static variables in .h files!

  - Automated dependencies: CFLAGS += -MMD -MP emits .d files tracking transitive header modifications.

- **Libraries & Dynamic Loading:**

  - Static archives: ar rcs libname.a foo.o bar.o. Link order matters (left-to-right resolution).

  - Shared objects: gcc -shared -fPIC -o libname.so foo.o bar.o. Relies on the Global Offset Table (GOT) & Procedure Linkage Table (PLT).

  - Dynamic symbol loading: dlopen(path, RTLD_NOW | RTLD_LOCAL), dlsym(), dlerror(), and dlclose().

- **Error Handling & Non-Local Jumps:**

  - errno is a thread-local modifiable lvalue ((*__errno_location())). Always save int saved_errno = errno; before invoking cleanup routines.

  - setjmp/longjmp: All automatic local variables modified after setjmp must be qualified as volatile to prevent register rollback bugs.

  - Kernel RAII idiom: Ordered single-exit goto cleanup;.

- **Defensive Programming & Undefined Behavior (UB):**

  - Compilers optimize under the assumption that UB never occurs; check conditions before executing operations (e.g. b > INT_MAX - a instead of a + b < a).

  - Always test with -fsanitize=address,undefined,leak -fno-omit-frame-pointer.

- **Debugging Tools (GDB & Valgrind):**

  - GDB replaces target instructions with 0xCC (INT 3) via ptrace(2). Hardware watchpoints use DR0--DR7.

  - Valgrind Memcheck tracks A-bits (Addressability) and V-bits (Validity). Differentiates *Definitely*, *Indirectly*, *Possibly*, and *Still Reachable* leaks.

- **Low-Level POSIX System Calls & I/O:**

  - Process lifecycle: fork(), execve(), waitpid(). Use _exit() in children if exec fails to prevent parent buffer double-flushes.

  - Descriptors: Kernel Open File Table stores byte offsets and reference counts; dup2(oldfd, newfd) redirects streams.

## 2. In-Depth Theory & Low-Level Mechanics

### A. The POSIX Daemonization Protocol

A true UNIX daemon must be completely divorced from the terminal, session, and controlling process group that spawned it.

Interactive Terminal Shell (Session 100, PGID 100, TTY: /dev/pts/0)

1.  **fork()**: Parent exits immediately. (Returns control to user shell; child is guaranteed NOT to be a process group leader).

2.  **setsid()**: Creates a brand new Session and Process Group (Leader of Session 200). Detaches permanently from controlling terminal (/dev/pts/0).

3.  **fork()**: Second fork! Parent (Session Leader) terminates. (Child is NOT session leader; can NEVER reacquire a TTY even if opening device files!).

4.  **chdir("/")**: Unlinks current working directory so filesystems can unmount safely.

5.  **umask(0)**: Resets file creation mode mask for explicit permission control.

6.  **Stream Redirection**: Close FDs 0, 1, 2 and redirect to /dev/null or syslog.

### B. Event-Driven Non-Blocking I/O Multiplexing (poll / epoll)

Thread-per-connection server architectures do not scale to thousands of concurrent connections due to OS thread context switching and stack allocation overhead (8MB per thread).

The event-driven model operates on a single thread using non-blocking file descriptors:

1.  **Setting Non-Blocking Mode:**int flags = fcntl(fd, F_GETFL, 0);

> fcntl(fd, F_SETFL, flags | O_NONBLOCK);

2.  **The poll(2) Event Loop:** An array of struct pollfd monitors multiple file descriptors concurrently:struct pollfd fds[MAX_CLIENTS];

> fds[i].fd = client_fd; > > fds[i].events = POLLIN; // Monitor read availability > > int ready = poll(fds, num_fds, -1); // Block until an event occurs

3.  **Handling Non-Blocking Semantics:** When reading from a non-blocking socket:

    - If bytes are available, read() returns the byte count.

    - If no data is available, read() returns -1 with errno == EAGAIN or EWOULDBLOCK. This is **not an error**! The server continues processing other clients.

    - If client disconnected, read() returns 0 (EOF).

### C. Dynamic Plugin Hot-Reloading Architecture

In high-availability daemons, taking down the entire service to upgrade a business logic module or query handler is unacceptable.

Because file descriptors remain open in the event loop, active TCP or Unix Domain Socket client connections experience zero interruption during the library swap. The daemon catches the SIGHUP signal, flips a reload flag, and performs a dlclose/dlopen cycle to swap the shared object logic.

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Non-Blocking Unix Domain Socket Echo Server (unix_echo_server)

#### Objective

Build a fast, multiplexed Unix Domain Socket server that accepts local connections, buffers input, and echoes data back to multiple concurrent clients using poll(2) and non-blocking I/O.

#### Complete Implementation (unix_echo.c)

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdint.h>
#include "plugin_abi.h"
static int transform_init(void) { return 0; }
static void transform_process(const char *input, char *output, size_t max_out) {
    size_t len = strlen(input);
    if (len >= max_out) len = max_out - 1;
    for (size_t i = 0; i < len; i++) {
        output[i] = (char)toupper((unsigned char)input[len - 1 - i]);
    }
    output[len] = '\0';
}
static void transform_shutdown(void) {}
``` __attribute__((visibility("default"))) const DaemonPlugin active_plugin = { .magic = PLUGIN_MAGIC, .name = "Reverse-Uppercase Transformer", .version = "1.0.0", .init = transform_init, .process_request = transform_process, .shutdown = transform_shutdown }; ### File 3: The Complete Daemon Implementation (microdaemon.c) The daemon manages the event loop, handles signals, and hot-reloads plugins using dlopen. It uses a poll loop to monitor the server socket and up to MAX_CLIENTS connections, dispatching data to the loaded plugin. ### Build & Execution Instructions # 1. Compile Plugin as Position Independent Shared Library gcc -std=c17 -Wall -Wextra -fPIC -shared plugin_transform.c -o libplugin_transform.so # 2. Compile Daemon with Dynamic Linker gcc -std=c17 -Wall -Wextra -D_GNU_SOURCE microdaemon.c -ldl -o microdaemon # 3. In Terminal 1: Launch Daemon ./microdaemon # 4. In Terminal 2: Connect using netcat nc -U /tmp/microdaemon.sock hello world systems # Response: SMETSYS DLROW OLLEH
