---
tags:
  - c
  - static-libraries
  - shared-libraries
  - position-independent-code
  - dynamic-loading
  - dlopen-dlsym
date: 2026-09-15
day: 24
---

# Day 24: Static vs Dynamic Libraries, Position Independent Code & Dynamic Loading

---

## 1. Quick Reference & Cheat Sheet

### Static vs Shared Libraries Comparison

| Feature | Static Archive (`.a` / `.lib`) | Dynamic / Shared Object (`.so` / `.dll`) |
| :--- | :--- | :--- |
| **Link Time** | Copied directly into final executable (`ar rcs`). | References resolved; symbols remain external. |
| **Binary Size** | Large (Code duplicated across every consumer binary). | Small (Code resides in single external file on disk). |
| **RAM Footprint** | Duplicate text pages in RAM per running process. | Single physical memory page shared across all processes. |
| **Updates** | Requires full relink of all consumers. | Drop-in replacement without relinking consumers. |
| **Load Mechanics** | OS loads single contiguous binary image. | Dynamic linker (`ld.so`) loads dependent libraries. |

### Critical Linker Rule: Order Sensitivity

The GNU linker (`ld`) processes object files and archives sequentially from **Left to Right**:
- It maintains an internal list of *Unresolved Symbols*.
- When an object file (`main.o`) is encountered, its undefined symbols are added to the list.
- When an archive (`libmath.a`) is encountered, the linker extracts *only* the members that resolve current unresolved symbols.
- If you place the library *before* the consumer on the command line:

```bash
gcc -L. -lmath main.o -o app # Linker error: undefined reference to 'compute'!
```

The linker visits `libmath.a` first, sees *zero* unresolved symbols, discards the library, and then encounters `main.o`, leaving symbols unresolved!

**Correct Link Order:**

```bash
gcc main.o -L. -lmath -o app # Correct!
```

### Dynamic Loading API (`<dlfcn.h>`)

```c
#include <dlfcn.h>
// 1. Open shared object
void *handle = dlopen("./libplugin.so", RTLD_NOW | RTLD_LOCAL);
if (!handle) { fprintf(stderr, "%s\n", dlerror()); exit(1); }
// 2. Clear pre-existing error flag
dlerror();
// 3. Resolve symbol address (POSIX-compliant function pointer assignment)
int (*init_fn)(void);
*(void **)(&init_fn) = dlsym(handle, "plugin_init");
char *err = dlerror();
if (err != NULL) { fprintf(stderr, "dlsym error: %s\n", err); dlclose(handle); exit(1); }
// 4. Invoke function
init_fn();
// 5. Unload shared object
dlclose(handle);
```

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Position Independent Code (-fPIC) & GOT/PLT Mechanics

When building a shared library, code cannot contain hardcoded absolute memory addresses because the OS ASLR (Address Space Layout Randomization) loads the `.so` at an arbitrary, non-deterministic base address for each process.

`-fPIC` forces the compiler to generate relative addressing using two indirection tables:
1. **Global Offset Table (GOT):** Resides in the writable `.data` segment. Stores absolute pointers to global variables.
2. **Procedure Linkage Table (PLT):** Resides in the executable `.text` segment. Implements lazy symbol resolution for function calls via dynamic linker trampolines.

### B. Dynamic Symbol Resolution: `RTLD_NOW` vs `RTLD_LAZY`, `RTLD_GLOBAL` vs `RTLD_LOCAL`

- `RTLD_NOW`: Resolves all undefined symbols immediately before `dlopen()` returns. Essential for mission-critical software to fail-fast on missing dependencies.
- `RTLD_LAZY`: Resolves function symbols only when they are first called.
- `RTLD_GLOBAL`: Makes symbols defined in this shared library available to subsequently loaded libraries.
- `RTLD_LOCAL`: Symbols remain private to this library (Default, best practice to prevent symbol collisions).

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Extensible Dynamic Plugin Engine (`c_plugin_loader`)

#### Objective

Build an extensible plugin architecture in C where a host application dynamically discovers, loads, executes, and unloads shared object (`.so`) plugins at runtime without recompilation.

#### Directory Layout

```text
plugin_project/
├── Makefile
├── include/
│   └── plugin_api.h
├── plugins/
│   ├── plugin_uppercase.c
│   └── plugin_rot13.c
└── src/
    └── host_main.c
```

#### 1. The Common Plugin API (`include/plugin_api.h`)

```c
#define PLUGIN_API_H
#include <stdint.h>
#define PLUGIN_MAGIC 0x504C5547 // "PLUG"
typedef struct {
    uint32_t magic;
    const char *name;
    const char *version;
    int  (*init)(void);
    void (*process)(char *io_text);
    void (*shutdown)(void);
} PluginDescriptor;
```

#### 2. Plugin Implementation: Uppercase Transformer (`plugins/plugin_uppercase.c`)

```c
#define EXPORT_PLUGIN(desc) \
    __attribute__((visibility("default"))) const PluginDescriptor plugin_export = desc
#endif // PLUGIN_API_H
2. Plugin 1: Uppercase Converter (plugins/plugin_uppercase.c)
#include <stdio.h>
#include <ctype.h>
#include <stdint.h>
#include "plugin_api.h"
static int upper_init(void) {
    printf("  [Uppercase Plugin] Initialized.\n");
    return 0;
}
static void upper_process(char *text) {
    if (!text) return;
    for (int i = 0; text[i] != '\0'; i++) {
        text[i] = (char)toupper((unsigned char)text[i]);
    }
}
```

#### 3. Plugin Implementation: Rot13 Cipher (`plugins/plugin_rot13.c`)

```c
    printf("  [Uppercase Plugin] Shut down successfully.\n");
}
static const PluginDescriptor s_desc = {
    .magic    = PLUGIN_MAGIC,
    .name     = "Uppercase Transformer",
    .version  = "1.0.0",
    .init     = upper_init,
    .process  = upper_process,
    .shutdown = upper_shutdown
};
EXPORT_PLUGIN(s_desc);
3. Plugin 2: ROT13 Cipher (plugins/plugin_rot13.c)
#include <stdio.h>
#include <stdint.h>
#include "plugin_api.h"
static int rot13_init(void) {
    printf("  [ROT13 Plugin] Initialized.\n");
    return 0;
```

#### 4. The Host Application (`src/host_main.c`)

```c
static void rot13_process(char *text) {
    if (!text) return;
    for (int i = 0; text[i] != '\0'; i++) {
        char c = text[i];
        if (c >= 'a' && c <= 'z') {
            text[i] = (char)('a' + (c - 'a' + 13) % 26);
        } else if (c >= 'A' && c <= 'Z') {
            text[i] = (char)('A' + (c - 'A' + 13) % 26);
        }
    }
}
static void rot13_shutdown(void) {
    printf("  [ROT13 Plugin] Shut down successfully.\n");
}
static const PluginDescriptor s_desc = {
    .magic    = PLUGIN_MAGIC,
    .name     = "ROT13 Cipher",
    .version  = "2.1.0",
    .init     = rot13_init,
    .process  = rot13_process,
    .shutdown = rot13_shutdown
};
EXPORT_PLUGIN(s_desc);
4. The Host Application (src/host_main.c)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <dlfcn.h>
#include "plugin_api.h"
typedef struct {
    void *lib_handle;
    const PluginDescriptor *descriptor;
} LoadedPlugin;
LoadedPlugin *plugin_load(const char *path) {
    // 1. Open shared object
    void *handle = dlopen(path, RTLD_NOW | RTLD_LOCAL);
    if (!handle) {
        fprintf(stderr, "[-] dlopen failed: %s\n", dlerror());
        return NULL;
    }
    // 2. Clear any pre-existing dlerror
    dlerror();
    // 3. Resolve export symbol
    const PluginDescriptor *desc = NULL;
    *(const void **)(&desc) = dlsym(handle, "plugin_export");
    char *err = dlerror();
    if (err != NULL || !desc) {
        fprintf(stderr, "[-] dlsym failed: %s\n", err ? err : "NULL descriptor");
        dlclose(handle);
        return NULL;
    }
    // 4. Validate magic
    if (desc->magic != PLUGIN_MAGIC) {
        fprintf(stderr, "[-] Invalid plugin magic in %s\n", path);
        dlclose(handle);
        return NULL;
    }
    // 5. Initialize plugin
    if (desc->init && desc->init() != 0) {
        fprintf(stderr, "[-] Plugin initialization rejected by %s\n", desc->name);
        dlclose(handle);
        return NULL;
    }
    LoadedPlugin *plug = (LoadedPlugin *)malloc(sizeof(LoadedPlugin));
    plug->lib_handle = handle;
    plug->descriptor = desc;
    return plug;
}
void plugin_unload(LoadedPlugin *plug) {
    if (!plug) return;
    if (plug->descriptor->shutdown) {
        plug->descriptor->shutdown();
    }
    dlclose(plug->lib_handle);
    free(plug);
}
int main(void) {
    printf("=======================================================\n");
    printf("     DYNAMIC PLUGIN ENGINE (dlopen / dlsym Runtime)     \n");
    printf("=======================================================\n\n");
    const char *plugin_paths[] = {
        "./plugins/libplugin_uppercase.so",
        "./plugins/libplugin_rot13.so"
    };
    size_t count = sizeof(plugin_paths) / sizeof(plugin_paths[0]);
    for (size_t i = 0; i < count; i++) {
        printf("[*] Loading plugin: %s\n", plugin_paths[i]);
        LoadedPlugin *plug = plugin_load(plugin_paths[i]);
        if (!plug) continue;
        printf("    Plugin Active: %s (v%s)\n", 
               plug->descriptor->name, plug->descriptor->version);
        char buffer[128];
        strcpy(buffer, "Hello Systems World! 2026");
```

#### 5. The Complete Automated Makefile (`Makefile`)

```makefile
        // Execute transformation
        plug->descriptor->process(buffer);
        printf("    Processed Text: \"%s\"\n", buffer);
        // Clean unload
        plugin_unload(plug);
        printf("[+] Unloaded.\n\n");
    }
    return 0;
}
5. Build Automation (Makefile)
CC      := gcc
CFLAGS  := -std=c17 -Wall -Wextra -Wpedantic -O2
LDFLAGS := -ldl
all: host plugins
host: bin/host_app
plugins: plugins/libplugin_uppercase.so plugins/libplugin_rot13.so
bin/host_app: src/host_main.c include/plugin_api.h | bin
$(CC) $(CFLAGS) -Iinclude $< $(LDFLAGS) -o $@
plugins/%.so: plugins/%.c include/plugin_api.h
$(CC) $(CFLAGS) -fPIC -shared -Iinclude $< -o $@
bin:
mkdir -p bin
run: all
./bin/host_app
clean:
rm -rf bin plugins/*.so
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Dangling Symbol Pointer & Memory Fault After `dlclose()`

Examine the following buggy dynamic plugin executor:

```c
#include <stdlib.h>
#include <dlfcn.h>
typedef void (*action_fn)(void);
// BUGGY CODE: Look for severe memory safety bugs
action_fn load_and_get_action(const char *path) {
    void *h = dlopen(path, RTLD_LAZY);
    if (!h) return NULL;
    action_fn fn = (action_fn)dlsym(h, "run_action"); // BUG 1: dlerror() unchecked!
    // BUG 2: dlclose unmaps the shared library's .text pages from virtual memory!
    dlclose(h);
    // BUG 3: Returns function pointer into unmapped memory!
    return fn; 
}
int main(void) {
    action_fn act = load_and_get_action("./libaction.so");
    if (act) {
        act(); // FATAL: SIGSEGV / Crash! Executing unmapped memory page!
    }
    return 0;
}
```

### Analysis of Vulnerabilities:

1. **Unmapped Page Execution (Use-After-Close):** Calling `dlclose(h)` decrements the reference count of the shared library. When it reaches zero, `munmap()` is invoked on the library's `.text` and `.data` segments. Calling `act()` immediately triggers a segmentation fault (`SIGSEGV`) because the code is no longer mapped in memory.
2. **Missing `dlerror()` Verification:** Testing `if (fn)` is insufficient. A valid symbol address can coincidentally be `NULL`, or a prior error can corrupt diagnostics. You must call `dlerror()` to clear errors before `dlsym()`, and verify its return value afterward.
3. **ISO C Pointer Conversion Warning:** Direct cast `(action_fn)dlsym(...)` triggers compiler warnings under strict `-Wpedantic`. POSIX recommends casting through `*(void **)(&fn)`.

### Defensive Fix:

```c
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>
typedef struct {
    void *handle;
    void (*run_action)(void);
} SafePluginContext;
SafePluginContext *safe_plugin_init(const char *path) {
    void *h = dlopen(path, RTLD_NOW | RTLD_LOCAL);
    if (!h) {
        fprintf(stderr, "dlopen error: %s\n", dlerror());
        return NULL;
    }
    dlerror(); // Clear error state
    void (*fn)(void) = NULL;
    *(void **)(&fn) = dlsym(h, "run_action"); // POSIX-compliant assignment
    char *err = dlerror();
    if (err != NULL || !fn) {
        fprintf(stderr, "dlsym error: %s\n", err ? err : "NULL function pointer");
        dlclose(h);
        return NULL;
    }
    SafePluginContext *ctx = (SafePluginContext *)malloc(sizeof(SafePluginContext));
    ctx->handle = h;
    ctx->run_action = fn;
    return ctx;
}
void safe_plugin_destroy(SafePluginContext *ctx) {
    if (!ctx) return;
    // Only unload shared library AFTER all invocations have completed!
    dlclose(ctx->handle);
    free(ctx);
}
```
