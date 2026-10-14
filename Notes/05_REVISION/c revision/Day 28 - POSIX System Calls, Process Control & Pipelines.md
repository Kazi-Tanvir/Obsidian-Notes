---
tags:
  - c
  - posix
  - system-calls
  - file-descriptors
  - fork-exec
  - pipe-ipc
  - dup2
date: 2026-09-19
day: 28
---

# Day 28: POSIX System Calls, Process Control & Pipelines

---

## 1. Quick Reference & Cheat Sheet

### Standard File Descriptors

| Integer FD | Macro Constant | Standard POSIX Stream | C Runtime Stream | Default Target |
| :--- | :--- | :--- | :--- | :--- |
| `0` | `STDIN_FILENO` | Standard Input | `stdin` | Keyboard / Terminal (`/dev/tty`) |
| `1` | `STDOUT_FILENO`| Standard Output | `stdout`| Terminal Display (`/dev/tty`) |
| `2` | `STDERR_FILENO`| Standard Error | `stderr`| Terminal Display (Unbuffered) |

### Low-Level File I/O (`<unistd.h>`, `<fcntl.h>`)

- `open()`: Returns a non-negative integer file descriptor, or `-1` on error with `errno` set.
```c
int fd = open("log.bin", O_WRONLY | O_CREAT | O_TRUNC, 0644);
```
- `read()` / `write()`: Low-level unbuffered system calls. Transfer raw byte buffers directly to/from kernel space.
- `close()`: Releases the file descriptor and decrements kernel open file reference count.

### Process Control & Lifecycle API (`<sys/wait.h>`, `<unistd.h>`)

- **`fork()`:** Clones the calling process.
```c
pid_t pid = fork();
if (pid < 0) {
    perror("fork failed");
} else if (pid == 0) {
    // Child Process: pid is 0
} else {
    // Parent Process: pid is Child's PID
}
```
- **`execvp()`:** Overwrites current process image with a new executable.
```c
char *args[] = { "grep", "root", "/etc/passwd", NULL };
execvp(args[0], args);
// Returns ONLY on failure!
perror("execvp failed");
_exit(1);
```
- **`waitpid()`:** Suspends calling process until child state changes.
```c
int status;
waitpid(pid, &status, 0);
if (WIFEXITED(status)) {
    int exit_code = WEXITSTATUS(status);
}
```

### Pipe IPC (`pipe`, `dup2`)

- `pipe(int pipefd[2])`: Creates a unidirectional data channel in kernel memory.
  - `pipefd[0]`: Read End.
  - `pipefd[1]`: Write End.
- `dup2(oldfd, newfd)`: Atomically duplicates `oldfd` onto `newfd`. If `newfd` was open, closes it first without a race condition.

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. The Three-Tier Kernel File Table Architecture

In Linux/POSIX operating systems, a file descriptor is merely an index into a per-process table:

1. **Per-Process File Descriptor Table:** An array indexed by the integer FD. Each entry holds flags (e.g. `FD_CLOEXEC`) and a pointer to an Open File Description in kernel space.
2. **System-Wide Open File Table:** Resides in kernel space. Stores the current byte offset, status flags (`O_RDONLY`, `O_NONBLOCK`), and a reference counter.
3. **V-Node / Inode Table:** Resides in kernel space. Represents the actual underlying physical file on the storage device (filesystem metadata, permissions, lock lists).

```text
Process A (FD Table)             Kernel Open File Table                 Filesystem Inode Table
┌──────────────────┐             ┌────────────────────────┐             ┌─────────────────────┐
│ FD 0 (stdin)     ├────────────►│ Offset=0, O_RDONLY     ├────────────►│ Inode 1042 (/dev/tty│
│ FD 1 (stdout)    ├───┐         └────────────────────────┘             └─────────────────────┘
│ FD 2 (stderr)    │   │         ┌────────────────────────┐             ┌─────────────────────┐
└──────────────────┘   └────────►│ Offset=4096, O_WRONLY  ├────────────►│ Inode 8923 (log.txt)│
                                 └────────────────────────┘             └─────────────────────┘
```

### B. Process Duplication (`fork`) & Copy-On-Write (COW) Mechanics

When `fork()` executes, the OS kernel does *not* physically duplicate the parent's memory pages:
- It creates a duplicate Page Table for the child pointing to the *exact same physical memory frames*.
- All writable memory pages are marked as **Read-Only** in both parent and child MMU page tables.
- **Copy-On-Write (COW):** If either process attempts to write to a page, a hardware page fault triggers. The kernel transparently allocates a new physical frame, copies the 4KB data, marks the page writable, and resumes execution.

### C. The Two Fatal Pipeline Bugs:

1. **The Hanging Reader (Deadlock):** A `read()` on a pipe will only return `0` (EOF) once **all write descriptors pointing to that pipe across all processes are closed**. If the parent fails to close its own write end (`close(pipefd[1])`), the child reading from the pipe blocks forever waiting for EOF.
2. **The Broken Pipe (`SIGPIPE`):** If a process calls `write()` on a pipe when no processes have the read end open, the kernel raises `SIGPIPE`. By default, this kills the process immediately.

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Mini UNIX Shell Pipeline Engine (`posix_pipeline`)

#### Objective

Build a robust, programmatic pipeline executor in C that executes arbitrary multi-stage pipelines (e.g. `ls -l | grep .c | wc -l`), wiring stdout to stdin using `pipe()` and `dup2()`, with deterministic cleanup and exit status collection.

#### Complete Implementation (`pipeline_engine.c`)

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>
#include <assert.h>
typedef struct {
    char *const *cmd1_argv;
    char *const *cmd2_argv;
} PipelineConfig;
bool execute_pipeline(const PipelineConfig *config, int *out_status1, int *out_status2) {
    if (!config || !config->cmd1_argv || !config->cmd2_argv) return false;
    int pipefd[2];
    if (pipe(pipefd) == -1) {
        perror("pipe creation failed");
        return false;
    }
    // =========================================================================
    // Fork Child 1: Writer (cmd1)
    // =========================================================================
    pid_t pid1 = fork();
    if (pid1 < 0) {
        perror("fork child 1 failed");
        close(pipefd[0]);
        close(pipefd[1]);
        return false;
    }
    if (pid1 == 0) {
        // Child 1 Execution Context
        close(pipefd[0]); // Close unused read end
        // Redirect STDOUT to pipe write end
        if (dup2(pipefd[1], STDOUT_FILENO) == -1) {
            perror("dup2 child 1 failed");
            close(pipefd[1]);
            _exit(EXIT_FAILURE);
        }
        close(pipefd[1]); // Close original FD after duplicating
        execvp(config->cmd1_argv[0], config->cmd1_argv);
        perror("execvp cmd1 failed");
        _exit(127); // Standard command-not-found code
    }
    // =========================================================================
    // Fork Child 2: Reader (cmd2)
    // =========================================================================
    pid_t pid2 = fork();
    if (pid2 < 0) {
        perror("fork child 2 failed");
        close(pipefd[0]);
        close(pipefd[1]);
        // Clean up child 1
        waitpid(pid1, NULL, 0);
        return false;
    }
    if (pid2 == 0) {
        // Child 2 Execution Context
        close(pipefd[1]); // Close unused write end
        // Redirect STDIN to pipe read end
        if (dup2(pipefd[0], STDIN_FILENO) == -1) {
            perror("dup2 child 2 failed");
            close(pipefd[0]);
            _exit(EXIT_FAILURE);
        }
        close(pipefd[0]); // Close original FD after duplicating
        execvp(config->cmd2_argv[0], config->cmd2_argv);
        perror("execvp cmd2 failed");
        _exit(127);
    }
    // =========================================================================
    // Parent Process Context: CRITICAL CLEANUP
    // =========================================================================
    // MUST close both pipe ends in parent so child 2 receives EOF when child 1 finishes!
    close(pipefd[0]);
    close(pipefd[1]);
    // Reap both children cleanly
    int status1 = 0, status2 = 0;
    while (waitpid(pid1, &status1, 0) == -1) {
        if (errno != EINTR) break;
    }
    while (waitpid(pid2, &status2, 0) == -1) {
        if (errno != EINTR) break;
    }
    if (out_status1) *out_status1 = status1;
    if (out_status2) *out_status2 = status2;
    return true;
}
int main(void) {
    printf("=======================================================\n");
    printf("      POSIX PIPELINE ENGINE: 'echo' | 'tr' Pipeline    \n");
    printf("=======================================================\n\n");
    // Command 1: echo "systems programming in c 2026"
    char *cmd1[] = { "echo", "systems programming in c 2026", NULL };
    // Command 2: tr 'a-z' 'A-Z' (converts incoming stdin stream to uppercase)
    char *cmd2[] = { "tr", "a-z", "A-Z", NULL };
    PipelineConfig pipeline = {
        .cmd1_argv = cmd1,
        .cmd2_argv = cmd2
    };
    printf("Executing: echo \"systems programming in c 2026\" | tr 'a-z' 'A-Z'\n");
    printf("Pipeline Output:\n----------------------------------------\n");
    fflush(stdout); // Flush parent stdout before pipeline runs!
    int st1 = 0, st2 = 0;
    bool ok = execute_pipeline(&pipeline, &st1, &st2);
    assert(ok);
    printf("----------------------------------------\n");
    printf("[+] Both children reaped successfully.\n");
    if (WIFEXITED(st1)) {
        printf("    Cmd1 (echo) exited with code: %d\n", WEXITSTATUS(st1));
    }
    if (WIFEXITED(st2)) {
        printf("    Cmd2 (tr)   exited with code: %d\n", WEXITSTATUS(st2));
    }
    return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Hanging Pipe Deadlock & The Double-Flush Bug

Examine the following buggy pipeline implementation:

```c
Examine the following buggy pipeline implementation:#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
// BUGGY CODE: Identify 3 critical systems-level bugs
void run_buggy_pipe(char *const cmd1[], char *const cmd2[]) {
    printf("Starting pipeline...\n"); // Note: Stdio buffer populated!
    int fds[2];
    pipe(fds); // BUG 1: Unchecked system call!
    if (fork() == 0) {
        dup2(fds[1], 1);
        close(fds[0]);
        execvp(cmd1[0], cmd1);
        // BUG 2: Using exit() instead of _exit() inside failed child!
        exit(1); 
    }
    if (fork() == 0) {
        dup2(fds[0], 0);
        close(fds[1]);
        execvp(cmd2[0], cmd2);
        exit(1);
    }
    // BUG 3: FATAL DEADLOCK! Parent forgot to close fds[1]!
    // Reader child 2 will NEVER see EOF on stdin!
    wait(NULL);
    wait(NULL);
}
```

### Analysis of Vulnerabilities:

1. **The Hanging Pipe Deadlock:** The parent process keeps `fds[1]` (the write end) open in its own file descriptor table. The second child reading from `fds[0]` will never receive EOF (`read() == 0`) and hangs indefinitely in an unkillable deadlock!
2. **The Stdio Double-Flush Bug:** `printf("Starting pipeline...\n")` writes to userspace `stdout` buffer. When `fork()` is called, the unwritten buffer is cloned into the child. When the child or parent exits, the buffer flushes twice, corrupting pipeline output. Always call `fflush(NULL)` prior to `fork()`, and call `_exit()` (not `exit()`) in the child!
3. **Unchecked Return Codes:** If `pipe()` or `fork()` fails (e.g. process limit `EAGAIN` reached), dereferencing or continuing execution spawns runaway zombie processes.

### Defensive Fix:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>
void run_defensive_pipe(char *const cmd1[], char *const cmd2[]) {
    // 1. Flush stdio buffers BEFORE fork to prevent duplication
    fflush(stdout);
    int fds[2];
    if (pipe(fds) == -1) {
        perror("pipe error");
        return;
    }
    pid_t p1 = fork();
    if (p1 < 0) {
        perror("fork 1 error");
        close(fds[0]);
        close(fds[1]);
        return;
    }
    if (p1 == 0) {
        close(fds[0]);
        if (dup2(fds[1], STDOUT_FILENO) == -1) {
            _exit(EXIT_FAILURE);
        }
        close(fds[1]);
        execvp(cmd1[0], cmd1);
        _exit(127); // Clean kernel exit without flushing parent buffers
    }
    pid_t p2 = fork();
    if (p2 < 0) {
        perror("fork 2 error");
        close(fds[0]);
        close(fds[1]);
        waitpid(p1, NULL, 0);
        return;
    }
    if (p2 == 0) {
        close(fds[1]);
        if (dup2(fds[0], STDIN_FILENO) == -1) {
            _exit(EXIT_FAILURE);
        }
        close(fds[0]);
        execvp(cmd2[0], cmd2);
        _exit(127);
    }
    // CRITICAL: Close BOTH descriptors in the parent to allow EOF propagation!
    close(fds[0]);
    close(fds[1]);
    // Robust reap with EINTR retry loop
    int st1, st2;
    while (waitpid(p1, &st1, 0) == -1 && errno == EINTR);
    while (waitpid(p2, &st2, 0) == -1 && errno == EINTR);
}
```
