---
date: 2026-06-17
tags:
  - termux
  - python
  - github
  - android
---
## Termux Python Setup & GitHub Integration

>[!info] The Google Play Store version of Termux is deprecated and will fail to update packages. Always download Termux from F-Droid or the official Termux GitHub Releases page. 

`Step 1: Initial Setup & Update`

```bash
pkg update && pkg upgrade -y
termux-setup-storage
```
**What It does :** Updates the package lists to the latest versions and grants Termux permission to access your phone's internal storage.

`Step 2: Install Dependencies`

```bash
pkg install python git nano -y
```

`Step 3: Clone Repository & Run`

```bash
git clone <your_repository_url>
cd <repository_folder_name>
pip install -r requirements.txt
python main.py
```

---

## Error: Invalid Requirement in requirements.txt

>[!info] The `requirements.txt` file is strictly for listing Python packages. If you add directory paths (like `/downloads`) to this file, `pip` will crash because it thinks it's a Python package name rather than a folder path.

`Error Message`

```bash
ERROR: Invalid requirement: '/downloads': Expected package name at the start of dependency specifier
    /downloads
    ^ (from line 6 of requirements.txt)
Hint: It looks like a path. File '/downloads' does not exist.
```

`Fix`

```bash
nano requirements.txt
```
**What it does :** Opens the terminal text editor. You must delete the `/downloads` line entirely, save (CTRL+O, Enter), and exit (CTRL+X). 

>[!abstract] recommended
>Use the `os` module inside your Python script to create target folders like `/downloads`, or create them manually using `mkdir downloads` in the terminal. Never put folder paths in `requirements.txt`.