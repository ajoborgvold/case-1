# Workflow

## Open the GitHub repo locally
1. Go to: https://github.com/ajoborgvold/case1-rasmus-ajo
1. Click the green `Code` button and copy the URL.
1. In the terminal in VS Code, write the command:
```
git clone your-copied-url
```

## Working with branches

Always work on a branch! Don't make any changes directly to the `main` branch. This allows us to work simultaniously on different branches without breaking each others code.

### Create a new branch

In the terminal, you write:
```
git switch -c new-branch-name
```
 This will create the new branch and switch to it at the same time. Choose a branch name that describes the task you're currently working on. Whitespace in branch names is not allowed; use dash `-` or underscore `_` instead.

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

An example:
```
git add workflow.md
git commit -m "edit workflow.md
```

## Merge branches

In order to merge your branch with the `main` branch, you have to be on the `main` branch itself.

### Switch to main

Switch to the `main` branch using the command:
```
git switch main
```

### Merge your branch into `main`

Merge the branch you've been working on using the command:
```
git merge your-branch-name
```

NB: If there are no merge conflicts, you're now done. If there are conflicts, you need to handle those.

## Handle merge conflicts

A merge conflict means that your new code cannot be merged with the existing code on the `main` branch without you making decisions about what code to keep.

- Follow the instructions in VS Code to handle the merge conflict.
- When all conflicts are resolved, save and commit the changes.

## Push new code
Check the current status of your local work using the command: `git status`. This will show you all changes made since the code was last pushed to the repo. To push the changes that you have added and commited, use the command:
```
git push
```

## Delete your branch
When your banch is correctly merged into `main` and you've pushed the code to the repo, you should delete the branch. Before doing so, make sure that you're not on the branch that you want to delete. To delete the branch, use the command:
```
(git switch main)
git branch -d your-branch-name
```
You can that start over from the beginning and create a new branch for any new tasks.