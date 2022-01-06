

# TIL : Today I Learned

##### 2022 01 05

- 늦게 출발한만큼 쉬지 않고 달리기



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

## 2. CLI 기초

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



## 3. Markdown 문법

- Typora 설치 (UI가 편리하다)
- Git hub 문서 : README.md 파일을 통해 오픈소스의 공식 문서 작성

#### 1. 헤딩

- `#` : h1
- `##` : h2
- `###` : h3
- `######` : ~ h6
- `ctrl+1` ~ `ctrl+6` 도 가능하다



#### 2. 리스트

- 순서가 있는
  - `1.`  :  순서가 있는 리스트 생성
- 순서가 없는
  - `-`/`*` : 순서가 없는 리스트 생성
- `tab`을 사용해서 들여쓰기 가능!!



#### 3. 코드 블록

- ````
  ```
  ````

  - 백킷을 세번 (```)  입력하면 **코드블럭**이 만들어지고
  - 백킷을 한번(`) 입력하면 **인라인 코드블럭**이 만들어짐

``` python
print('hello Korea!')
if my_country = "Korea":
    print('Yes')
else:
    print('No')   
```



#### 4. 링크

- `[string](url)` : 링크 생성
  - 반드시 url은 full link로 해야 한다

​		ex) [Hello world](https://www.google.com/search?q=hello+world&tbm=isch&ved=2ahUKEwjTxdb355n1AhXVAd4KHZKtAQwQ2-cCegQIABAA&oq=hello+world&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOgQIABADOgQIABAeUKARWIszYO40aAFwAHgAgAFniAGGCpIBAzguNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=oSPVYZPxONWD-AaS24Zg&bih=587&biw=1278)



#### 5. 이미지 링크

- `![string](img_url)`:

  ex) ![imglink](README/github-logo-5F384D0265-seeklogo.com.png)

  



#### 6. 텍스트 강조

- `**안녕**` : **안녕** -> 볼드체 : `ctrl+b`
- `*안녕* `: *안녕* -> 이태리체 : `ctrl+i`
- `~~안녕~~` : ~~안녕~~ -> 취소선 
- `***안녕***` : ***안녕*** -> 볼드체 + 이태리



#### 7. 수평선

- `---` : 단락을 구분할 수 있다. (`***`, `___` 로 대체 가능)

  ---

  

#### 8. 인용문

- `>`

  - > 논문

- `>>`

  - > > 논문



#### 9. 표

- `|A|` 가 표로 1칸

  ex) `|A|B|`

- | A    | B    | C    |
  | ---- | ---- | ---- |
  |      |      |      |

  