

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

  ex) ![git](data:image/png;base64,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)

  



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

  