# Git CLI

### Git - Github 연결 (User)

- **한번만 해도 되는 작업**
- `git config --global user.name 'user_name'` : username 등록
  
- `git config --global user.name` : user.name 확인
  
- `git config --global user.email 'user_email'` : email 등록
  
- `git config --global user.email` : email 확인

---

### Git - Github 연결 (Repository)

- **Repostory 연결할때는 한번만 해도 되는 작업**

  - `git init` : git 시작

  - `git remote add origin <git repository url>` : repository 연결
  - `ctrl + v` : 문서작업용
  - `shift + insert` : 붙여넣기



- **파일 수정, 생성 할때마다 해야하는 작업**

  - `git add .` : 모든 파일 staging area에 올리기

  - `git add <file_name>` : 파일 staging area에 올리기

  - `git commit -m 'commit massage'` : commit massage 작성

  - `git push origin master` : github로 밀어내기



- 자주하는 실수
  - .git 이 이미 존재하는 폴더 하위 폴더에 `git init`을 하는 경우 에러가 발생