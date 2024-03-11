# Workflow

## Open the GitHub repo locally

### Fork and clone repo

1. Go to: https://github.com/ajoborgvold/case1-rasmus-ajo
2. Click the `Fork` button and fork the proejct to your own GitHub account.
3. Go to your own GitHub account and find the forked repo.
4. Click the green `Code` button and copy the URL.

### Open repo and connect it to original

1. In the terminal in VS Code, write the command:
```git clone your-copied-url```
2. Add a remote to the upstream, i.e. the original repo, so that you can get the latest changes in the `main` branch:
```git remote add upstream https://github.com/ajoborgvold/case1-rasmus-ajo```

## Working with branches

Always work on a branch! Don't make any changes directly to the `main` branch. This allows us to work simultaniously on different branches without breaking each others code.

### Create a new branch

In the terminal, you write `git switch -c new-branch-name`. This will create the new branch and switch to it at the same time. Choose a branch name that describes the task you're currently working on. Whitespace in branch names is not allowed; use dash `-` or underscore `_` instead.

### Check and switch branch

- To check which branch you're on, use the command `git branch`.
- To switch between branches, use the command `git switch branch-name`.

## Add and commit changes

When you're done working on a task, you should add and commit the changes.

### Add your changes

- The command `git add .` adds all changes.
- The command `git add some-file-name` adds the specified file.

### Commit your changes

Write a commit message using the command `git commit -m your-message` describing the changes you've made.

## Merge branches

In order to merge your branch with the `main` branch, you have to be on the `main` branch.

### Switch to main

Switch to the `main` branch using the command `git switch main`

### Merge your branch into `main`

Merge the branch you've been working on using the command `git merge your-branch-name`

NB: If there are no merge conflicts, you're now done. If there are conflicts, you need to handle those.

## Handle merge conflicts

A merge conflict means that your new code cannot be merged with the existing code on the `main` branch without you making decisions about what code to keep.

- Follow the instructions in VS Code to handle the merge conflict.
- When all conflicts are resolved, save and commit the changes.

## Delete your branch

When your banch is correctly merged into `main`, delete the branch using the command `git branch -d your-branch-name`.
