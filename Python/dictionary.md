# Dictionary

### 1. 형식

- `{key : value, key : value ...}`
- :star:**key는 중복될 수 없다, key는 유일한 값이어야 한다.**
  - 따라서 key에 list를 쓸 수 없음
  - tuple은 가능은 하나 사용하지 않는 것을 추천
- dictionary에서 key는 list에서의 index와 같은 역할
  - index는 존재하지 않기 때문에 기본 출력인 key의 정렬 순서대로

```python
dic = {'name' : '김영현', 'age' : 27, 'birth' : '960604'}

dic2 = {1 : '김영현'}

# 흔치는 않지만 리스트를 넣을 수도 있음
dic3 = {'a' : [1, 2, 3]}
```

- dictionary안에 dictionary를 만들 수 있다.

  - `{key : {key1 : value1, key2 : value2 ...}}`
  - `dic['key']['key1']` 으로 따로 출력 가능

  ```python
  price = {'돌체라떼' : {'톨' : 5600, '그란데' : 6100, '벤티' : 6600},
           '초콜릿모카' : {'톨' : 5600, '그란데' : 6100, '벤티' : 6600},
           '카페모카' : {'톨' : 5100, '그란데' : 5600, '벤티' : 6100}}
  
  price['돌체라떼']['톨']
  
  >>>
  5600
  ```

  

### 2. 추가하기

- `dic[key] = value`
  - ``dic[index] = value` 도 가능하다

```python
dic4 = {1: 'a'}

#1
dic4['name'] = '김영현'

dic4

>>> {1: 'a', 'name': '김영현'}

#2
dic4[2] = 'b'

dic4

>>> {1: 'a', 2: 'b'}
```



### 3. 삭제하기

- `del dic[key]`
  - `del dic[index]` 도 가능하다

```python
del dic4[1]

dic4

>>> {1: 'a'}
```



### 4. 딕셔너리 관련 함수

- `dic.keys()` : key 값들만 return
- `dic.values()` : value 값들만 return

- `dic.items()` : (key, value)의 형태로 return
  - 위 전부 `[]`로 표현되나 list는 아님 각각 `dict_keys`, `dict_values`, `dict_values` type임
- keys, values, items를 리스트로 바꾸는 법

```python
list(price.keys())
list(price.values())
list(price.items())
```

- `dic.clear()` : 모두 지우기 
- `'key' in dic` : dictionary 안에 특정 key가 있는 지 확인
  - 있으면 True, 없으면 False