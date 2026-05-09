---
date: 2026-05-08
tags:
  - github
  - git
---
## Error Due to Large File 

>[!info] GitHub Can't handle large file [100Mb or 50Mb] so if you add and commit large file , You will be unable to push the file 
>The Timeline of problem 
>git tried added a snapshot of the timeline you added 
>when trying to push github saw the large file in the snapshot and started to decline the timeline or commit 
>So need to to reset the changes so that git takes a new snapshot without the large files 

`Error Message`

```bash
remote: error: Trace: 24b85ffee632ff2177858fa6f4b6c20cd0bfddf9199fe6c7fc8824338ed8a362
remote: error: See https://gh.io/lfs for more information.s file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/Kazi-Tanvir/Obsidian-Notes.git
error: failed to push some refs to 'https://github.com/Kazi-Tanvir/Obsidian-Notes.git'
```

`Fix 1`

```bash
git reset HEAD~3
```
**What It does :** It Rewinds ~N number of commits 
>[!abstract] not recommended 

`Fix 2`

```bash
git reset origin/main
```
**What it does :** It tells Git, "Forget trying to count backward by 3 or 4 steps. Just completely erase my local history timeline and make it perfectly match GitHub's timeline."

>[!abstract] recommended
