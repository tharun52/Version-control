# README: Using Git Pre-Commit Hook to Block TODO Comments

## Overview

This project demonstrates how to use a Git **pre-commit hook** to enforce coding standards by preventing commits that contain `TODO` comments.

## Steps to Set Up the Pre-Commit Hook

### 1. Enable the Pre-Commit Hook

Git provides sample hooks in the `.git/hooks/` directory. To enable the pre-commit hook:

1.  Navigate to the `.git/hooks/` directory in your repository.
2.  Rename `pre-commit.sample` to `pre-commit`:
    ```sh
    mv .git/hooks/pre-commit.sample .git/hooks/pre-commit
    ```
### 2. Modify the Pre-Commit Hook

Edit the `pre-commit` file and add the following script:

```sh
#!/bin/sh

# Redirect output to stderr.
exec 1>&2

# Check if there are any "TODO" comments in staged files
if git diff --cached --name-only | xargs grep -n "TODO"; then
  echo "ERROR: Commit blocked! Remove TODO comments before committing."
  exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached HEAD --

```


## Testing the Hook

### 1. Create a Python File with a `TODO` Comment

```python
def hello():
    #TODO
    pass

if __name__ == "__main__":
    hello()

```

### 2. Try Committing the File

```sh
git add .
git commit -m "created python file"

```

#### Expected Output:

```
2:    #TODO
ERROR: Commit blocked! Remove TODO comments before committing.

```

The commit is blocked because the file contains a `TODO` comment.

### 3. Fix the Code and Commit Again

Modify the file to remove `TODO`:

```python
def hello():
    print("hello")
    pass

if __name__ == "__main__":
    hello()

```

Then, retry the commit:

```sh
git add .
git commit -m "created python file"

```

#### Output:

```
[master 58646f7] created python file
 1 file changed, 6 insertions(+), 1 deletion(-)

```

Now the commit is successful.