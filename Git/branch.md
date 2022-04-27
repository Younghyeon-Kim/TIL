# Branch

- 내가 지금 작업하고 있는 공간
  - master -> main 으로 바뀌는 추세 
  - Black Lives Matter를 거치며 master가 주종관계를 연상

- `git branch` : 지금 어디서 작업 중인지 확인하기
- `git branch <name>` : branch 생성하기
- `git switch <branch name>` : branch 이동하기
- `git log --all` : 다른 branch 작업까지 볼 수 있음
- `git merge <branch name>`

- `git branch --graph` : 좀 더 보기 쉽게 그래프로 보여줌
- `git branch -d ''<name>''` : branch 삭제하기
- `git switch -c '<name>'` : 만들면서 이동

---

- 브랜치 만들기

  - `git branch <name>`

- 브랜치 확인

  - `git branch`

- 브랜치 지우기

  - `git branch -d <name>`
  - `git branch -D <name>` : 더 강력한 명령어 (merge하지 않은 상태에서도 삭제)

- 브랜치 이동

  - `git switch <name>`
  - `git checkout <name>`
  - 만들면서 이동
    - `git switch -c <name>`

- branch merge situation

  - 기준이 될 branch에서
    - git merge (합칠 branch 이름)

  1. 두 브랜치 모두에서 수정사항이 있지만, 겹치지 않은 상황
     - 3-way merge
  2. 두 브랜치 모두에서 수정사항이 있고, 겹친 상황
     - Conflict 해결 후 commit
  3. 합쳐질 브랜치에만 수정사항이 있는 상황
     - Fast-forward 잘 합쳐짐