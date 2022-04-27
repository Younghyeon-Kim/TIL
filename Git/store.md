### 1. Restore 복원하기

- `git restore <name>` : 다시 돌아오기
  - restore 는 staging area 나 commit의 가장 최근 상태로 돌아가는 것
    - 가장 최근 기록(staging area, commits)으로 돌아온다

- `git restore --staged <name>` : `git add` 이전 상태로 돌아가는 것(working directory)
  - staging area에서 내려준다

---

- 원래는 한번 add를 하게 되면 ignore할 수 없다
  - **예외** - `git rm --cached <name>` : untracked 상태로 바꿔준다
    - git -> local

---

### 2. Commit Massage 수정하기

- `git commit --amend`
  - 파일 수정이 없으면 commit massage만 재작성
  - 파일 수정이 있으면 그것을 반영하여 commit을 덮어씌운다

---

### 3. Diff 차이점 확인하기

- `git diff` : 가장 최근 기록과의 차이
  - **(working directory <-> 최근 commits *OR* 최근 staged)**
- `git diff --staged` : staging area와 commits의 차이
  - **(staging area <-> commits)**