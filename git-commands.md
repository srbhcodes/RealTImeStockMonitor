### **Uploading the Project to GitHub: Step-by-Step**

Here’s a complete breakdown of how we uploaded your project to GitHub, the issues faced, and the commands used:

---

#### **1. Initialize a Local Git Repository**
- **Why**: To track your project's files and versions locally with Git.
- **Command**:
  ```bash
  git init
  ```
  This creates a `.git` folder in your project directory.

---

#### **2. Add Files to Git Tracking**
- **Why**: To include all the files and folders of your project in the Git repository.
- **Command**:
  ```bash
  git add .
  ```
  The `.` adds all files and directories recursively to Git's tracking.

---

#### **3. Commit the Changes**
- **Why**: To save the current state of your project to the Git repository with a message describing the changes.
- **Command**:
  ```bash
  git commit -m "Initial commit"
  ```

---

#### **4. Link the Local Repository to GitHub**
- **Why**: To connect your local repository to the GitHub repository so that you can upload files.
- **Command**:
  ```bash
  git remote add origin https://github.com/srbhcodes/RealTimeStockMonitor.git
  ```
  This links your local repository to the remote GitHub repository.

---

#### **5. Push to GitHub**
- **Why**: To upload the committed changes to the remote repository on GitHub.
- **Command**:
  ```bash
  git push -u origin main
  ```

---

### **Issues Faced and How We Resolved Them**

---

#### **Issue 1: Password Authentication Deprecated**
- **Error**:
  ```
  remote: Support for password authentication was removed on August 13, 2021.
  ```
- **Reason**: GitHub no longer allows password authentication for pushing changes. You need to use a Personal Access Token (PAT) instead.

- **Solution**:
  1. Generated a PAT from GitHub.
  2. Used the token in place of the password during the `git push` operation.

---

#### **Issue 2: Remote Contains Work**
- **Error**:
  ```
  Updates were rejected because the remote contains work that you do not have locally.
  ```
- **Reason**: The GitHub repository already had some initial content (e.g., `README.md`), and the local repository was unaware of it.

- **Solution**:
  1. Pulled changes from the remote repository with `--allow-unrelated-histories`:
     ```bash
     git pull origin main --allow-unrelated-histories
     ```
  2. Resolved merge conflicts (if any).
  3. Added resolved files and committed:
     ```bash
     git add .
     git commit -m "Resolved merge conflicts"
     ```

---

#### **Issue 3: Divergent Branches**
- **Error**:
  ```
  Need to specify how to reconcile divergent branches.
  ```
- **Reason**: Git required a strategy to reconcile local and remote changes because their histories were unrelated.

- **Solution**:
  Specified the merge strategy directly:
  ```bash
  git pull origin main --allow-unrelated-histories --no-rebase
  ```

---

#### **6. Final Push to GitHub**
- **Command**:
  ```bash
  git push -u origin main
  ```
  This successfully uploaded the merged project to GitHub.

---

### **Summary of All Commands Used**

```bash
# Initialize Git repository
git init

# Add all files to staging
git add .

# Commit files
git commit -m "Initial commit"

# Link to GitHub repository
git remote add origin https://github.com/srbhcodes/RealTimeStockMonitor.git

# Pull changes from GitHub to resolve divergence
git pull origin main --allow-unrelated-histories --no-rebase

# Resolve conflicts (if any), then add and commit
git add .
git commit -m "Resolved merge conflicts"

# Push to GitHub
git push -u origin main
```

