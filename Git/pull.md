# Pull, Clone

- `git clone <url> .`

  **git 안에 git이 있는 것은 절대 안됨**:no_entry_sign:

- clone, push, 허락을 받고 push에 대한 권한을 설정할 수 있다.



- clone은 제로부터 끌어오고 pull은 이미 있는 상태에서 가져오는 행동



- 가정
  - 이미 레포지토리에 커밋이 올라가 있다.
  - pull, push하는 권한이 있다.
- clone
  - 빈 폴더 (상위 폴더에 깃이 없어야 함)에 clone을 합니다
    - `git clone <url>` : 새로운 폴더를 만든다
    - `git clone <url> .` : 현재 폴더에 그대로
- do something and push commit
  - 원격 저장소가 원본 로컬 저장소보다 상위 버전이 됨
- pull
  - 운본 로컬 저장소에서 원격 저장소의 코밋을 pull 함
    - `git pull`



## 사고났을 때

### prac1

- 왼쪽 디렉토리에서 a.txt를 변경합니다.
- 그에 대한 코밋을 남깁니다
- 원격 저장소에 push합니다



### prac2

- 오른쪽 디렉토리에서 a.txt를 변경합니다.
- 그에 대한 코밋을 남깁니다.
- 원격 저장소에 pull합니다
- vscode에서 합쳐주고 push



## Conflict 해야 함 Merging 해결하기

- prac 1에서는 prac2가 conflict한 것을 push 하고 prac 2에서 pull을 하면 해결

