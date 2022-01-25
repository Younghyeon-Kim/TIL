# 문자열 (string)

### 1. 문자열 만들기

- `'str'` ,  `"str"`

- 줄바꿈을 해도 Syntax Error가 뜨지 않는 방법

  1. `'''str'''`

  2. `"""str"""`

  3. 이스케이프 코드 `\n` 을 삽입



- 문자열 안에 따옴표를 포함시키고 싶을 때

  1. 다른 따옴표로 구분한다

     ex) `"Jane's shoes"` , `'she said "I hate you"'`

  2. `\`를 사용하여 `'`, `"` 자체를 문자열에 포함시킨다

     ex) `'she said "you\'re so special"'`



### 2. 이스케이프 코드

1. `\n` - 줄 바꿈
2. `\t` - 탭 간격
3. `\\` - 문자열에 `\` 포함
4. `\'` - 문자열에 `'` 포함
5. `\"` - 문자열에 `"` 포함
6. `\r` - 줄 바꿈 (캐리지 리턴) : 현재 커서를 가장 앞으로 이동
7. `\f` - 줄 바꿈 (폼 피드) : 현재 커서를 다음 줄로 이동
8. `\a` - 벨소리 : 출력 시 '삑' 소리
9. `\b` - 백 스페이스
10. `\000` - null 문자



### 3. 문자열 연산하기

1. 문자열 연결 (concatenation) : `+`

   ```python
   a = 'I '
   b = 'love '
   c = 'you'
   
   a + b + c
   >>> 'I love you'
   ```

2. 문자열 반복 (곱하기) : `*`

   ```python
   a = 'ha '
   
   a * 3
   >>> 'ha ha ha '
   ```

3. 문자열 길이 구하기 : `len()`

   ```python
   a = 'I love you'
   
   len(a)
   >>> 10
   ```



### 4. :star:인덱싱, 슬라이싱

- **인덱싱**

  문자열 안에 문자들은 각각 **인덱스 값**(위치 정보)을 가진다

  인덱싱은 문자열 안에 특정 인덱스 값에 있는 문자를 출력한다

  ```python
  a = 'I love you'
  
  a[5]
  >>> 'e'
  ```

  - 인덱스는 1이 아닌 0부터 시작한다
  - `-`는 0을 기준으로 거꾸로



- **슬라이싱**

  문자열 안에 원하는 부분을 짤라오는 방법

  `str[start:stop:step]`

  ```python
  a = 'I love you'
  
  a[1:9:2]
  >>> ' oey'
  ```

  - [A:B] - A부터 B까지 :star:B는 포함하지 않는다.
  - [A:] - A부터 끝까지
  - [:B] - 처음부터 B까지 (B는 미포함)
  - [:] - 전체



### 5. 문자열 포맷팅

- 만들기

  ```python
  'I ate %d apples' %3
  >>> 'I ate 3 apples'
  
  'I ate %s apples' %'three'
  >>> 'I ate three apples'
  
  # %s 여도 숫자를 쓰는 경우 자동으로 변환이 됨
  'I ate %s apples' %3
  >>> 'I ate 3 apples'
  ```

- 문자열 포맷 코드

  1. `%s` - String(문자열)

  2. `%c` - Character(문자 1개)

  3. `%d` - Integer(정수), 10진수

  4. `%f` - Floating-point(부동소수)

  5. `%o` - 8진수

  6. `%x` - 16진수

  7. `%%` - Literal %(문자 % 자체)

     - 포매팅 연산자`%d` 와 `%`를 같이 써야 할 경우

     ```python
     '%d%% discount %30'
     
     >>> '30% discount'
     ```

- 포맷 코드와 숫자 함께 사용하기

  - 정렬과 공백

    - `%숫자s` : 숫자만큼 자리를 만들고 문자열을 우로 정렬 후 나머지는 공백
    - `%-숫자s` : 숫자만큼 자리를 만들고 문자열을 좌로 정렬 후 나머지는 공백

    ```python
    '%10s' %'hi'
    >>> '        hi'
    
    '%-10sjane.' %'hi'
    >>> 'hi        jane.'
    ```

  - 소수점 표현하기

    - `'%숫자1.숫자2f'` : 숫자1만큼 정렬, 숫자2는 소수점 몇째자리**(반올림)**까지

      ```python
      '%10.4f' % 7.123456789
      >>> '    7.1235'
      ```

---

- format 함수

  `{}`안에 숫자(인덱스) 혹은 변수 자체를 넣는 방법이 있다. 

  :star:**항상 `{0}` 부터 시작**

  `'I ate {0} apples'`

  - 숫자 대입 : `.format(3)`

  - 문자열 대입 : `.format('three')`

  - 숫자 값의 변수 대입

    ```python
    n = 3
    'I ate {0} apples' .format(n)
    
    >>> 'I ate 3 apples'
    ```

  - 2개 이상의 값

    ```python
    n = 10
    d = 'three'
    'I ate {0} apples. so I was sick for {1} days.'.format(n,d)
    
    >>> 'I ate 10 apples. so I was sick for three days.'
    ```

  - 이름으로 넣기

    ```python
    'I ate {n} apples. so I was sick for {d} days.'.format(n=10,d=3)
    
    >>> 'I ate 10 apples. so I was sick for 3 days.'
    ```

  - 인덱스와 이름 혼용

    ```python
    'I ate {0} apples. so I was sick for {d} days.'.format(10,d=3)
    
    >>> 'I ate 10 apples. so I was sick for 3 days.'
    ```

  ---

  <알아두기>

  - 정렬과 공백

    - 좌로 정렬 : `'{0:<10}'.format('hi')`

    - 우로 정렬 : `'{0:>10}'.format('hi')`

    - 가운데 정렬 : `'{0:^10}'.format('hi')`

    - 공백 채우기 : `'{0:기호<10}'.format('hi')`

      공백이 입력한 기호로 대체

  - 소수점 표현

    - `'{0:총자리수.소수점f}' .format(y)`

  - { }문자 그대로 표현하기

    - `'{{ 내용 }}'.format()` --> `'{ 내용 }'`

---

#### :star:F 문자열 포매팅

- 가장 유용하다
- 단점 : Python 3.6 이하 버전에서는 사용 불가

```python
name = '김영현'
age = 27
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

>>> '나의 이름은 김영현입니다. 나이는 27입니다.'
```

- 표현식

  ```python
  age = 29
  f'내년이면 나도 {age+1}살이 된다.'
  
  >>> '내년이면 나도 30살이 된다.'
  ```

- **딕셔너리**

  `*`의 역할 : 값을 끌어온다. 원하는 값의 개수에 따라 늘어남 (2개의 경우 `**`)

  ```python
  dic = {'name' : '김영현', 'age' : 27}
  f'나의 이름은 {dic["name"]}입니다. 나이는 {dic["age"]}입니다.'
  
  >>> '나의 이름은 김영현입니다. 나이는 27입니다.'
  
  
  # *를 사용하는 방법
  f'나의 이름은 {dic["name"]}입니다. 나이는 {dic["age"]}입니다.'.format(**dic)
  
  >>> '나의 이름은 김영현입니다. 나이는 27입니다.'
  ```

  

### 6. 문자열 함수

- `a.count('b')` : `a`문자열안에 `'b'`(특정 값)이 몇 개 있는지 세기
- `a.find('b')` : `'b'` 가 `a` 문자열 어느 인덱스에 있는지 찾기
  - `'b'`가 없을 경우에 `-1` 을 출력함

- `a.index('b')` : `'b'` 가 `a` 문자열 어느 인덱스에 있는지 찾기

  - find와 다른 점 : 값이 없을 경우 error 발생

  :star:**Python의 경우 error 발생 시 동작을 멈추기 때문에 `find` 사용 지향**

- `''.join()` : `()` 문자열 사이사이에 `''` 값을 넣는다

- `.upper()` : 전부 대문자

- `.lower()` : 전부 소문자

- `.strip()` : 좌우 공백 지우기

  - `.lstrip()` : 왼쪽 공백 지우기
  - `.rstrip()` : 오른쪽 공백 지우기

- `.replace('a', 'b')` : 문자열의 a를 b로 대체하기

  - `+` 연산과 슬라이싱을 활용할 수도 있음

- `.split('기준')` : 기준으로 문자열 쪼개기

  ```python
  a = 'a:b:c:d'
  a.split(':')
  
  >>> ['a', 'b', 'c', 'd']
  ```

  