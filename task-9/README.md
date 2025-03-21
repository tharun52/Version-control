# **Task 9: Working with Remote Repositories and Collaboration**

## **Objective**

Simulate a collaborative workflow with remote repositories using Git.

## **Steps to Follow**

### **1. Initialize a Local Repository**

```sh
git init

```

Create an `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<body>
    Welcome
</body>
</html>

```

Add and commit the file:

```sh
git add .
git commit -m "added index.html"

```

### **2. Push to a Remote Repository**

Create a new repository on GitHub and link it to the local repository:

```sh
git remote add origin https://github.com/tharun52/Version-control.git
git push -u origin main

```

### **3. Create a Feature Branch (`title-branch`)**

```sh
git checkout -b title-branch

```

Modify `index.html` by adding a `<title>` tag:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>task 9 title</title>
</head>
<body>
    Welcome
</body>
</html>

```

Stage and commit the changes:

```sh
git add .
git commit -m "added head"

```

Push the feature branch to the remote repository:

```sh
git push origin title-branch

```

### **4. Open a Pull Request**

Go to GitHub and open a Pull Request (PR) for `title-branch`.

### **5. Merge the Feature Branch into `main`**

Once reviewed and approved, merge the PR on GitHub.

### **6. Pull the Latest Changes Locally**

```sh
git checkout main
git pull origin main

```
