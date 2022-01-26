# Git

## 1. Git

- Git : 분산 관리 시스템 (CLI를 사용)
  - **CLI**(Command Line Interface) : 터미널을 통해 사용자와 컴퓨터가 상호작용하는 방식
  - GUI(Graphic User Interface) : 그래픽을 통해 사용자와 컴퓨터가 상호작용하는 방식
    - Window 운영체제에서 Unix/Linux 명령어를 사용하기 위해서 **Git bash**를 쓴다
- Commit은 3가지 영역을 바탕으로 동작
  - Working Directory : 내가 작업하고 있는 실제 Directory
  - Staging Area : Commit으로 남기고 싶은, 특정 버젼으로 관리하고 싶은 파일 저장소
  - Repository : Commit들이 저장되는 곳

- `git init` : 로컬 저장소 생성
- `git add`, `git commit -m`, `git push origin master`



### 로컬

- **`git init`** : git으로 관리하겠다는 의미
- do something(생성, 수정)
  - 파일 생성, 폴더 생성(빈폴더는 안됨)
- `git add .`
- `git commit -m 'message'`

### 원격(최초 1회)

- **깃허브 레포 만들기**
- **`git remote add origin <url>`**
  - `git remote add <name> <url>`


### 원격

- `git push -u origin master`
  - `-u` 옵션이 차후 push를 할 때 뒤의 아이들 쓰지 않아도 되게 함



## 2. Git CLI

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



## 3. CLI 기초

- `ls` : 현재 위치의 폴더, 파일 목록보기

  - `ls -a` : 숨겨진 폴더까지 볼 수 있음

- `cd <path>` : 현재 위치 이동하기

- `cd ..` : 상위 폴더로 이동하기

- `mkdir <name>` : 폴더 생성하기

- `touch` : 파일 생성하기

- `vi` : 기존에 파일이 있다면 수정하기, 없다면 생성하면서 수정

  (`i` : 글쓰기, `esc + : + wq` : 저장)

- `rm` : 삭제하기

- `start` (Windows), `open` (Mac) : 폴더나 파일 열기

- `mv` : 폴더를 이동하거나 이름을 변경하기
