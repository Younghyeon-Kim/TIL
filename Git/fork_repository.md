# 1. 그룹 레포지토리 Fork 하기

1. 마스터 레포지토리 fork

5. 로컬에서 clone

   * `git clone <fork한 레포지토리 Url> <파일명> ` 

     ***주의: 본인 계정에 Fork한 레포지토리 Url을 통해 clone 해야 합니다**

6. remote repository 추가

   * `git remote -v` 입력후 `origin`이 출력되는지 확인

   * `git remote add upstream <마스터 레포지토리 Url>`

   * `git remote -v` 입력후 `origin`과 `upstream`이 출력되는지 확인

     > upstream은 github 레포지토리의 내용을 컴퓨터 디렉토리에 반영하기 위해 만드는 겁니다



# 2. 개인 branch 만들기 

1. `git branch <이름 초성 소문자> `로 해주시면 구분이 편함

2. `git checkout -b <이름>`
   - pull request -> `master branch` 에서 merge



# 3. 파일 수정하기

1. 각자 branch 에서 작업

   - `git add .` 

   - `git commit -m 'add <파일명>'`

   - ``git push origin <작업한 개인 branch>`

2. pull request & merge



# 4. 로컬 디렉토리를 git hub와 동기화

1. master branch에서 작업 : `git branch master`
2. `git fetch upstream`
3. `git merge upstream/master`
