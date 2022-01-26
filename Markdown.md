# Markdown 문법

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

  ex) ![imglink](Markdown/github-logo-5F384D0265-seeklogo.com.png)

  



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




#### 10. 원본으로 보기

- `ctrl + /`



#### 11. 링크가 걸린 목차를 만들어보자

- README -> 다른 파일 : `[string](url)`활용
- 같은 파일 안에서 목차에 링크를 걸어보자
  - 링크가 걸리는 텍스트의 띄어쓰기는 `-`로 명시해야 한다.

```링크가 걸린 목차
[목차 텍스트1](#링크가-걸리는-텍스트1)
[목차 텍스트2](#링크가-걸리는-텍스트2)
...
# 링크가 걸리는 텍스트1
# 링크가 걸리는 텍스트2
```

- [참고 github](https://github.com/cheese10yun/TIL)