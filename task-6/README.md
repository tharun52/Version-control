
# **Git Stashing Example with HTML File**

## **Objective**

This exercise demonstrates how to use `git stash` to temporarily save uncommitted changes, switch branches, and merge stashed changes while resolving conflicts.

----------

## **Steps and Commands**

### **1. Initial Setup**

Create `index.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    Welcome to My Website
</body>
</html>

```

Commit the initial version:

```sh
git add index.html
git commit -m "Initial commit with index.html"

```

----------

### **2. Work on the `footer-branch`**

Create a new branch and modify `index.html`:

```sh
git checkout -b footer-branch

```

Update `index.html` to add an `<h1>` tag:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
</body>
</html>

```

Commit this change:

```sh
git add index.html
git commit -m "Added <h1> tag"

```

Add a footer to `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>

    <footer>
        footer of the page
    </footer>
</body>
</html>

```

Stash the footer changes:

```sh
git stash

```

----------

### **3. Switch to `main` and Modify HTML**

Switch back to `main`:

```sh
git checkout main

```

Modify `index.html` by adding a navigation bar:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <nav>nav bar </nav>
    Welcome to My Website
</body>
</html>

```

Stash the navigation bar changes:

```sh
git stash

```

List the stashes:

```sh
git stash list

```

Output:

```
stash@{0}: WIP on main: 8bddcb7 created index.html
stash@{1}: WIP on footer-branch: 958f5d4 added <h1>

```

----------

### **4. Apply the Footer Stash on `main` and Resolve Conflict**

Apply the `footer-branch` stash:

```sh
git stash apply stash@{1}

```

A conflict occurs in `index.html`. Resolve it to:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>

    <footer>
        footer of the page
    </footer>
</body>
</html>

```

Mark the conflict as resolved:

```sh
git add index.html
git commit -am "Conflict resolved with h1"

```

----------

### **5. Drop the Remaining Stash**

Since the navigation bar stash is no longer needed, drop it:

```sh
git stash drop stash@{0}

```

----------

## **Final Outcome**

-   The `<footer>` were successfully stashed and then added  into `main` using `git stash apply stash@{1}`.
-   The navigation bar stash was dropped as it was unnecessaryusing `git stash drop`.
-   The `index.html` now contains the version with stashed changed.
