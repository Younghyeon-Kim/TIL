# **Class**

- 객체 지향 프로그래밍



### 1. 함수의 한계

- 작업자 1과 작업자 2가 함수를 사용하는 경우
  - 글로벌 변수의 값이 변하면서 생기는 문제들을 해결하기 위해 아래와 같은 방법을 사용함
  - 아래의 단점 : 작업자가 늘어날수록 계속 만들어줘야하는 불편함이 있다.
    - :star: 그래서 **`class `**를 사용한다.

```python
result1 = 0
result2 = 0

def add1(num):
  global result1
  result1 += num
  return result1

def add2(num):
  global result2
  result2 += num
  return result2
```



### 2. Class 정의

- 중요한 요소 : 클래스, 객체, 인스턴스

```python
# 계산기를 만들어보자

# 관례적으로 클래스명의 첫글자는 대문자를 사용한다

class Calc:

  # Method : 클래스에 포함된 함수
  # self는 특정 객체의 변수로 구분짓는 역할
  
  def setData(self, first, second):
    self.first = first
    self.second = second

  def add(self):
    return self.first + self.second

  def sub(self):
    return self.first - self.second
  
  def mul(self):
    return self.first * self.second
  
  def div(self):
    return self.first / self.second
```

- 객체를 만들기
  - `a = Calc()`	
  - `a.setData(4, 2)` : 객체 변수에 값을 입력한다

- 객체 변수 확인
  - `a.first` : 4
  - `a.second` : 2

- 함수를 호출하는 방법
  - `a.함수()` : 지정된 객체 변수 값에 정의된 함수를 호출하여 출력값을 뽑는다

- :star: 같은 클래스 다른 객체
  - `a = Calc()` 와 `b = Calc()` 라는 객체 변수를 만들었을 때
    - `a.first` 와 `b.first` 는 다른 것이다 



### 3. 생성자 : constructor

- 따로 입력하지 않아도 default init이 존재하긴 함
- 객체 값을 초기화하고 재정의하기 위해서 사용하는 기능
  - Python interpreter가 지정하는 클래스에 대한 함수
- :star: 클래스의 기능이 광범위해지면 관리가 어렵기 때문에
  - **객체 변수는 생성자에서 선언하는 것**이 관리면에서 용이함

```python
class Calc:
    
	def __init__(self, first, second):
    	self.first = first
    	self.second = second
```

- 객채 변수 만들기
  - `객체명 = 클래스명(first, second) `



### 4. 상속

- `class 상속받는클래스(상속하는클래스)`

- 상속받은 클래스에 새로운 함수를 추가할 경우
  - 상속해준 클래스에는 함수가 추가되지 않는다



### 5. 클래스 변수와 객체 변수

- 클래스 변수 : 모든 객체들이 공유하는 변수
- 객체 변수 : 클래스로부터 생성된 각각의 객체에 존재한
  - `self.변수` : 보통의 형태
    - 여기서 `self`는 객체 자체를 가리킨다 (나의 것이라는 의미)

```python
# 클래스만 정의하는 경우 : 아직 객체가 만들어지지 않은 상태

class Family:
  lastname = '김'

# 이때의 클래스 변수
>>> Family.lastname 
>>> '김'

# 객체를 만들고
>>> a = Family()

# 형식으로 보아서는 객체 변수의 값을 부르는 것 같지만
# 클래스 정의에서 객체 변수를 만들지 않았기 때문에 불러온 값은 클래스 변수이다.
>>> a.lastname
>>> '김'
```



### 6. 추가적으로

- 클래스를 상속하고 새로운 객체 변수를 추가하는 경우

  - Car 클래스를 상속해서 Truck 클래스 만들기

  - `super().__init__(wheel, engine)` : 상속해준 클래스의 변수를 초기화

  - 아래와 같이 하는 이유

    - 기존 Car 클래스에 존재하던 정의를 다시 입력해줘도 되지만

    - 특정 객체의 인스턴스가 어떤 클래스에서 발생했는지 구분짓기 어렵다

      하지만 상속관계로 인해 Truck 클래스에서 인스턴스된 객체 변수는

      Car 클래스에서 인스턴스된 객체 변수이기도 하다.

```python
class Truck(Car):
  def __init__(self, wheel, engine, luggage): # 변수들을 다 적어줘야 함
    super().__init__(wheel, engine)
    self.luggage = luggage
```

- 마지막으로

  `객체.wheel = `로 변수를 지정하면

  `super().__init__`를 하지 않더라도 객체 변수가 추가된다

  :star: 그러나 객체 변수를 어디서 생성했는지 확인하기 어렵기 때문에

  **객체 변수는 생성자에서 추가**하는 것이 바람직하다

- 상속관계를 확인하는 방법

  - `클래스명.mro()`

    ```python
    >>> Truck.mro()
    ...
    >>> [__main__.Truck, __main__.Car, object]
    ```

    

