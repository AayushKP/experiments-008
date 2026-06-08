# Top 30 Git Commands for DevOps Engineers

## 1. Clone Repository

**Command**

```bash
git clone <repo-url>
```

**Implementation**

```bash
git clone https://github.com/company/ecommerce-app.git
```

**Why**
Used when joining a project or setting up code on a new server/workstation.

---

## 2. Check Repository Status

**Command**

```bash
git status
```

**Implementation**

```bash
git status
```

**Why**
Verify modified, staged, and untracked files before committing.

---

## 3. View Branches

**Command**

```bash
git branch
```

**Implementation**

```bash
git branch -a
```

**Why**
Check available local and remote branches.

---

## 4. Create Feature Branch

**Command**

```bash
git checkout -b <branch>
```

**Implementation**

```bash
git checkout -b feature/payment-api
```

**Why**
Develop a new feature without affecting the main codebase.

---

## 5. Switch Branch

**Command**

```bash
git checkout <branch>
```

**Implementation**

```bash
git checkout master
```

**Why**
Move between feature, release, hotfix, and master branches.

---

## 6. Get Latest Changes

**Command**

```bash
git pull
```

**Implementation**

```bash
git pull origin master
```

**Why**
Sync local repository before starting work.

---

## 7. Download Remote Changes Only

**Command**

```bash
git fetch
```

**Implementation**

```bash
git fetch --all
```

**Why**
Review incoming changes before merging them.

---

## 8. View File Changes

**Command**

```bash
git diff
```

**Implementation**

```bash
git diff
```

**Why**
Review code changes before committing.

---

## 9. Stage All Files

**Command**

```bash
git add .
```

**Implementation**

```bash
git add .
```

**Why**
Prepare modified files for commit.

---

## 10. Commit Changes

**Command**

```bash
git commit
```

**Implementation**

```bash
git commit -m "Add payment service"
```

**Why**
Save a logical checkpoint of completed work.

---

## 11. Push Changes

**Command**

```bash
git push
```

**Implementation**

```bash
git push origin feature/payment-api
```

**Why**
Share code with team members and CI/CD pipelines.

---

## 12. Push New Branch

**Command**

```bash
git push -u origin <branch>
```

**Implementation**

```bash
git push -u origin feature/payment-api
```

**Why**
Creates upstream tracking for future pushes.

---

## 13. Merge Branch

**Command**

```bash
git merge
```

**Implementation**

```bash
git merge feature/payment-api
```

**Why**
Integrate completed feature into master or release branch.

---

## 14. Rebase Branch

**Command**

```bash
git rebase
```

**Implementation**

```bash
git rebase master
```

**Why**
Feature branch is 2 weeks old. Rebase with latest master before creating PR to avoid conflicts.

---

## 15. Abort Rebase

**Command**

```bash
git rebase --abort
```

**Implementation**

```bash
git rebase --abort
```

**Why**
Stop rebase when conflicts become difficult to resolve.

---

## 16. Stash Changes

**Command**

```bash
git stash
```

**Implementation**

```bash
git stash
```

**Why**
Save unfinished work when production issue requires immediate attention.

---

## 17. Restore Stashed Changes

**Command**

```bash
git stash pop
```

**Implementation**

```bash
git stash pop
```

**Why**
Continue previous work after handling urgent tasks.

---

## 18. List Stashes

**Command**

```bash
git stash list
```

**Implementation**

```bash
git stash list
```

**Why**
View saved work snapshots.

---

## 19. View Commit History

**Command**

```bash
git log
```

**Implementation**

```bash
git log --oneline
```

**Why**
Check recent deployments and code history.

---

## 20. View Commit Details

**Command**

```bash
git show
```

**Implementation**

```bash
git show a1b2c3d
```

**Why**
Inspect exact changes made in a deployment.

---

## 21. Cherry Pick Commit

**Command**

```bash
git cherry-pick
```

**Implementation**

```bash
git cherry-pick a1b2c3d
```

**Why**
Move a production bug fix from master to release branch without merging everything.

---

## 22. Create Release Branch

**Command**

```bash
git checkout -b release/<version>
```

**Implementation**

```bash
git checkout -b release/v2.1.0
```

**Why**
Prepare code for QA testing and production deployment.

---

## 23. Create Hotfix Branch

**Command**

```bash
git checkout -b hotfix/<name>
```

**Implementation**

```bash
git checkout -b hotfix/login-timeout
```

**Why**
Fix critical production issue quickly.

---

## 24. Create Tag

**Command**

```bash
git tag
```

**Implementation**

```bash
git tag v2.1.0
```

**Why**
Mark production release version.

---

## 25. Push Tags

**Command**

```bash
git push origin --tags
```

**Implementation**

```bash
git push origin --tags
```

**Why**
Allow deployment tools to recognize releases.

---

## 26. Delete Local Branch

**Command**

```bash
git branch -d
```

**Implementation**

```bash
git branch -d feature/payment-api
```

**Why**
Clean up merged branches.

---

## 27. Remove Untracked Files

**Command**

```bash
git clean -fd
```

**Implementation**

```bash
git clean -fd
```

**Why**
Remove temporary files generated by builds.

---

## 28. Undo Last Commit Keep Changes

**Command**

```bash
git reset --soft HEAD~1
```

**Implementation**

```bash
git reset --soft HEAD~1
```

**Why**
Incorrect commit message or forgot a file.

---

## 29. Reset Everything

**Command**

```bash
git reset --hard HEAD
```

**Implementation**

```bash
git reset --hard HEAD
```

**Why**
Discard all local changes and return to last committed state.

---

## 30. Find Who Changed a Line

**Command**

```bash
git blame
```

**Implementation**

```bash
git blame application.yml
```

**Why**
Investigate who modified a configuration causing production issues.

---

# Common DevOps Workflows

## Feature Development

```bash
git pull origin master
git checkout -b feature/user-auth
git add .
git commit -m "Add JWT authentication"
git push -u origin feature/user-auth
git rebase master
```

**Scenario:** Building a new application feature.

---

## Release Preparation

```bash
git checkout master
git pull origin master
git checkout -b release/v2.0.0
git push origin release/v2.0.0
```

**Scenario:** QA team starts testing release candidate.

---

## Production Hotfix

```bash
git checkout master
git checkout -b hotfix/payment-failure
git commit -m "Fix payment timeout"
git push origin hotfix/payment-failure
git tag v2.0.1
```

**Scenario:** Critical production issue affecting customers.

---

## Sync Old Feature Branch

```bash
git checkout feature/order-api
git fetch origin
git rebase master
```

**Scenario:** Master has 50 new commits and you need latest code before PR creation.
