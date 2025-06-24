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

# Git Commands and Concepts Explained

## Branches in Git
- **Definition**: A branch is a lightweight, movable pointer to a commit. It allows multiple lines of development in a repository.
- **Use Case**: Used to isolate work, for example, developing a new feature or fixing a bug, without affecting the main codebase.

---

## HEAD in Git
- **Definition**: HEAD is a pointer to the current branch reference or the last commit in the working directory.
- **Use Case**: Used to track where you are in the repository's commit history. For example, when you switch branches, HEAD points to the tip of the new branch.

---

## `git switch <branch_name>`
- **Definition**: Switches to the specified branch in your repository.
- **Use Case**: Preferred for switching between branches or creating a new branch. Safer and more intuitive than `git checkout` for branch-related tasks.

---

## `git checkout`
- **Definition**: Used to switch branches or restore files in the working directory to their state in another branch or commit.
- **Use Case**: Often used for both branch switching and file restoration, though it's now partially replaced by `git switch` and `git restore`.

---

## `git merge <branch_name>`
- **Definition**: Combines the changes from the specified branch into the current branch.
- **Use Case**: Used to integrate changes from one branch into another, such as merging a feature branch into the main branch.

---

## `git branch -m <old-branch-name> <new-branch-name>`
- **Definition**: Renames an existing branch from `<old-branch-name>` to `<new-branch-name>`.
- **Use Case**: Used to rename a branch locally.

---

## `git branch`
- **Definition**: Lists all branches in the repository and shows the current branch with an asterisk (*).
- **Use Case**: Used to view available branches or create/delete branches with additional options.

---

## `git diff`
- **Definition**: Shows the changes between the working directory and the index or between two commits.
- **Use Case**: Used to review uncommitted changes before committing or changes between commits.

---

## `git diff --staged`
- **Definition**: Shows the changes between the staging area and the last commit.
- **Use Case**: Used to view changes that are staged for the next commit.

---

## `git stash`
- **Definition**: Temporarily saves changes in the working directory that are not ready to be committed.
- **Use Case**: Used to store unfinished work when switching branches or pulling updates.

---

## `git stash list`
- **Definition**: Lists all stashed changes in the repository.
- **Use Case**: Used to view the saved stashes with their identifiers.

---

## `git tag <tag-name>`
- **Definition**: Creates a lightweight or annotated tag for a specific commit.
- **Use Case**: Used to mark a specific commit as important, such as marking a version release.

---

## `git tag`
- **Definition**: Lists all tags in the repository.
- **Use Case**: Used to view all tags, such as version numbers.

---

## Rebase in Git
- **Definition**: Rebasing moves or re-applies commits from one branch onto another.
- **Use Case**: Used to create a linear commit history by integrating changes from one branch into another without merging.

---

## Reflog in Git
- **Definition**: Reflog records updates to the tip of branches or HEAD in the repository.
- **Use Case**: Used to recover lost commits or track reference updates, even after branch deletion.
