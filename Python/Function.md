# Function (함수)

:star:함수의 기본적인 구조 : input --> function --> output

### 1. 일반적인 형태

```python
# 함수의 정의 1
def 함수명 (입력값):
  실행문...

# 함수의 정의 2
def 함수명 (매개변수):
  실행문
  return 결과값
```

- **함수 호출** : `변수 = 함수명(인수)`

- :star:알아두면 좋은 차이 (현업에서는 따로 구분하지 않는 편)

  - **매개변수 (parameter)** : 함수가 입력 받은 값 (callee)

  - **인수 (argument)** : 정의된 함수를 사용할 때 입력하는 값 (caller)

    (callee, caller를 쓰는 이유 : 함수를 호출한다는 표현을 많이 쓰기 때문에)

---



### 2. 입력값이 없는 경우

- `변수 = 함수명()`

  ```python
  # 함수 정의
  def say():
    return 'hi'
  
  # 함수 호출
  a = say()
  
  print(a)
  >>> 'hi'
  ```

  ---

  

### 3. 결과값이 없는 경우

- `함수명(인수)`

  ```python
  # 함수 정의
  def add(a, b):
    print(f'{a}, {b}의 합은 {a + b} 입니다.')
  
  # 함수 호출
  add(5, 6)
  >>> 5, 6의 합은 11 입니다.
  ```

  ---

  

### 4. 입력값, 출력값 모두 없는 경우

- `함수명()`

  ```python
  # 함수 정의
  def say():
    print('hi~~~')
  
  # 함수 호출
  say()
  >>> hi~~~
  ```

  ---

  

### 5. 추가적으로

##### a. 매개 변수를 지정하는 것과 지정하지 않는 것의 차이

```python
# 함수 정의
def add(a, b):
  print(a)
  return a + b

# 매개 변수 지정
result = add(a = 3, b = 4)
result = add(b = 3, a = 4)
>>> 결과가 같음

# 지정하지 않는 경우 인수의 위치에 따라 값이 바뀐다.
result = add(3, 4)
>>> a = 3
>>> a + b = 7

result = add(4, 3)
>>> a = 4
>>> a + b = 7
```

---



##### b. 위와 같이 매개변수를 (a, b)로 정해 놓으면 인수 값을 2개 밖에 받을 수 없다.

- 범용성을 고려하여 아래와 같은 방법을 활용한다.

  ```python
  # *args : 개수와 상관없이 받겠다는 의미 (관습적으로 args로 통용 : arguments)
  def add2 (*args):
    result=0
    for arg in args:
        result += arg       # <-- 하나씩 불러온다는 의미
  
    return result
  ```

---



##### c. 계산기 만들어보기

```python
def cal(op, *args):
  if op == 'add':
    result = 0
    for arg in args:
      result += arg

  elif op == 'mul':
    result = 1
    for arg in args:
      result *= arg

  else:
    return 0

  return result
```

⭐ **result = 0, result = 1 이 들어간 이유**

- **변수를 초기화하는 값이 필요하다**
- add는 덧셈이기 때문에 0으로
- mul은 곱셈이기 때문에 0으로 할 수 없어서 1로

---



##### d. 키워드 파라미터

- **Dictionary**로 출력하기 위해서는 `**`을 사용한다
  - 통상적으로 `*`는 args, `**`는 kwargs

```python
# 함수 정의
def print2(**kwargs):
  print(kwargs)

# 함수 호출
print2(a=1)
>>> {'a': 1}

print2(name='김영현', age=27)
>>> {'name': '김영현', 'age': 27}
```

---



##### e. 결과 처리

- **Packing**된 **Tuple**을 결과 값으로 나타낸다

  ```python
  # 함수 정의
  def add_mul(a, b):
    return a+b, a*b
  
  # 결과 값
  result = add_mul(3, 5)
  print(result)
  
  >>> (8, 15) #기본 출력 값이 Tuple
  ```

- **Unpacking**

  ```python
  # 함수 정의
  res1, res2 = add_mul(3, 5)
  
  # 결과 값
  res1
  >>> 8
  
  res2
  >>> 15
  ```

  ---



##### :star:f. 파라미터를 확인할 때 쓰는 방법 (현업에서 중요함)

- 내가 설정한 파라미터가 유효한지 유효하지 않은지 확인한다.

  ```python
  # 함수 정의
  def say_nick(nick):
    if nick == '바보':
      return
  
    print(f'나의 별명은 {nick}입니다. ')
      
  # 확인
  say_nick('아이언맨')
  >>> 나의 별명은 아이언맨입니다. 
  
  say_nick('바보')
  >>>
  # return 값을 정의하지 않았기 때문에 아무 값도 나오지 않음
  ```

  ---



##### g. 기본값 설정

```python
# 함수 정의
def intro_me(name, age, sex='남자'):
  print(f'나의 이름은 {name}입니다. ')
  print(f'나의 나이는 {age}입니다. ')
  print(f'나는 {sex}입니다. ')

# 호출
intro_me('김영현', 27)

# 원래는 인수의 수가 맞지 않으면 에러가 발생한다.
# 그러나 기본값을 설정한 부분은 자동으로 기본값이 입력되기 때문에 결과가 나옴

>>> 나의 이름은 김영현입니다. 
>>> 나의 나이는 27입니다. 
>>> 나는 남자입니다. 
```

- 주의사항

  - 기본값을 설정한 매개변수 뒤에 다른 변수가 있으면 에러 발생
  - 따라서 **default**(기본값)이 있는 매개변수는 맨뒤로 보내야 한다.

  ```python
  # 이 경우에는 에러가 발생
  def intro_me(name, age, sex='남자', hobby):
    print(f'나의 이름은 {name}입니다. ')
    print(f'나의 나이는 {age}입니다. ')
    print(f'나는 {sex}입니다. ')
    print(f'나의 취미는 {hobby}입니다. ')
      
  # 올바른 버전
  def intro_me(name, age, hobby, sex='남자'):
    print(f'나의 이름은 {name}입니다. ')
    print(f'나의 나이는 {age}입니다. ')
    print(f'나의 취미는 {hobby}입니다. ')
    print(f'나는 {sex}입니다. ')
      
  # 참고로 print의 순서는 바뀌어도 상관 없음
  ```

  ---



### 6. :star:변수 스코프:star:

- 글로벌 변수(전역 변수) : 전 영역에서 쓰는 변수 / 함수를 호출할 때 쓰는 변수
- 로컬 변수(지역 변수) : 특정 부분에서 쓰이는 변수 / 함수를 정의할 때 함수 안에서 사용되는 변수



**글로벌 변수와 로컬 변수의 구분**

- gVar : 글로벌 변수
- lVar : 로컬 변수

```python
gVar = 1              # 위의 gVar의 값이 변하지 않는다

def vartest(lVar):
  lVar = lVar + 1
  print(lVar)
  return lVar        

gVar = vartest(gVar)  # 여기서 gVar의 값을 바꿔주는 것
# gVar자체가 함수안에 가는 것이 아니라 gVar 값만 위쪽에 정의된 함수안에서 lVar로 대입해 연산
# 연산된 결과가 gVar가 되어서 출력 
gVar
```

---



### 7. 람다함수 (익명함수, Anonymous Function)

- 형식 : `함수명 = lambda 파라미터 : 실행문`

```python
# 예시
add = lambda a, b : a + b

result = add(1, 2)
result
>>> 3

# 위와 같은 기존 함수 형식
def add(a, b):
  return a + b
```

