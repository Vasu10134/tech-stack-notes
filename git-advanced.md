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
