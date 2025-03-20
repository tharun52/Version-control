# **Git Merge Conflict Example**

## **Overview**

This project demonstrates how to create, simulate, and resolve a merge conflict in Git using an `index.html` file.

## **Initial State**

The `index.html` file before branch creation:

```html
<!DOCTYPE html>
<html>
<body>
    <p>This is the content before branch creation</p>
</body>
</html>

```

## **Steps to Simulate and Resolve the Merge Conflict**

### **1. Create a New Branch (`new-branch`)**

```bash
git checkout -b new-branch

```

Output:

```
Switched to a new branch 'new-branch'

```

### **2. Modify `index.html` in `new-branch`**

After making changes, `index.html` looks like this:

```html
<!DOCTYPE html>
<html>
<body>
    <p>This is the content in the new-branch</p>
</body>
</html>

```

### **3. Commit the Changes in `new-branch`**

```bash
git add .
git commit -m "added changes to index in new-branch"

```

Output:

```
[new-branch 1f1e09f] added changes to index in new-branch
 1 file changed, 1 insertion(+), 1 deletion(-)

```

### **4. Switch to `main` Branch**

```bash
git checkout main

```

Output:

```
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

```

### **5. Modify `index.html` Again in `main` Branch**

After making changes, `index.html` now looks like:

```html
<!DOCTYPE html>
<html>
<body>
    <p>This is the content  changed again in main</p>
</body>
</html>

```

### **6. Commit the Changes in `main`**

```bash
git add .
git commit -m "changed content in main branch for conflict"

```

Output:

```
[main 5418516] changed content in main branch for conflict
 1 file changed, 1 insertion(+), 1 deletion(-)

```

### **7. Check Differences Between `main` and `new-branch`**

```bash
git diff main..new-branch

```

Output:

```diff
diff --git a/task-4/index.html b/task-4/index.html
index 9758681..5f27726 100644
--- a/task-4/index.html
+++ b/task-4/index.html
@@ -1,6 +1,6 @@
 <!DOCTYPE html>
 <html>
 <body>
-    <p>This is the content  changed again in main</p>
+    <p>This is the content in the new-branch</p>
 </body>
 </html>

```

### **8. Merge `new-branch` into `main`**

```bash
git merge new-branch

```

Output:

```
Auto-merging task-4/index.html
CONFLICT (content): Merge conflict in task-4/index.html
Automatic merge failed; fix conflicts and then commit the result.

```

### **9. Resolve the Conflict**

At this point, `index.html` contains conflict markers:

```html
<!DOCTYPE html>
<html>
<body>
<<<<<<< HEAD
    <p>This is the content  changed again in main</p>
=======
    <p>This is the content in the new-branch</p>
>>>>>>> new-branch
</body>
</html>

```

Manually resolve the conflict by choosing the final version:

```html
<!DOCTYPE html>
<html>
<body>
    <p>This is the content in the new-branch</p>
</body>
</html>

```

### **10. Mark the Conflict as Resolved**

```bash
git add .
git commit -m "resolved merge conflict"

```

Output:

```
[main aacd5ef] resolved merge conflict

```

## **Final State After Merge**

The `index.html` file looks like:

```html
<!DOCTYPE html>
<html>
<body>
    <p>This is the content in the new-branch</p>
</body>
</html>

```

----------

## **Conclusion**

This exercise demonstrates how Git handles merge conflicts when the same file is modified in different branches. The conflict was resolved by manually editing the file and committing the changes.
