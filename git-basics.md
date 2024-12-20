# Git and GitHub Basics
Git is a version control software, and GitHub is a service that hosts Git repositories online, enabling collaboration and version tracking.

## Version Control System (VCS)
A VCS tracks changes to files, allowing you to manage and control the versions of your code, and revert changes if needed.
---

## Common Git Commands

- **Check Git Version**
  ```bash
  git --version
  ```
  Displays the current version of Git installed on your system.

- **Show Current Directory**
  ```bash
  pwd
  ```
  Prints the current working directory.

- **List Directory Contents**
  ```bash
  ls
  ```
  Lists the files and directories in the current directory.

---

## Configuring Git

- **Set Global User Email and Username**
  ```bash
  git config --global user.email "Vasu.sahu.8080@gmail.com"
  git config --global user.name "Vasu10134"
  ```

- **View Git Configuration**
  ```bash
  git config --list
  ```
  Displays the current Git configuration settings, such as user email and username.

---

## Usual Git Workflow

1. **Write Code**: Create or modify files.
2. **Add Files**: Stage the files you want to commit.
3. **Commit Changes**: Record the changes to the repository.

---

### Git Commands for Workflow

- **Track Repository Status**
  ```bash
  git status
  ```
  Displays the current status of the repository, showing which files have been modified, added, or deleted.

- **Change Directory**
  ```bash
  cd <folder_path>
  ```
  Changes the current directory to the specified folder.

- **Check Current Directory**
  ```bash
  pwd
  ```
  After using `cd`, this confirms you’ve navigated to the correct folder.

- **Initialize a Git Repository**
  ```bash
  git init
  ```
  Initializes a new Git repository in your current directory, creating a `.git` folder that tracks changes.

- **Add Files to Staging Area**
  ```bash
  git add <file1> <file2> <file3>
  git add .
  ```
  The first command adds specific files, while the second adds all files in the directory to the staging area.

- **Commit Changes with a Message**
  ```bash
  git commit -m "First commit"
  ```
  Commits the changes made, with a message describing the changes.

- **View Commit History**
  ```bash
  git log
  git log --oneline
  ```
  The first command shows detailed commit history, while the second provides a more concise, one-line view.

---

## Other Important Concepts

### `.gitignore`

A `.gitignore` file tells Git which files or directories to ignore, preventing irrelevant or sensitive data (like logs, credentials, etc.) from being added to the repository.

Example `.gitignore` entries:
```
# Ignore log files
*.log

# Ignore node_modules directory
node_modules/

# Ignore system files
.DS_Store
```

---

## Additional Tips

- **Committing Changes Multiple Times**: You can commit as many times as needed. After making changes to files, simply run:
  ```bash
  git add .
  git commit -m "Describe the changes"
  ```

- **Git Log Options**: You can customize how you view your commit history.
  - `git log --oneline` shows a compact log with one commit per line.
  - `git log --graph --oneline` displays a graphical representation of the commit tree.

---
