# Gitignore

- https://www.toptal.com/developers/gitignore
  - 위 사이트에 ignore할 소프트웨어를 검색
  - `.gitignore` 파일을 열어서 복사 + 붙여넣기
- **:star:`.gitignore`를 통해 git에서 해당 파일을 관리하지 않도록 하기 위해서 주의할 점**:star:
  - ignore 이전에 add를 하게 되면 이미 git에서 관리를 하고 있기 때문에 문제 발생
  - 따라서 `git init`을 한 이후에 바로 `.gitignore`를 해야 한다.

- `git bash`에서 `vi .gitignore`를 통해서도 가능하다.

- `git commit` 을 하면 타이틀 + 여러 줄을 쓸 수 있다.
  - `git log` : 전체 다 보임
  - `git log --oneline` : 타이틀만 보임
