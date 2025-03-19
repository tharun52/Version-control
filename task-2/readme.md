# Task 2 - Using .gitignore and Tracking Files

## **Objective**
- Set up a `.gitignore` file to exclude certain files or directories.  
- Verify that ignored files are not tracked by Git.  

## **Commands Used**

```bash
git checkout -b task-2
mkdir task-2
git add task-2
cd task-2
code main.py
code .env
code .gitignore
git add .
git status
git push -u origin task-2
cd ..
git checkout main
git merge task-2
code readme.md
git add .
git status
git commit -m "add readme"
cd ..
git push -u origin main
```
