## 1. How to co-work using Github
### 1.1. Git Clone
git clone <github_URL>  
### 1.2. Git Switch
git branch -a  
git switch <branch_name>
### 1.3. Update from local to Git
git add <file_name>  
git commit -m "<commit_message>"  
git push origin <branch_name>  



# Git Command

---

## 1. Clone with commit-msg hook

→ `git clone “ssh://………..” && scp -p`

- 복사후 local에서 실행

## 2. Branch 확인

`git branch -a`

## 3. Branch 이동

`git switch <Branch Name>`

## 4. Git에 코드 로드

`git config --global user.email "your@email.com"`

`git config --global user.name "your name"`

`git add test.c`

`git commit -m <Commit Message>`   

`git push origin HEAD:refs/for/master`  /* pushing a main branch */

# Github

---

## 1. SSH Key 생성

`ssh-keygen -t rsa -C "your_github_email"`

- 실행시 ./ssh 하위에 id_rsa와 id_rsa.pub 파일 생성
- id_rsa.pub : Public Key이므로 Github에 ssh키 등록시 사용
- id_rsa : Private Key이므로 개인 보관

## 2. Public Key 복사

`cat ~/.ssh/id_rsa.pub`

## 3. Github에 Public Key 등록

Settings → SSH and GPG keys → New SSH key

- Title은 임의로 작성, Key type은 Authentication
- Key란에 복사내용 붙여넣기

## 4. RSA키로 Git clone 확인

`git clone [git@github.com](mailto:git@github.com):<user_name>/<repo_name>.git`

- Clone에서 복사후 git clone 이후 local에서 pull 결과 확인

