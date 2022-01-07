# Reset

- 쌓여있는 Commit 히스토리 중에서 특정 지점으로 돌아가는 것
  - conflict가 일어날 수 있기 때문에 자주 사용하지는 않는다

- `git reset --soft <commit 고유명>` : commit만
  - `git commit`하면 원 상태로 돌아옴
- `git reset --mixed <commit 고유명>` : staging area랑 commit
  - `git add` + `git commit`하면 원 상태로 돌아옴
- `git reset --hard <commit 고유명>` : working directory, staging area, commit 전부 다
  - 전부 다 Reset이 되어버림 

---

- `git reflog` : reset 내역까지 다보임
- `git revert <commit 고유명>` : 해당 commit을 취소하고 새로운 commit이 생성됨
  - 로컬에서도 사라짐 (생성하고 추가했다는 기록 자체를 삭제하는 것)
  - `git revert <commit1>..<commit2>` : 1부터 2까지 삭제

---

- HEAD를 Branch의 특정 시점(commit)으로 이동한다. 
  - 그때까지의 기록(버전)으로 열림

https://opentutorials.org/module/4032/24533

숙제 - soft, mixed, hard의 차이 알아보자...

---

### 협업하는 방식

- **git flow**
  - master- mainstream
  - develop - second mainstream
  - hotfix : 긴급 수정
  - realease : 마스터 전 검사
  - feature : 특정 기능



- **fork & pull model**
  - Pull request를 통한 협업이 가능, Github 기반의 오픈소스 참여 과정에서 쓰이는 방식



- **shared repository moder**
  - 동일한 저장소를 공유하여 활용하는 방식