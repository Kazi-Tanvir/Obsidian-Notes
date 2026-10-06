**Meta-information**\
**Tags:** c, week-4-synthesis, mega-project, systems-programming,
posix-daemon, unix-domain-sockets, non-blocking-io, dynamic-plugins\
Date: 2026-09-20\
Day: 29

Day 29: Week 4 Review & Weekly Mega Project --- High-Performance
Event-Driven Microservice Daemon with Unix Domain Sockets & Dynamic
Shared Plugins

# 1. Quick Reference & Cheat Sheet (Week 4 Synthesis)

## Week 4 Core Systems Foundations

- **Multi-File Build Systems & Header Hygiene:**

  - Headers contain only declarations (extern int g_val;), types, and
    static inline functions. Never define non-static variables in .h
    files!

  - Automated dependencies: CFLAGS += -MMD -MP emits .d files tracking
    transitive header modifications.

- **Libraries & Dynamic Loading:**

  - Static archives: ar rcs libname.a foo.o bar.o. Link order matters
    (left-to-right resolution).

  - Shared objects: gcc -shared -fPIC -o libname.so foo.o bar.o. Relies
    on the Global Offset Table (GOT) & Procedure Linkage Table (PLT).

  - Dynamic symbol loading: dlopen(path, RTLD_NOW \| RTLD_LOCAL),
    dlsym(), dlerror(), and dlclose().

- **Error Handling & Non-Local Jumps:**

  - errno is a thread-local modifiable lvalue
    ((\*\_\_errno_location())). Always save int saved_errno = errno;
    before invoking cleanup routines.

  - setjmp/longjmp: All automatic local variables modified after setjmp
    must be qualified as volatile to prevent register rollback bugs.

  - Kernel RAII idiom: Ordered single-exit goto cleanup;.

- **Defensive Programming & Undefined Behavior (UB):**

  - Compilers optimize under the assumption that UB never occurs; check
    conditions before executing operations (e.g. b \> INT_MAX - a
    instead of a + b \< a).

  - Always test with -fsanitize=address,undefined,leak
    -fno-omit-frame-pointer.

- **Debugging Tools (GDB & Valgrind):**

  - GDB replaces target instructions with 0xCC (INT 3) via ptrace(2).
    Hardware watchpoints use DR0--DR7.

  - Valgrind Memcheck tracks A-bits (Addressability) and V-bits
    (Validity). Differentiates *Definitely*, *Indirectly*, *Possibly*,
    and *Still Reachable* leaks.

- **Low-Level POSIX System Calls & I/O:**

  - Process lifecycle: fork(), execve(), waitpid(). Use \_exit() in
    children if exec fails to prevent parent buffer double-flushes.

  - Descriptors: Kernel Open File Table stores byte offsets and
    reference counts; dup2(oldfd, newfd) redirects streams.

# 2. In-Depth Theory & Low-Level Mechanics

## A. The POSIX Daemonization Protocol

A true UNIX daemon must be completely divorced from the terminal,
session, and controlling process group that spawned it.

Interactive Terminal Shell (Session 100, PGID 100, TTY: /dev/pts/0)

1.  **fork()**: Parent exits immediately. (Returns control to user
    shell; child is guaranteed NOT to be a process group leader).

2.  **setsid()**: Creates a brand new Session and Process Group (Leader
    of Session 200). Detaches permanently from controlling terminal
    (/dev/pts/0).

3.  **fork()**: Second fork! Parent (Session Leader) terminates. (Child
    is NOT session leader; can NEVER reacquire a TTY even if opening
    device files!).

4.  **chdir(\"/\")**: Unlinks current working directory so filesystems
    can unmount safely.

5.  **umask(0)**: Resets file creation mode mask for explicit permission
    control.

6.  **Stream Redirection**: Close FDs 0, 1, 2 and redirect to /dev/null
    or syslog.

## B. Event-Driven Non-Blocking I/O Multiplexing (poll / epoll)

Thread-per-connection server architectures do not scale to thousands of
concurrent connections due to OS thread context switching and stack
allocation overhead (8MB per thread).

The event-driven model operates on a single thread using non-blocking
file descriptors:

1.  **Setting Non-Blocking Mode:**int flags = fcntl(fd, F_GETFL, 0);

> fcntl(fd, F_SETFL, flags \| O_NONBLOCK);

2.  **The poll(2) Event Loop:**\
    An array of struct pollfd monitors multiple file descriptors
    concurrently:struct pollfd fds\[MAX_CLIENTS\];

> fds\[i\].fd = client_fd;
>
> fds\[i\].events = POLLIN; // Monitor read availability
>
> int ready = poll(fds, num_fds, -1); // Block until an event occurs

3.  **Handling Non-Blocking Semantics:**\
    When reading from a non-blocking socket:

    - If bytes are available, read() returns the byte count.

    - If no data is available, read() returns -1 with errno == EAGAIN or
      EWOULDBLOCK. This is **not an error**! The server continues
      processing other clients.

    - If client disconnected, read() returns 0 (EOF).

## C. Dynamic Plugin Hot-Reloading Architecture

In high-availability daemons, taking down the entire service to upgrade
a business logic module or query handler is unacceptable.

Because file descriptors remain open in the event loop, active TCP or
Unix Domain Socket client connections experience zero interruption
during the library swap. The daemon catches the SIGHUP signal, flips a
reload flag, and performs a dlclose/dlopen cycle to swap the shared
object logic.

# 3. Thoughtful Mini-Project (\~1 Hour Scope)

## Project Title: Non-Blocking Unix Domain Socket Echo Server (unix_echo_server)

### Objective

Build a fast, multiplexed Unix Domain Socket server that accepts local
connections, buffers input, and echoes data back to multiple concurrent
clients using poll(2) and non-blocking I/O.

### Complete Implementation (unix_echo.c)

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<stdint.h\>

#include \<stdbool.h\>

#include \<string.h\>

#include \<unistd.h\>

#include \<fcntl.h\>

#include \<poll.h\>

#include \<errno.h\>

#include \<sys/socket.h\>

#include \<sys/un.h\>

#include \<assert.h\>

#define SOCKET_PATH \"/tmp/unix_echo.sock\"

#define MAX_FDS 16

#define BUFFER_SIZE 256

static int set_nonblocking(int fd) {

int flags = fcntl(fd, F_GETFL, 0);

if (flags == -1) return -1;

return fcntl(fd, F_SETFL, flags \| O_NONBLOCK);

}

int main(void) {

printf(\"=== Starting Non-Blocking Unix Domain Socket Server ===\\n\");

unlink(SOCKET_PATH); // Ensure stale socket file is removed

int server_fd = socket(AF_UNIX, SOCK_STREAM, 0);

assert(server_fd != -1);

assert(set_nonblocking(server_fd) == 0);

struct sockaddr_un addr;

memset(&addr, 0, sizeof(addr));

addr.sun_family = AF_UNIX;

strncpy(addr.sun_path, SOCKET_PATH, sizeof(addr.sun_path) - 1);

assert(bind(server_fd, (struct sockaddr \*)&addr, sizeof(addr)) == 0);

assert(listen(server_fd, 8) == 0);

printf(\"\[+\] Server listening on %s (FD: %d)\\n\", SOCKET_PATH,
server_fd);

struct pollfd fds\[MAX_FDS\];

for (int i = 0; i \< MAX_FDS; i++) fds\[i\].fd = -1;

fds\[0\].fd = server_fd;

fds\[0\].events = POLLIN;

int nfds = 1;

int iterations = 0;

while (++iterations \< 20) { // Run bounded loop for testing
demonstration

int ret = poll(fds, nfds, 100); // 100ms timeout

if (ret == -1) {

if (errno == EINTR) continue;

perror(\"poll failed\");

break;

}

// 1. Check for incoming connections on listening socket

if (fds\[0\].revents & POLLIN) {

while (true) {

int client_fd = accept(server_fd, NULL, NULL);

if (client_fd == -1) {

if (errno == EAGAIN \|\| errno == EWOULDBLOCK) break; // All drained

\|\-\--\|perror(\"accept failed\");

break;

}

set_nonblocking(client_fd);

// Add to poll set

int idx = -1;

for (int i = 1; i \< MAX_FDS; i++) {

if (fds\[i\].fd == -1) { idx = i; break; }

}

if (idx != -1) {

fds\[idx\].fd = client_fd;

fds\[idx\].events = POLLIN;

if (idx \>= nfds) nfds = idx + 1;

printf(\"\[+\] Accepted client (FD: %d) at slot %d\\n\", client_fd,
idx);

} else {

printf(\"\[-\] Server full, rejecting client FD: %d\\n\", client_fd);

close(client_fd);

}

}

}

// 2. Check for client data

for (int i = 1; i \< nfds; i++) {

if (fds\[i\].fd != -1 && (fds\[i\].revents & POLLIN)) {

char buf\[BUFFER_SIZE\];

ssize_t n = read(fds\[i\].fd, buf, sizeof(buf) - 1);

if (n \> 0) {

buf\[n\] = \'\\0\';

printf(\" \[FD %d Echo\] Received: %s\", fds\[i\].fd, buf);

write(fds\[i\].fd, buf, (size_t)n); // Echo back

} else if (n == 0 \|\| (n == -1 && errno != EAGAIN && errno !=
EWOULDBLOCK)) {

printf(\"\[-\] Client disconnected (FD: %d)\\n\", fds\[i\].fd);

close(fds\[i\].fd);

fds\[i\].fd = -1;

}

}

}

}

// Cleanup

for (int i = 0; i \< nfds; i++) {

if (fds\[i\].fd != -1) close(fds\[i\].fd);

}

unlink(SOCKET_PATH);

printf(\"\[+\] Server shutdown cleanly.\\n\");

return 0;

}

# 4. Error Handling & Defensive Programming Challenge

## Scenario: The Signal Handler Reentrancy Trap & Broken Pipe Termination

Examine this buggy daemon server code:#include \<stdio.h\>

#include \<stdlib.h\>

#include \<signal.h\>

#include \<unistd.h\>

#include \<syslog.h\>

int g_server_fd = -1;

FILE \*g_log_fp = NULL;

// FATAL BUG: Unsafe Async-Signal Handler!

void handle_sigterm(int sig) {

// BUG 1: syslog(), fprintf(), and free() are NOT async-signal-safe!

syslog(LOG_INFO, \"Daemon caught signal %d, exiting\...\", sig);

fprintf(g_log_fp, \"Caught signal %d\\n\", sig);

// BUG 2: Non-atomic cleanup

if (g_server_fd != -1) {

close(g_server_fd);

}

exit(0);

}

void send_response(int client_fd, const char \*msg, size_t len) {

// BUG 3: If client disconnected, write() raises SIGPIPE and kills the
daemon instantly!

write(client_fd, msg, len);

}

## Analysis of Vulnerabilities:

1.  **Async-Signal-Unsafe Functions:** Signal handlers interrupt
    execution asynchronously. If the main thread holds a lock for
    buffered I/O or malloc and the handler calls them again, the process
    **deadlocks**.

2.  **SIGPIPE Crash:** Writing to a closed socket triggers SIGPIPE,
    which terminates the process by default.

## Defensive Fix:

#include \<stdio.h\>

#include \<stdlib.h\>

#include \<signal.h\>

#include \<unistd.h\>

#include \<errno.h\>

#include \<sys/socket.h\>

static volatile sig_atomic_t g_shutdown_requested = 0;

void safe_signal_handler(int sig) {

(void)sig;

int saved_errno = errno;

g_shutdown_requested = 1;

errno = saved_errno;

}

void init_safe_signals(void) {

struct sigaction sa_pipe;

sa_pipe.sa_handler = SIG_IGN; // Fix 2: Ignore SIGPIPE

sigemptyset(&sa_pipe.sa_mask);

sa_pipe.sa_flags = 0;

sigaction(SIGPIPE, &sa_pipe, NULL);

struct sigaction sa_term;

sa_term.sa_handler = safe_signal_handler;

sigemptyset(&sa_term.sa_mask);

sa_term.sa_flags = SA_RESTART;

sigaction(SIGTERM, &sa_term, NULL);

}

# 5. WEEKLY MEGA PROJECT (Week 4 Capstone)

## Project Title: High-Performance Multi-Client Event-Driven Microservice Daemon with Unix Domain Sockets & Dynamic Shared Plugins (c_microdaemon)

### Architectural Overview

This enterprise-grade capstone synthesizes all topics covered throughout
Week 4:

1.  **POSIX Daemonization & Process Isolation:** Detaches cleanly from
    the controlling terminal via the double-fork protocol.

2.  **Event-Driven Non-Blocking Multiplexing:** Utilizes POSIX poll(2)
    on a non-blocking Unix Domain Socket.

3.  **Dynamic Plugin Architecture:** Business logic is decoupled into
    external shared objects (.so) with runtime hot-reloading capability.

4.  **Resilient Signal Handling:** Ignores SIGPIPE and uses sig_atomic_t
    for graceful shutdown.

### File 1: The Plugin ABI (plugin_abi.h)

#ifndef PLUGIN_ABI_H

#define PLUGIN_ABI_H

#define PLUGIN_MAGIC 0x4D444145

typedef struct {

uint32_t magic;

const char \*name;

const char \*version;

int (\*init)(void);

void (\*process_request)(const char \*input, char \*output, size_t
max_out);

void (\*shutdown)(void);

} DaemonPlugin;

#endif

### File 2: Sample Dynamic Plugin (plugin_transform.c)

#include \<stdio.h\>

#include \<string.h\>

#include \<ctype.h\>

#include \<stdint.h\>

#include \"plugin_abi.h\"

static int transform_init(void) { return 0; }

static void transform_process(const char \*input, char \*output, size_t
max_out) {

size_t len = strlen(input);

if (len \>= max_out) len = max_out - 1;

for (size_t i = 0; i \< len; i++) {

output\[i\] = (char)toupper((unsigned char)input\[len - 1 - i\]);

}

output\[len\] = \'\\0\';

}

static void transform_shutdown(void) {}

\_\_attribute\_\_((visibility(\"default\")))

const DaemonPlugin active_plugin = {

.magic = PLUGIN_MAGIC,

.name = \"Reverse-Uppercase Transformer\",

.version = \"1.0.0\",

.init = transform_init,

.process_request = transform_process,

.shutdown = transform_shutdown

};

### File 3: The Complete Daemon Implementation (microdaemon.c)

The daemon manages the event loop, handles signals, and hot-reloads
plugins using dlopen. It uses a poll loop to monitor the server socket
and up to MAX_CLIENTS connections, dispatching data to the loaded
plugin.

### Build & Execution Instructions

\# 1. Compile Plugin as Position Independent Shared Library

gcc -std=c17 -Wall -Wextra -fPIC -shared plugin_transform.c -o
libplugin_transform.so

\# 2. Compile Daemon with Dynamic Linker

gcc -std=c17 -Wall -Wextra -D_GNU_SOURCE microdaemon.c -ldl -o
microdaemon

\# 3. In Terminal 1: Launch Daemon

./microdaemon

\# 4. In Terminal 2: Connect using netcat

nc -U /tmp/microdaemon.sock

hello world systems

\# Response: SMETSYS DLROW OLLEH
