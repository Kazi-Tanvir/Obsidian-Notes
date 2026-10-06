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

---

### Standard File Descriptors

----------------------------------------------------------------------- Integer Value     POSIX Constant    Description       Standard Stream ----------------- ----------------- ----------------- ----------------- 0                 STDIN_FILENO      Standard Input    stdin

1                 STDOUT_FILENO     Standard Output   stdout

2                 STDERR_FILENO     Standard Error    stderr -----------------------------------------------------------------------

### Low-Level File I/O (<unistd.h>, <fcntl.h>)

int fd = open("log.bin", O_WRONLY | O_CREAT | O_TRUNC, 0644); // User rw-, group r--, others r--

ssize_t bytes_written = write(fd, buffer, count);

ssize_t bytes_read = read(fd, buffer, sizeof(buffer));

off_t new_pos = lseek(fd, 0, SEEK_SET);

close(fd);

### Process Control & Lifecycle API (<sys/wait.h>, <unistd.h>)

pid_t pid = fork();

if (pid < 0) {

perror("fork failed");

} else if (pid == 0) {

// Child Process

char *args[] = { "grep", "root", "/etc/passwd", NULL };

execvp("grep", args);

// If execvp returns, it failed!

perror("execvp failed");

_exit(EXIT_FAILURE); // MUST use _exit() in child, NOT exit()!

} else {

// Parent Process

int status;

waitpid(pid, &status, 0); // Wait for child to finish

if (WIFEXITED(status)) {

printf("Child exited with code: %d\\n", WEXITSTATUS(status));

}

}

### Redirection & IPC (pipe, dup2)

int pipefd[2];

pipe(pipefd); // pipefd[0] = Read End, pipefd[1] = Write End

// Redirect STDOUT to pipe's write end:

dup2(pipefd[1], STDOUT_FILENO);

close(pipefd[1]); // Close original descriptor after dup2!

## 2. In-Depth Theory & Low-Level Mechanics

---

### A. The Three-Tier Kernel File Table Architecture

When a C process performs I/O, the operating system kernel maintains three distinct data structures:Process A (PID 1001) Open File Description Table (Kernel) Inode Table (VFS / Disk)

```text
┌───────────────────────┐             ┌─────────────────────────────┐         ┌────────────────────────┐
│ FD 0 (stdin)          │             │ File Offset: 1024           │         │ Inode #99211 (file.txt)│
│ FD 1 (stdout)         │             │ Status Flags: O_RDWR        │ ──────► │ File Size: 4096 bytes  │
│ FD 3 ─────────────────┼───────────► │ Ref Count: 2                │         │ Permissions: -rw-r--r--│
└───────────────────────┘             └──────────────┬──────────────┘         └────────────────────────┘
```

▲

```text
Process B (Child PID 1002)                           │
┌───────────────────────┐                            │
│ FD 3 (Inherited) ─────┼────────────────────────────┘
└───────────────────────┘
```

1.  **Per-Process File Descriptor Table:** An array indexed by the integer FD. Each entry holds flags (e.g. FD_CLOEXEC) and a pointer to an Open File Description in kernel space.

2.  **System-Wide Open File Description Table:** Contains the **current byte offset** in the file, file status flags (O_APPEND, O_NONBLOCK), and a reference count.

3.  **VFS Inode Table:** Represents the physical disk object containing file metadata, ownership, and blocks on physical storage.

#### What happens during fork()?

- The child process receives an exact **duplicate of the parent's File Descriptor Table**.

- Both parent and child FD 3 point to the **same Open File Description** in kernel memory!

- **Crucial Implication:** If the child advances the file offset via read() or lseek(), the parent's file offset moves concurrently. They share the same seek head.

### B. Virtual Memory Copy-on-Write (CoW) & _exit vs exit

When fork() is called:

- The kernel does not copy the parent's physical RAM pages (which could take hundreds of milliseconds for a large program).

- Instead, it marks all page table entries as **Read-Only** and duplicates only the page table references (**Copy-on-Write**).

- Only when either process attempts to modify a page does the CPU trigger a page fault, prompting the kernel to allocate a new physical frame.

#### The _exit() vs exit() Rule:

- Calling standard C exit() flushes all C stdio userspace buffers (FILE
  * streams like stdout) and executes atexit() handlers.

- If a child fails an execve() and calls exit(), it **flushes the parent's pending stdio buffers**, resulting in duplicated outputs in the terminal or log files.

- **The Rule:** Always terminate a child process with POSIX _exit() (or _Exit()), which terminates the process immediately at kernel level without flushing C runtime library buffers.

### C. The Zombie and Orphan Process Lifecycles

- **Zombie Process (<defunct>):** When a child terminates, its memory and open file descriptors are freed, but its entry in the kernel's process table remains. The kernel retains its PID, exit code, and resource usage statistics until the parent calls wait() or waitpid(). If the parent never reaps it, the zombie lingers, exhausting system PIDs.

- **Orphan Process:** If the parent process crashes or terminates before its children, the children become orphans. They are immediately adopted by the system supervisor process (init / PID 1 or systemd), which automatically reaps them upon termination.

### D. The Mechanics of a UNIX pipe()

A pipe is a unidirectional FIFO byte stream managed directly in kernel RAM (typically a 64KB circular ring buffer):

- **Write End (pipefd[1]):** Writers append bytes to the buffer. If the buffer is full, write() blocks until space becomes available.

- **Read End (pipefd[0]):** Readers consume bytes. If the buffer is empty, read() blocks until bytes arrive.

#### The Two Fatal Pipeline Bugs:

1.  **The Hanging Reader (Deadlock):** A read() on a pipe will only return 0 (EOF) when **ALL open file descriptors pointing to the write end across ALL processes are closed**. If the parent process creates a pipe, forks a reader and a writer, and forgets to close(pipefd[1]) in itself, the reader will **hang forever**, waiting for more input that never arrives!

2.  **The Broken Pipe (SIGPIPE):** If a process calls write() on a pipe where all read ends have been closed, the kernel sends the SIGPIPE signal to the writer (which terminates the process by default) and sets errno = EPIPE.

## 3. Thoughtful Mini-Project (~1 Hour Scope)

---

### Project Title: Mini UNIX Shell Pipeline Engine (posix_pipeline)

#### Objective

Build a robust, programmatic pipeline executor in C that executes a two-command pipeline (cmd1 | cmd2) using raw POSIX system calls (pipe, fork, dup2, execvp, and waitpid), guaranteeing zero descriptor leaks and full exit status diagnostics.

#### Complete Implementation (pipeline_engine.c)

##include <stdio.h>

##include <stdlib.h>

##include <stdint.h>

##include <stdbool.h>

##include <string.h>

##include <unistd.h>

##include <sys/types.h>

##include <sys/wait.h>

##include <errno.h>

##include <assert.h>

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

printf("=======================================================\\n");

printf(" POSIX PIPELINE ENGINE: 'echo' | 'tr' Pipeline \\n");

printf("=======================================================\\n\\n");

// Command 1: echo "systems programming in c 2026"

char *cmd1[] = { "echo", "systems programming in c 2026", NULL };

// Command 2: tr 'a-z' 'A-Z' (converts incoming stdin stream to uppercase)

char *cmd2[] = { "tr", "a-z", "A-Z", NULL };

PipelineConfig pipeline = {

.cmd1_argv = cmd1,

.cmd2_argv = cmd2

};

printf("Executing: echo \\"systems programming in c 2026\\" | tr 'a-z' 'A-Z'\\n");

printf("Pipeline Output:\\n----------------------------------------\\n");

fflush(stdout); // Flush parent stdout before pipeline runs!

int st1 = 0, st2 = 0;

bool ok = execute_pipeline(&pipeline, &st1, &st2);

assert(ok);

printf("----------------------------------------\\n");

printf("[+] Both children reaped successfully.\\n");

if (WIFEXITED(st1)) {

printf(" Cmd1 (echo) exited with code: %d\\n", WEXITSTATUS(st1));

}

if (WIFEXITED(st2)) {

printf(" Cmd2 (tr) exited with code: %d\\n", WEXITSTATUS(st2));

}

return 0;

}

## 4. Error Handling & Defensive Programming Challenge

---

### Scenario: The Hanging Pipe Deadlock & The Double-Flush Bug

Examine the following buggy pipeline implementation:#include <stdio.h>

##include <stdlib.h>

##include <unistd.h>

##include <sys/wait.h>

// BUGGY CODE: Identify 3 critical systems-level bugs

void run_buggy_pipe(char *const cmd1[], char *const cmd2[]) {

printf("Starting pipeline\...\\n"); // Note: Stdio buffer populated!

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

### Analysis of Vulnerabilities:

1.  **The Hanging Pipe Deadlock:** The parent process keeps fds[1] (the write end) open while waiting for the children to exit. Because the kernel sees at least one active write descriptor (parent's fds[1]), it never generates an EOF (0 bytes returned) on fds[0]. Child 2 blocks on read() forever. The program hangs indefinitely.

2.  **The Stdio Double-Flush Bug:** printf("Starting pipeline\...\\n") writes to the userspace FILE * buffer. When fork() is called, the child inherits the dirty userspace buffer. Calling exit(1) in the child triggers a stdio flush, causing "Starting pipeline\...\\n" to be printed multiple times. Calling _exit(1) bypasses userspace stream cleanup.

3.  **Unchecked Return Codes:** If pipe() or fork() fails (e.g. process limit EAGAIN reached), the function proceeds with invalid descriptors (-1), causing undefined behavior and orphaned children.

### Defensive Fix:

##include <stdio.h>

##include <stdlib.h>

##include <unistd.h>

##include <sys/wait.h>

##include <errno.h>

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
