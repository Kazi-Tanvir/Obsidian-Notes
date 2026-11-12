---
title: "PRAC GUI 01 to 05 - iup basics"
aliases:
  - iup basics
  - gui 01 to 05
tags:
  - type/practice
  - c/gui-iup
  - c/functions
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/image_editor/gui/"
up: "[[PRAC - Index]]"
next: "[[PRAC GUI 06 - red bmp]]"
related:
  - "[[PROJ Image Editor - gui]]"
  - "[[PROJ Image Editor - main]]"
created: 2026-10-29
status: draft
---
# PRAC GUI 01 to 05 - iup basics

> [!abstract] Summary
> Progressive step-by-step tutorial introducing the fundamentals of the IUP GUI toolkit: message popups, empty dialogs, button controls, hierarchical container layouts (`Vbox`/`Hbox`), and callback binding.

**Source:** `PRACTICE/image_editor/gui/` (`01_hello world.c` through `05_practice.c`)

## Problem
Learn graphical user interface development in C from first principles, stepping progressively from the simplest message alert dialog to structured multi-button layout containers.

## Concepts used
- **IUP Subsystem Lifecycle:** `IupOpen`, `IupClose`, `IupMainLoop`.
- **UI Components:**
  - `IupMessage("Title", "Body")`: Quick native alert dialog.
  - `IupDialog(child)`: Top-level desktop application window.
  - `IupButton("Text", "Action")`: Clickable push-button control.
- **Hierarchical Layout Boxes:**
  - `IupVbox(...)`: Arranging children vertically in a column.
  - `IupHbox(...)`: Arranging children horizontally in a row.
- **Event Callbacks:** Binding C functions to user interactions (`IupSetCallback`).

---

## Tutorial Steps & Code

### Step 1: Hello World (`01_hello world.c`)
Displays a simple modal native desktop message popup box.
```c

```

### Step 2: Empty Window Dialog (`02_dialog.c`)
Instantiates an empty native desktop window with title, custom width/height dimensions, and enters `IupMainLoop()`.
```c
#include <iup.h>
#include<stdio.h>

int main(int argc, char **argv) {
    IupOpen(&argc, &argv);

    Ihandle *label = IupLabel("Hello, World!");
    // Ihandle *hbox = IupHbox(label, NULL);

    Ihandle *dlg = IupDialog(label);
    IupSetAttribute(dlg, "TITLE", "My First IUP App");
    IupSetAttribute(dlg, "SIZE", "400x200");

    IupShowXY(dlg, IUP_CENTER, IUP_CENTER); 
    IupMainLoop();

    IupDestroy(dlg);
    IupClose();
    return 0;
}
```

### Step 3: Interactive Button (`03_button.c`)
Embeds an interactive button inside a dialog that triggers a message callback when clicked.
```c
#include<iup.h>
#include<stdio.h>

static int buttonClick(Ihandle *self){
    (void)self;
    printf("Button clicked!\n");
    return IUP_DEFAULT;
}

int main(int argc, char **argv){
    IupOpen(&argc, &argv);
    
    Ihandle *btn = IupButton("Click Me", NULL);
    IupSetCallback(btn, "ACTION", buttonClick);

    Ihandle *dlg = IupDialog(btn);
    IupSetAttribute(dlg, "TITLE", "My First IUP App");
    IupSetAttribute(dlg, "SIZE", "400x200");

    IupShowXY(dlg, IUP_CENTER, IUP_CENTER);
    IupMainLoop();

    IupDestroy(dlg);
    IupClose();
    return 0;
}
```

### Step 4: Vertical & Horizontal Boxes (`04_vbox_hbox.c`)
Demonstrates coordinate-free layout management by nesting `IupHbox` and `IupVbox` containers.
```c
#include <iup.h>
#include<stdio.h>

static int ok_action(Ihandle *self) {
    (void)self;
    printf("OK clicked!\n");
    return IUP_DEFAULT;
}

static int cancel_action(Ihandle *self) {
    (void)self;
    printf("Cancel clicked!\n");
    return IUP_DEFAULT;
}

int main(int argc, char **argv) {
    IupOpen(&argc , &argv);

    Ihandle *label = IupLabel("Enter name : ");
    Ihandle *text_box = IupText(NULL);

    IupSetAttribute(text_box , "EXPAND" , "HORIZONTAL");

    Ihandle *button_ok = IupButton("OK", NULL);
    Ihandle *button_cancel = IupButton("Cancel", NULL);

    IupSetCallback(button_ok, "ACTION", ok_action);
    IupSetCallback(button_cancel, "ACTION", cancel_action);

    Ihandle *button_row = IupHbox(
        IupFill(),
        button_ok,
        button_cancel,
        NULL
    );
    IupSetAttribute(button_row, "GAP",  "10");

    Ihandle *main_layout = IupVbox(
        label,
        text_box,
        button_row,
        NULL
    );

    IupSetAttribute(main_layout , "GAP", "10");
    IupSetAttribute(main_layout, "MARGIN","15x15");

    Ihandle *dlg = IupDialog(main_layout);

    IupSetAttribute(dlg, "TITLE", "Box Layout Example");
    IupSetAttribute(dlg, "RASTERSIZE", "320x180");

    IupShowXY(dlg, IUP_CENTER, IUP_CENTER);
    IupMainLoop();
    IupClose();

    return 0;
}
```

### Step 5: Layout Practice (`05_practice.c`)
Synthesizes layouts with interactive button events, setting up the foundation for desktop application development.
```c
#include<iup.h>
#include<stdio.h>

static int msgfunc(Ihandle *self){
    (void)self;
    IupMessage("Hi","Hello from callback!");
    return IUP_DEFAULT;
}

int main(int argc , char **argv){
    IupOpen(&argc, &argv);
    
    Ihandle *lbl = IupLabel("Hello, Iup!");
    Ihandle *btn = IupButton("Say Hi !",NULL);
    Ihandle *hbox = IupHbox(lbl,IupFill(),btn,NULL);
    Ihandle *dlg = IupDialog(hbox);

    IupSetCallback(btn,"ACTION",msgfunc);

    IupSetAttribute(dlg, "RASTERSIZE", "400x200");
    IupSetAttribute(dlg, "TITLE", "My First Window");
    IupShowXY(dlg,IUP_CENTER,IUP_CENTER);

    IupMainLoop();
    IupClose();

    return 0;
}
```

## How it works
1. Every program initializes IUP via `IupOpen(&argc, &argv)`.
2. Widgets are instantiated from leaf controls (buttons, labels) upward into container boxes (`Vbox`, `Hbox`).
3. Top-level container is passed to `IupDialog()`.
4. `IupShow(dlg)` realizes the native Win32 window and `IupMainLoop()` processes desktop events.
5. `IupClose()` cleanly shuts down toolkit subsystems.

## Sample run
```text
(Launches native desktop windows displaying styled buttons and message prompts)
```

## Gotchas
> [!warning] NULL Sentinel in Box Constructors
> In IUP, container constructors like `IupVbox(btn1, btn2, NULL)` and `IupHbox(...)` require a trailing `NULL` sentinel argument to signal the end of the variable-length argument list. Omitting `NULL` causes memory access violations.

## My notes
> [!question]- My notes

## Related
- [[PROJ Image Editor - gui]]
- [[PROJ Image Editor - main]]
