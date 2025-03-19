# Task 2 - Using .gitignore and Tracking Files

## **Objective**
- Set up a `.gitignore` file to exclude certain files or directories.  
- Verify that ignored files are not tracked by Git.  

## **Commands Used**

### **Step 1: Create and Switch to a New Branch**
```bash
git checkout -b task-2
Step 2: Create a New Folder and Files
bash
Copy code
mkdir task-2
cd task-2
code main.py
code .env
code .gitignore
Step 3: Edit .gitignore to Ignore .env
bash
Copy code
task-2/.env
Step 4: Write Python Script (main.py)
python
Copy code
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")
Step 5: Add and Push Changes
bash
Copy code
git add .
git status
git push -u origin task-2
Step 6: Merge to Main Branch
bash
Copy code
cd ..
git checkout main
git merge task-2
Step 7: Create and Commit README.md
bash
Copy code
code readme.md
git add .
git commit -m "Add README"
git push -u origin main