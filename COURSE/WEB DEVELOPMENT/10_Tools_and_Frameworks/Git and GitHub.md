---
tags:
- git
- github
- version-control
---
# Git and GitHub

## What's the Actual Use?
Git is a version control system that tracks changes in your code, allowing you to "go back in time" if you break something. GitHub is a cloud-based platform that hosts your Git repositories, making it easy to collaborate with others and share your work.

## Real-Life Analogy
Git is like the "Undo" button in Word, but on steroids—it remembers every version of your document ever saved. GitHub is like Google Drive for your code; it's a place where you can upload your work so your teammates can see it and add their own "comments" or changes.

## Other Common Use Cases
- Working in a team where multiple people are editing the same files simultaneously.
- Trying out a new experimental feature in a "branch" without breaking the main app.
- Contributing to open-source projects by "forking" their code and suggesting changes.

## Documentation & Code
Common Git commands for a standard workflow:

```bash
# Initialize a local repository
git init

# Stage changes for a commit
git add .

# Save the changes with a message
git commit -m "Add login functionality"

# Push local changes to GitHub
git push origin main

# Get the latest changes from GitHub
git pull
```