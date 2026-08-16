# Appendix C: Building a Windows Skeleton

C is a popular language for Windows programming. As such, it makes sense that some coverage of this important topic be included in this book. But be forewarned: Programming for Windows requires a thorough knowledge of both C and Windows. Frankly, before you can write useful Windows programs, you will need to hone your C programming skills and then invest substantial time in learning the ins and outs of the Windows operating system. Keep in mind that just a description of the functions available within Windows requires approximately 2,000 printed pages!

The preceding notwithstanding, if you will be moving on to Windows programming, you are probably anxious to begin. The purpose of this appendix is to give you a brief overview of Windows programming and to explain a few of its most fundamental elements. In essence, the information presented here is designed to give you a "jump start" into the world of Windows programming.

This appendix discusses in a general way what Windows is, how a program must interact with it, and what rules must be followed by every Windows application. It also develops an application skeleton that you can use as a basis for your own Windows programs. As you will see, all Windows programs share several common traits. It is these shared attributes that will be contained in the application skeleton.

---

## WHICH VERSION OF WINDOWS?

At the time of this writing, there are three versions of the Windows operating system in common use: Windows 3.1, Windows 95, and Windows NT. The skeleton developed in this appendix is designed for 32-bit versions of Windows, such as Windows 95 or Windows NT, since these are the most widely used versions. However, the basic principles apply to all versions of Windows.

---

## WINDOWS PROGRAMMING PERSPECTIVE

The goal of Windows is to enable a person who has basic familiarity with the system to sit down and run virtually any application without prior training. To accomplish this end, Windows provides a consistent interface to the user. In theory, if you can run one Windows-based program, you can run them all. Of course, in actuality, most useful programs will still require some sort of training in order to be used effectively, but at least this instruction can be restricted to what the program *does*, not *how* the user must interact with it. In fact, much of the code in a Windows application is there just to support the user interface.

Before continuing, it must be stated that not every program that runs under Windows will necessarily present the user with a Windows-style interface. It is possible to write Windows programs that do not take advantage of the Windows interface elements. To create a Windows-style program, you must purposely do so. Only those programs written to take advantage of Windows will look and feel like Windows programs. While you can override the basic Windows design philosophy, you had better have a good reason to do so, because the users of your programs will, most likely, be very disappointed. In general, any application programs you are writing for Windows should utilize the normal Windows interface and conform to the standard Windows design practices.

Windows is graphics-oriented, which means that it provides a Graphical User Interface (GUI). While graphics hardware and video modes are quite diverse, many of the differences are handled by Windows. This means that, for the most part, your program does not need to worry about what type of graphics hardware or video mode is being used.

Let's look at a few of the more important features of Windows.

### The Desktop Model

With few exceptions, the point of a window-based user interface is to provide the equivalent of a desktop on the screen. On a desk you might find several different pieces of paper, one on top of another, often with fragments of different pages visible beneath the top page. The equivalent of the desktop in Windows is the screen. The pieces of paper are represented by windows on the screen. On a desk you may move pieces of paper about, maybe switching which piece of paper is on top, or how much of another is exposed to view. Windows allows the same type of operations on its windows. By selecting a window, you can make it current, which means putting it on top of all the other open windows. You can enlarge or shrink a window, or move it about on the screen. In short, Windows lets you control the surface of the screen the way you control the items on your desk.

While the desktop model forms the foundation of the Windows user interface, Windows is not limited by it. In fact, several Windows interface elements emulate other types of familiar devices, such as slider controls, spin controls, property sheets, and toolbars. Windows gives you, the programmer, a large array of features from which you may choose those most appropriate to your specific application.

### The Mouse

Windows allows the use of the mouse for almost all control, selection, and drawing operations. Of course, to say that it allows the use of the mouse is an understatement. The fact is that the Windows interface was *designed* for the mouse—it allows the use of the keyboard! Although it is certainly possible for an application program to ignore the mouse, it does so only in violation of a basic Windows design principle.

### Icons and Bitmaps

Windows encourages the use of icons and bitmaps (graphics images). The theory behind the use of icons and bitmaps is found in the old adage "a picture is worth a thousand words."

An icon is a small symbol that represents some operation or program. Generally, the operation or program can be activated by selecting the icon. A bitmap is often used to convey information quickly and simply to the user. However, bitmaps can also be used as menu elements.

### Menus and Dialog Boxes

Aside from standard windows, Windows also provides several special-purpose windows. The most common of these are the menu and the dialog box. A *menu* is, as you would expect, a special window that contains choices from which the user makes a selection. The thing that makes menus valuable is that they are largely automated. Instead of having to manage menu selection manually in your program, you simply create a standard menu—Windows will handle the details for you.

A *dialog box* is a special window that allows more complex interaction with the application than that allowed by a menu. For example, your application might use a dialog box to request a file name. With few exceptions, non-menu input is accomplished via a dialog box.

---

## HOW WINDOWS AND YOUR PROGRAM INTERACT

When you write a program for many operating systems, it is your program that initiates interaction with the operating system. For example, in a DOS program, it is the program that requests such things as input and output. Put differently, programs written in the "traditional way" call the operating system. The operating system does *not* call your program. However, Windows generally works in the opposite way. It is Windows that calls your program. The process works like this: Your program waits until it is sent a *message* by Windows. The message is passed to your program through a special function that is called by Windows. Once a message is received, your program is expected to take an appropriate action. While your program may call Windows when responding to a message, it is still Windows that initiates the activity. More than anything else, it is the message-based interaction with Windows that dictates the general form of all Windows programs.

There are many different types of messages that Windows may send your program. For example, each time the mouse is clicked on a window belonging to your program, a mouse-clicked message will be sent to your program. Another type of message is sent each time a window belonging to your program must be redrawn. Still another message is sent each time the user presses a key when your program is the focus of input. Keep one fact firmly in mind: As far as your program is concerned, messages arrive randomly. This is why Windows programs resemble interrupt-driven programs. You can't know what message will be next.

One final point: Messages sent to your program are stored in a *message queue* associated with your program. Therefore, no message will be lost because your program is busy processing another message. The message will simply wait in the queue until your program is ready for it.

---

## WINDOWS IS MULTITASKING

Since the start, Windows has been a multitasking operating system. This means that it can run two or more programs concurrently. All 32-bit versions of Windows (such as Windows NT and Windows 95) use *preemptive multitasking*. Using this approach, each active application receives a slice of CPU time. It is during its time slice that an application actually executes. When the application's time slice runs out, the next application begins executing. (The previously executing application enters a suspended state in which it awaits another time slice.) In this fashion, each application in the system receives a portion of CPU time. Although the application skeleton developed in this appendix is not concerned with the multitasking aspects of Windows, they will be an important part of any application you create.

> [!NOTE]
> Older, 16-bit versions of Windows used a form of multitasking called non-preemptive multitasking. With this approach, an application retained the CPU until it explicitly released it. This allowed applications to monopolize the CPU and effectively "lock out" other programs. Preemptive multitasking eliminates this problem.

---

## THE WIN32 API

In general, the Windows environment is accessed through a call-based interface called the Application Program Interface (API). The API consists of several hundred functions that your program calls as needed. The API functions provide all the system services performed by Windows. There is a subset to the API called the Graphics Device Interface (GDI), which is the part of Windows that provides device-independent graphics support. It is the GDI functions that make it possible for a Windows application to run on a variety of hardware.

Programs designed for use by 32-bit versions of Windows, such as Windows 95 and Windows NT, use the Win32 API. For the most part, Win32 is a superset of the older Windows 3.1 API (Win16). Indeed, for the most part, the functions are called by the same name and are used in the same way. However, even though similar in spirit and purpose, the two APIs differ because Win32 supports 32-bit addressing while Win16 supports only the 16-bit, segmented-memory model. Because of this difference, several of the older API functions have been widened to accept 32-bit arguments and return 32-bit values. A few API functions have had to be altered to accommodate the 32-bit architecture. API functions have also been added to support preemptive multitasking, new interface elements, and other enhanced features.

Because modern versions of Windows support 32-bit addressing, it makes sense that integers are also 32 bits long. This means that types **int** and **unsigned** are 32 bits long, not 16 bits, as is the case for Windows 3.1. If you want to use a 16-bit integer, it must be declared as **short**. Windows provides portable typedef names for these types, as you will see shortly.

---

## THE COMPONENTS OF A WINDOW

Before moving on to specific aspects of Windows programming, a few important terms need to be defined. Figure C-1 shows a standard window with each of its elements pointed out.

```
FIGURE C-1
The elements of a standard window

+-------------------------------------------------------------------+
| [X] System menu icon | Title                | [_][^][X] Min/Max/Close |
+-------------------------------------------------------------------+
| Border                                                | | Vertical|
|                                                       | | scroll  |
|                                                       | | bar     |
|                      Client area                      | |         |
|                                                       | |         |
|                                                       | |         |
|                                                       | |         |
|                                                       | |         |
+-------------------------------------------------------+-+---------+
| [ < ] Horizontal scroll bar [ > ]                     | |         |
+-------------------------------------------------------------------+
```

All windows have a border that defines the limits of the window; the borders are also used when resizing the window. At the top of the window are several items. On the far left is the system menu icon (also called the title bar icon). Clicking on this box displays the system menu. To the right of the system menu icon is the window's title. At the far right are the minimize, maximize, and close boxes. The client area is the part of the window in which your program activity takes place. Most windows also have horizontal and vertical scroll bars that are used to move information through the window.

---

## SOME WINDOWS APPLICATION BASICS

Before developing the Windows application skeleton, some basic concepts common to all Windows programs need to be discussed.

### WinMain( )

All Windows programs begin execution with a call to `WinMain()`. (Windows programs do not have a `main()` function.) `WinMain()` has some special properties that differentiate it from other functions in your application. First, it must be compiled using the `WINAPI` calling convention. (You will see `APIENTRY` used as well. They both mean the same thing.) By default, functions in your C programs use the C calling convention. However, it is possible to compile a function so that it uses a different calling convention; Pascal is a common alternative. For various technical reasons, the calling convention Windows uses to call `WinMain()` is `WINAPI`. The return type of `WinMain()` should be **int**.

### THE WINDOW FUNCTION

All Windows programs must contain a special function that is not called by your program, but is called by Windows. This function is generally referred to as the *window function* or the *window procedure*. The window function is called by Windows when it needs to pass a message to your program. It is through this function that Windows communicates with your program. The window function receives the message in its parameters. All window functions must be declared as returning type `LRESULT CALLBACK`. The type `LRESULT` is a typedef that, at the time of this writing, is another name for a long integer. The `CALLBACK` calling convention is used with those functions that will be called by Windows. In Windows terminology, any function that is called by Windows is referred to as a *callback function*.

In addition to receiving the messages sent by Windows, the window function must initiate any actions indicated by a message. Typically, a window function's body consists of a `switch` statement that links a specific response to each message that the program will respond to. Your program need not respond to every message that Windows sends. For messages that your program doesn't care about, you can let Windows provide default processing. Since there are hundreds of different messages that Windows can generate, it is common for most messages simply to be processed by Windows and not by your program.

All messages are 32-bit integer values. Furthermore, all messages are linked with any additional information that the messages require.

### WINDOW CLASSES

When your Windows program first begins execution, it will need to define and register a *window class*. When you register a window class, you are telling Windows about the form and function of the window. However, registering the window class does not cause a window to come into existence. To actually create a window requires additional steps.

### THE MESSAGE LOOP

As explained earlier, Windows communicates with your program by sending it messages. All Windows applications must establish a *message loop* inside the `WinMain()` function. This loop reads any pending message from the application's message queue and dispatches that message back to Windows, which then calls your program's window function with that message as a parameter. This may seem to be an overly complex way of passing messages, but it is, nevertheless, the way all Windows programs must function. (Part of the reason for this scheme is to return control to Windows so that the scheduler can allocate CPU time as it sees fit rather than waiting for your application's time slice to end.)

### WINDOWS DATA TYPES

As you will soon see, Windows programs do not make extensive use of standard C data types, such as **int** or **char \***. Instead, all data types used by Windows have been typedefed within the WINDOWS.H file and/or its related files. The WINDOWS.H file is supplied by your Windows-compatible compiler and must be included in all Windows programs. Some of the most common types are `HANDLE`, `HWND`, `BYTE`, `WORD`, `DWORD`, `UINT`, `LONG`, `BOOL`, `LPSTR`, and `LPCSTR`. `HANDLE` is a 32-bit integer that is used as a handle. As you will see, there are a number of handle types, but they are all the same size as `HANDLE`. A handle is simply a value that identifies some resource. Also, all handle types begin with an H. For example, `HWND` is a 32-bit integer used as a window handle. `BYTE` is an 8-bit unsigned character. `WORD` is a 16-bit unsigned short integer. `DWORD` is an unsigned long integer. `UINT` is a 32-bit unsigned integer. `LONG` is another name for **long**. `BOOL` is an integer; this type is used to indicate values that are either true or false. `LPSTR` is a pointer to a string, and `LPCSTR` is a const pointer to a string.

In addition to the basic types described above, Windows defines several structures. The two that are needed by the skeleton program are `MSG` and `WNDCLASSEX`. The `MSG` structure holds a Windows message, and `WNDCLASSEX` is a structure that defines a window class. These structures will be discussed later in this appendix.

---

## A WINDOWS SKELETON

Now that the necessary background information has been covered, it's time to develop a minimal Windows application. As stated, all Windows programs have certain things in common. This section develops a Windows skeleton that provides these necessary features. In the world of Windows programming, application skeletons are commonly used because there is a substantial "price of admission" when creating a Windows program. For instance, the short example programs shown in this book are designed for a command-line interface (such as DOS), in which a minimal program is about 5 lines long. A minimal Windows program, however, is approximately 50 lines long.

A minimal Windows program contains two functions: `WinMain()` and the window function. The `WinMain()` function must perform the following general steps:

1. Define a window class.
2. Register that class with Windows.
3. Create a window of that class.
4. Display the window.
5. Begin running the message loop.

The window function must respond to all relevant messages. Since the skeleton program does nothing but display its window, the only message that it must respond to is the one telling the application that the user has terminated the program.

Before considering the specifics, examine the following program, which is a minimal Windows skeleton. It creates a standard window that includes a title. The window also contains the system menu and is, therefore, capable of being minimized, maximized, moved, resized, and closed. It also contains the standard minimize, maximize, and close boxes.

```c
/* A minimal 32-bit Windows skeleton. */

#include <windows.h>

LRESULT CALLBACK WindowFunc(HWND, UINT, WPARAM, LPARAM);

char szWinName[] = "MyWin"; /* name of window class */

int WINAPI WinMain(HINSTANCE hThisInst, HINSTANCE hPrevInst,
                   LPSTR lpszArgs, int nWinMode)
{
    HWND hwnd;
    MSG msg;
    WNDCLASSEX wcl;

    /* Define a window class. */
    wcl.cbSize = sizeof(WNDCLASSEX); /* size of WNDCLASSEX */

    wcl.hInstance = hThisInst; /* handle to this instance */
    wcl.lpszClassName = szWinName; /* window class name */
    wcl.lpfnWndProc = WindowFunc;  /* window function */
    wcl.style = 0;                 /* default style */

    wcl.hIcon = LoadIcon(NULL, IDI_APPLICATION); /* icon style */
    wcl.hIconSm = LoadIcon(NULL, IDI_WINLOGO);   /* small icon style */

    wcl.hCursor = LoadCursor(NULL, IDC_ARROW);   /* cursor style */
    wcl.lpszMenuName = NULL;                     /* no menu */

    wcl.cbClsExtra = 0; /* no extra */
    wcl.cbWndExtra = 0; /* information needed */

    /* Make the window background white. */
    wcl.hbrBackground = (HBRUSH) GetStockObject(WHITE_BRUSH);

    /* Register the window class. */
    if(!RegisterClassEx(&wcl)) return 0;

    /* Now that a window class has been registered, a window
       can be created. */
    hwnd = CreateWindow(
        szWinName,                 /* name of window class */
        "Windows Skeleton",        /* title */
        WS_OVERLAPPEDWINDOW,       /* window style - normal */
        CW_USEDEFAULT,             /* X coordinate - let Windows decide */
        CW_USEDEFAULT,             /* Y coordinate - let Windows decide */
        CW_USEDEFAULT,             /* width - let Windows decide */
        CW_USEDEFAULT,             /* height - let Windows decide */
        HWND_DESKTOP,              /* no parent window */
        NULL,                      /* no menu */
        hThisInst,                 /* handle of this instance of the program */
        NULL                       /* no additional arguments */
    );

    /* Display the window. */
    ShowWindow(hwnd, nWinMode);
    UpdateWindow(hwnd);

    /* Create the message loop. */
    while(GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg); /* translate keyboard messages */
        DispatchMessage(&msg);  /* return control to Windows */
    }
    return msg.wParam;
}

/* This function is called by Windows and is passed
   messages from the message queue.
*/
LRESULT CALLBACK WindowFunc(HWND hwnd, UINT message,
                            WPARAM wParam, LPARAM lParam)
{
    switch(message) {
        case WM_DESTROY: /* terminate the program */
            PostQuitMessage(0);
            break;
        default:
            /* Let Windows process any messages not specified in
               the preceding switch statement. */
            return DefWindowProc(hwnd, message, wParam, lParam);
    }
    return 0;
}
```

The window produced by this program is shown in Figure C-2. Now let's go through this program step by step.

First, all Windows programs must include the header file WINDOWS.H. As stated, this file (along with its support files) contains the API function prototypes and various types, macros, and definitions used by Windows. For example, the data types `HWND` and `WNDCLASSEX` are defined in WINDOWS.H.

The window function used by the program is called `WindowFunc()`. It is declared as a callback function, because this is the function that Windows calls to communicate with the program.

Program execution begins with `WinMain()`, which is passed four parameters. `hThisInst` and `hPrevInst` are handles. `hThisInst` refers to the current instance of the program. Remember, Windows is a multitasking system, so more than one instance of your program may be running at the same time. `hPrevInst` will always be `NULL`. (In Windows 3.1 programs, `hPrevInst` would be non-zero if there were other instances of the program currently executing, but this doesn't apply to 32-bit versions of Windows.) The `lpszArgs` parameter is a pointer to a string that holds any command line arguments specified when the application was begun. The `nWinMode` parameter contains a value that determines how the window will be displayed when your program begins execution.

Inside the function, three variables are created. The `hwnd` variable will hold the handle to the program's window. The `msg` structure variable will hold window messages, and the `wcl` structure variable will be used to define the window class.

```
FIGURE C-2
The window produced by the Windows skeleton

+----------------------------------------------------+
| Windows Skeleton                         [_][^][X] |
+----------------------------------------------------+
|                                                    |
|                                                    |
|                                                    |
|                                                    |
|                                                    |
|                                                    |
+----------------------------------------------------+
```

### DEFINING THE WINDOW CLASS

The first two actions that `WinMain()` takes are to define a window class and then register it. A window class is defined by filling in the fields defined by the `WNDCLASSEX` structure. Its fields are shown here:

```c
UINT cbSize;          /* size of the WNDCLASSEX structure */
UINT style;           /* type of window */
WNDPROC lpfnWndProc;  /* address to window func */
int cbClsExtra;       /* extra class info */
int cbWndExtra;       /* extra window info */
HINSTANCE hInstance;  /* handle of this instance */
HICON hIcon;          /* handle of standard icon */
HICON hIconSm;        /* handle of small icon */
HCURSOR hCursor;      /* handle of mouse cursor */
HBRUSH hbrBackground; /* background color */
LPCSTR lpszMenuName;  /* name of main menu */
LPCSTR lpszClassName; /* name of window class */
```

As you can see by looking at the program, `cbSize` is assigned the size of the `WNDCLASSEX` structure. The `hInstance` field is assigned the current instance handle as specified by `hThisInst`. The name of the window class is pointed to by `lpszClassName`, which points to the string "MyWin" in this case. The address of the window function is assigned to `lpfnWndProc`. No default style is specified, and no extra information is needed.

All Windows applications need to define a default shape for the mouse cursor and for the application's icons. An application can define its own custom version of these resources or it may use one of the built-in styles, as the skeleton does. In either case, handles to these resources must be assigned to the appropriate members of the `WNDCLASSEX` structure. To see how this is done, let's begin with icons.

A modern Windows application has at least two icons associated with it: one standard size and one small. The small icon is used when the application is minimized and it is also the icon that is used for the system menu. The standard icon is displayed when you move or copy an application to the desktop. Typically, standard icons are 32 by 32 bitmaps and small icons are 16 by 16 bitmaps. The style of each icon is loaded by the API function `LoadIcon()`, whose prototype is shown here:

```c
HICON LoadIcon(HINSTANCE hInst, LPCSTR lpszName);
```

This function returns a handle to an icon. Here, `hInst` specifies the handle of the module that contains the icon and the icon's name is specified in `lpszName`. However, to use one of the built-in icons, you must use `NULL` for the first parameter and specify one of the following macros for the second:

| Icon Macro | Shape |
| :--- | :--- |
| `IDI_APPLICATION` | Default icon |
| `IDI_ASTERISK` | Information icon |
| `IDI_EXCLAMATION` | Exclamation point icon |
| `IDI_HAND` | Stop sign |
| `IDI_QUESTION` | Question mark icon |
| `IDI_WINLOGO` | Windows logo |

In the skeleton, `IDI_APPLICATION` is used for the standard icon and `IDI_WINLOGO` is used for the small icon.

To load the mouse cursor, use the `LoadCursor()` API function. This function has the following prototype:

```c
HCURSOR LoadCursor(HINSTANCE hInst, LPCSTR lpszName);
```

This function returns a handle to a cursor resource. Here, `hInst` specifies the handle of the module that contains the mouse cursor, and the name of the mouse cursor is specified in `lpszName`. However, to use one of the built-in cursors, you must use `NULL` for the first parameter and specify one of the built-in cursors, using its macro, for the second parameter. Some of the most common built-in cursors are shown here:

| Cursor Macro | Shape |
| :--- | :--- |
| `IDC_ARROW` | Default arrow pointer |
| `IDC_CROSS` | Cross hairs |
| `IDC_IBEAM` | Vertical I-beam |
| `IDC_WAIT` | Hourglass |

The background color of the window created by the skeleton is specified as white, and a handle to this brush is obtained using the API function `GetStockObject()`. A brush is a resource that paints the screen using a predetermined size, color, and pattern. The function `GetStockObject()` is used to obtain a handle to a number of standard display objects, including brushes, pens (which draw lines), and character fonts. It has this prototype:

```c
HGDIOBJ GetStockObject(int object);
```

The function returns a handle to the object specified by *object*. (The type `HGDIOBJ` is a GDI handle.) Here are some of the built-in brushes available to your program:

| Brush Macro | Background Type |
| :--- | :--- |
| `BLACK_BRUSH` | Black |
| `DKGRAY_BRUSH` | Dark gray |
| `HOLLOW_BRUSH` | See-through window |
| `LTGRAY_BRUSH` | Light gray |
| `WHITE_BRUSH` | White |

You can use these macros as parameters to `GetStockObject()` to obtain a brush.

Once the window class has been fully specified, it is registered with Windows using the API function `RegisterClassEx()`, whose prototype is shown here:

```c
ATOM RegisterClassEx(CONST WNDCLASSEX *lpWClass);
```

The function returns a value that identifies the window class. `ATOM` is a typedef that means `WORD`. Each window class is given a unique value. `lpWClass` must be the address of the `WNDCLASSEX` structure.

### CREATING A WINDOW

Once a window class has been defined and registered, your application can actually create a window of that class using the API function `CreateWindow()`, whose prototype is shown here:

```c
HWND CreateWindow(
    LPCSTR lpClassName,     /* name of window class */
    LPCSTR lpWinName,       /* title of window */
    DWORD dwStyle,          /* type of window */
    int X, int Y,           /* upper-left coordinates */
    int Width, int Height,  /* dimensions of window */
    HWND hParent,           /* handle of parent window */
    HMENU hMenu,            /* handle of main menu */
    HINSTANCE hThisInst,    /* handle of creator */
    LPVOID lpszAdditional   /* pointer to additional info */
);
```

As you can see by looking at the skeleton program, many of the parameters to `CreateWindow()` may be defaulted or specified as `NULL`. In fact, most often the *X*, *Y*, *Width*, and *Height* parameters will simply use the macro `CW_USEDEFAULT`, which tells Windows to select an appropriate size and location for the window. If the window has no parent, which is the case in the skeleton, then *hParent* must be specified as `HWND_DESKTOP`. (You may also use `NULL` for this parameter.) If the window does not contain a main menu, then *hMenu* must be `NULL`. Also, if no additional information is required, as is most often the case, then *lpszAdditional* is `NULL`. (The type `LPVOID` is typedefed as **void \***. Historically, `LPVOID` stands for "long pointer to void.")

The remaining four parameters must be set explicitly by your program. First, `lpszClassName` must point to the name of the window class. (This is the name you gave it when it was registered.) The title of the window is a string pointed to by `lpszWinName`. This can be a null string, but usually a window will be given a title. The style (or type) of window actually created is determined by the value of `dwStyle`. The macro `WS_OVERLAPPEDWINDOW` specifies a standard window that has a system menu, a border, and minimize, maximize, and close boxes. While this style of window is the most common, you can construct one to your own specifications. To accomplish this, simply OR together the various style macros that you want. Some other common styles are shown here:

| Style Macros | Window Feature |
| :--- | :--- |
| `WS_OVERLAPPED` | Overlapped window with border |
| `WS_MAXIMIZEBOX` | Maximize box |
| `WS_MINIMIZEBOX` | Minimize box |
| `WS_SYSMENU` | System menu |
| `WS_HSCROLL` | Horizontal scroll bar |
| `WS_VSCROLL` | Vertical scroll bar |

The `hThisInst` parameter must contain the current instance handle of the application.

The `CreateWindow()` function returns the handle of the window it creates or `NULL` if the window cannot be created.

Once the window has been created, it still is not displayed on the screen. To cause the window to be displayed, call the `ShowWindow()` API function. This function has the following prototype:

```c
BOOL ShowWindow(HWND hwnd, int nHow);
```

The handle of the window to display is specified in `hwnd`. The display mode is specified in `nHow`. The first time the window is displayed, you will want to pass `WinMain()`'s `nWinMode` as the `nHow` parameter. Remember, the value of `nWinMode` determines how the window will be displayed when the program begins execution. Subsequent calls can display (or remove) the window as necessary. Some common values for `nHow` are shown here:

| Display Macros | Effect |
| :--- | :--- |
| `SW_HIDE` | Removes the window |
| `SW_MINIMIZE` | Minimizes the window into an icon |
| `SW_MAXIMIZE` | Maximizes the window |
| `SW_RESTORE` | Returns a window to normal size |

The `ShowWindow()` function returns the previous display status of the window. If the window was displayed, then nonzero is returned. If the window was not displayed, zero is returned.

Although not technically necessary for the skeleton, a call to `UpdateWindow()` is included because it is needed by virtually every Windows application that you will create. It essentially tells Windows to send a message to your application that the main window needs to be updated.

### THE MESSAGE LOOP

The final part of the skeletal `WinMain()` is the message loop. The message loop is a part of all Windows applications. Its purpose is to receive and process messages sent by Windows. When an application is running, it is continually being sent messages. These messages are stored in the application's message queue until they can be read and processed. Each time your application is ready to read another message, it must call the API function `GetMessage()`, which has this prototype:

```c
BOOL GetMessage(LPMSG msg, HWND hwnd, UINT min, UINT max);
```

The message will be received by the structure pointed to by *msg*. All Windows messages are contained in a structure of type `MSG`, shown here:

```c
/* Message structure */
typedef struct tagMSG {
    HWND hwnd;       /* window that message is for */
    UINT message;    /* message */
    WPARAM wParam;   /* more message-dependent info */
    LPARAM lParam;   /* more message-dependent info */
    DWORD time;      /* time message posted */
    POINT pt;        /* X,Y location of mouse */
} MSG;
```

In `MSG`, the handle of the window for which the message is intended is contained in `hwnd`. All Win32 messages are 32-bit integers, and the message is contained in `message`. Additional information relating to each message is passed in `wParam` and `lParam`. The type `WPARAM` is a typedef for `UINT`, and `LPARAM` is a typedef for `LONG`.

The time the message was sent (posted) is specified in milliseconds in the `time` field.

The `pt` member will contain the coordinates of the mouse when the message was sent. The coordinates are held in a `POINT` structure, which is defined like this:

```c
typedef struct tagPOINT {
    LONG x, y;
} POINT;
```

If there are no messages in the application's message queue, then a call to `GetMessage()` will pass control back to Windows.

The `hwnd` parameter to `GetMessage()` specifies the window for which messages will be obtained. It is possible, and even likely, that an application will contain several windows, but you only want to receive messages for a specific window. If you want to receive all messages directed at your application, this parameter must be `NULL`.

The remaining two parameters to `GetMessage()` specify a range of messages that will be received. Generally, you want your application to receive all messages. To accomplish this, specify both *min* and *max* as 0, as the skeleton does.

`GetMessage()` returns zero when the user terminates the program, causing the message loop to terminate. Otherwise it returns nonzero.

Inside the message loop, two functions are called. The first is the API function `TranslateMessage()`. This function translates raw keyboard input into character messages. Although it is not necessary for all applications, most applications call `TranslateMessage()` because it is needed to allow full integration of the keyboard into your application program.

Once the message has been read and translated, it is dispatched back to Windows using the `DispatchMessage()` API function. Windows then holds this message until it can be passed to the program's window function.

Once the message loop terminates, the `WinMain()` function ends by returning the value of `msg.wParam` to Windows. This value contains the return code generated when your program terminates.

---

## THE WINDOW FUNCTION

The second function in the application skeleton is its window function. In this case, the function is called `WindowFunc()`, but it could have any name you like. The window function is passed the first four members of the `MSG` structure as parameters. For the skeleton, the only parameter used is the message itself. However, actual applications will use the other parameters to this function.

The skeleton's window function responds to only one message explicitly: `WM_DESTROY`. This message is sent when the user terminates the program. When this message is received, your program must execute a call to the API function `PostQuitMessage()`. The argument to this function is an exit code that is returned in `msg.wParam` inside `WinMain()`. Calling `PostQuitMessage()` causes a `WM_QUIT` message to be sent to your application, which causes `GetMessage()` to return false, thus stopping your program.

Any other messages received by `WindowFunc()` are passed to Windows, via a call to `DefWindowProc()`, for default processing. This step is necessary because all messages must be dealt with in one fashion or another.

---

## A SHORT WORD ABOUT DEFINITION FILES

You may have heard or read about definition files. For 16-bit versions of Windows, such as 3.1, programs need to have a definition file associated with them. A definition file is simply a text file that specifies certain information and settings required by a Windows 3.1 program. However, because of the 32-bit architecture (and other improvements) of modern versions of Windows, definition files are no longer needed.

---

## NAMING CONVENTIONS

Before concluding this appendix, a short comment on the naming of functions and variables needs to be made. Several of the variable and parameter names in the skeleton program and its description probably seemed rather unusual. This is because they follow a set of naming conventions that was invented for Windows programming by Microsoft. For functions, the name consists of a verb followed by a noun. The first character of the verb and noun is capitalized.

For variable names, Microsoft chose to use a rather complex system of embedding the data type into the name. To accomplish this, a lowercase type prefix is added to the start of the variable's name. The name itself begins with a capital letter. The type prefixes are shown in Table C-1. Frankly, the use of type prefixes is controversial and is not universally supported. Many Windows programmers use this method, but many do not. You are free to use any naming convention you like.

| Prefix | Data Type |
| :--- | :--- |
| b | Boolean (one byte) |
| c | Character (one byte) |
| dw | Long unsigned integer |
| f | 16-bit bit-field (flags) |
| fn | Function |
| h | Handle |
| l | Long integer |
| lp | Long pointer |
| n | Short integer |
| p | Pointer |
| pt | Long integer holding screen coordinates |
| w | Short unsigned integer |
| sz | Pointer to null-terminated string |
| lpsz | Long pointer to null-terminated string |
| rgb | Long integer holding RGB color values |

*Table C-1 Variable Type Prefix Characters*

---

## TO LEARN MORE

The foregoing overview of Windows programming just scratches the surface. In order to write Windows programs that are useful, you must learn much more about Windows programming. To learn more about Windows 95 programs you will want to read the following books:

- *Schildt's Windows 95 Programming in C and C++*
- *Schildt's Advanced Windows 95 Programming in C and C++*

To learn more about Windows NT programming, you will find

- *Windows NT 4 Programming From the Ground Up*

especially useful. These books are written by Herbert Schildt and published by Osborne/McGraw-Hill.
