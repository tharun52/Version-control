# **Undoing Changes and Reverting Commits in Git**

## **Objective**

This document demonstrates how to undo changes, revert commits, and reset commits using Git with an HTML file.

----------

## **1. Initial Setup**

-   Created `index.html` with the following content:
    
    ```html
    <!DOCTYPE html>
    <html>
    <body>
        <h4>First content</h4>
    </body>
    </html>
    
    ```
    
-   Committed the file:
    
    ```bash
    git add index.html
    git commit -m "Initial commit: Add index.html"
    
    ```
    

----------

## **2. Undoing Changes Before Staging (`git restore`)**

-   Added an **unwanted paragraph** to `index.html`:
    
    ```html
    <p>Unwanted paragraph</p>
    
    ```
    
-   Checked the changes:
    
    ```bash
    git status
    
    ```
    
    **Output:**
    
    ```
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   index.html
    
    ```
    
-   Restored the file to the last committed state:
    
    ```bash
    git restore index.html  # OR git checkout -- index.html
    
    ```
    
-   Checked status again:
    
    ```bash
    git status
    
    ```
    
    **Output:**
    
    ```
    On branch main
    nothing to commit, working tree clean
    
    ```
    

----------

## **3. Undoing Changes After Staging (`git restore --staged`)**

-   Added changes to the staging area:
    
    ```bash
    git add index.html
    
    ```
    
-   Checked status:
    
    ```bash
    git status
    
    ```
    
    **Output:**
    
    ```
    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            modified:   index.html
    
    ```
    
-   Used `git restore --staged` to unstage changes:
    
    ```bash
    git restore --staged index.html
    
    ```
    
-   Checked status again:
    
    ```bash
    git status
    
    ```
    
    **Output:**
    
    ```
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git restore <file>..." to discard changes in working directory)
            modified:   index.html
    
    ```
    

----------

## **4. Reverting a Commit (`git revert`)**

-   Added and committed a **footer**:
    
    ```html
    <footer>
        Created footer
    </footer>
    
    ```
    
    ```bash
    git commit -am "Created footer"
    
    ```
    
-   Added and committed a **navbar**:
    
    ```html
    <nav>Navbar</nav>
    
    ```
    
    ```bash
    git commit -am "Created navbar"
    
    ```
    
-   Checked commit history:
    
    ```bash
    git log --oneline
    
    ```
    
    **Output:**
    
    ```
    0010195 (HEAD -> main) Created navbar
    dc0f49a Created footer
    3d24d44 Added wanted paragraph
    
    ```
    
-   Reverted the last commit (`HEAD~1`), removing the navbar:
    
    ```bash
    git revert HEAD~1
    
    ```
    
-   **New commit log after revert:**
    
    ```bash
    git log --oneline
    
    ```
    
    **Output:**
    
    ```
    cef79dc (HEAD -> main) Revert "Created footer"
    0010195 Created navbar
    dc0f49a Created footer
    3d24d44 Added wanted paragraph
    
    ```
    
-   **Effect of `git revert HEAD~1`**:
    -   Instead of deleting the last commit, it created a **new commit** that reversed the changes.

----------

## **5. Resetting to a Previous Commit (`git reset --hard`)**

-   Reset to an earlier commit:
    
    ```bash
    git reset --hard HEAD~1
    
    ```
    
-   Checked commit history:
    
    ```bash
    git log --oneline
    
    ```
    
    **Output:**
    
    ```
    cef79dc (HEAD -> main) Revert "Created footer"
    3d24d44 Added wanted paragraph
    
    ```
    
-   **Effect of `git reset --hard HEAD~1`**:
    -   This **completely removed** the last commit from the history.
    -   The commit that added the navbar is gone.

----------