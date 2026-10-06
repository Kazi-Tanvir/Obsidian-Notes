---
date: 2026-10-06
tags:
  - windows
  - cleanup
  - disk-space
  - cmd
  - git
  - node
  - pnpm
  - maintenance
---
## PC Cleanup — D: & C: Drive

> [!info] Your D: drive is already in decent shape (55.6 GB free). Most of the remaining weight is games, `02_CODE` (15 GB, mostly `node_modules` and `.git`), the pnpm store, and the 6.8 GB `pagefile.sys`. Open **Command Prompt as Administrator** and work through these in order.

---

## 1. D: Drive

`Empty the D: Recycle Bin` (~200 MB)

```cmd
rd /s /q D:\$RECYCLE.BIN
```
**What it does:** Deletes the recycle bin contents. Windows recreates the folder automatically.

`Clear the pnpm store` (~1.5 GB)

```cmd
pnpm store prune
```
**What it does:** Removes packages that no project uses anymore.

`Remove old node_modules folders`

```cmd
npx npkill -d D:\02_CODE
```
**What it does:** Interactive tool that finds and lists `node_modules` by size. Use arrow keys to select, press `Space` to delete. Or delete one manually:

```cmd
rd /s /q "D:\02_CODE\old-project\node_modules"
```

> [!abstract] Safe to delete — `npm install` or `pnpm install` restores them whenever you reopen a project. These folders are also the source of the 168k `.js`, 75k `.map`, and 70k `.ts` files. WizTree labels `.ts` as "video" — they're TypeScript files.

`Shrink big .git folders` (3.8 GB and 1.5 GB ones). Run inside each repo:

```cmd
git gc --aggressive --prune=now
```

`Delete build output and gitignored files in a repo`

```cmd
git clean -fdXn
git clean -fdX
```
**What it does:** The first command is a **dry run** — only lists what would be deleted. `-X` removes everything in `.gitignore`, which can include `.env` files with your keys. Always check the list before running the second command.

---

## 2. Package Manager Caches (usually on C:)

```cmd
npm cache clean --force
pip cache purge
yarn cache clean
```

---

## 3. Temp Files & Windows Junk (C:)

```cmd
del /q /f /s %TEMP%\*
del /q /f /s C:\Windows\Temp\*
rd /s /q C:\Windows\SoftwareDistribution\Download
```

> [!info] Some files will say "in use" — that's fine, just ignore those.

`Clean old Windows update leftovers` (can free several GB)

```cmd
Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase
```

> [!warning] `/ResetBase` means you **can't uninstall** currently installed updates afterwards.

`Run Disk Cleanup with all options`

```cmd
cleanmgr /sageset:1
cleanmgr /sagerun:1
```
**What it does:** The first command opens a popup — tick everything you want cleaned (except Downloads if you keep files there). The second command runs the cleanup with those saved settings.

`Turn off hibernation` (frees several GB on C:)

```cmd
powercfg /h off
```

> [!warning] Disabling hibernation removes the `hiberfil.sys` file but also **disables hibernate mode and Fast Startup**.

---

## 4. Things CMD Can't Do Well

- **`pagefile.sys` (6.8 GB on D:)** — Can't be deleted directly. Run `sysdm.cpl` → Advanced → Performance Settings → Advanced → Virtual memory. Either move it to C: or set a smaller custom size. Don't disable it completely.
- **BlueStacks (`Data.vhdx`, 7.4 GB + ~9.8 GB folder)** — Delete unused instances in BlueStacks' Multi-instance Manager, or uninstall it if unused.
- **`06_GAMES` is 25.4 GB** (Hollow Knight 7.7 GB, Silksong 7.6 GB, BlueStacks 9.8 GB) — Uninstalling finished games is the **single biggest space saver**.

---

## 5. Optional: List Files Over 1 GB

```cmd
forfiles /p D:\ /s /m *.* /c "cmd /c if @fsize GTR 1073741824 echo @path @fsize"
```

> [!info] Slow on 500k files — WizTree shows the same thing faster.

---

> [!caution] Everything with `rd /s /q` or `del` is **permanent** and skips the Recycle Bin. Double-check paths before pressing Enter.
