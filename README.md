## 1. Git Setting on local
### 1.1.a. Install Git
- https://git-scm.com/
### 1.1.b. Git Configuration
- 작업폴더에서 우클릭후 git bash 열기  
- 유저이름 및 이메일 설정, 설정확인  
git config --global user.name "your_name"  
git config --global user.email "your_email"   
git config --list

## 1.2. Git Add
git init  
git add <filename>  
git status //확인  

## 1.3. Generate History  
git commit -m "first commit"

## 1.4. Connecting a Github repository with my local project
git remote add origin <github_URL>  
git remote -v //확인  

## 1.5. Git Push on a specific branch 
git push origin <branch_name>  

---

## 2. How to Team a project using Github
### 2.1. Git Clone
git clone <URL>  
### 2.2. Git Switch
git branch -a
git switch <branch_name>
### 2.3. Update from local to Git
git add <file_name>  
git commit -m "<your commit name>"  
git push origin <branch_name>  









