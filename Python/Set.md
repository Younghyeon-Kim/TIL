# Set (집합)

## 1. 형식

- `set(객체)`

- `{[객체1, 객체2, 객체3, ...]}`

- :star: **Set**은 중복을 허용하지 않는다.

  ```python
  >>> 집합 = set('Hello')
  ...
  >>> 집합
  ...
  >>> {'H', 'e', 'l', 'o'}
  ```

- set에는 index가 없기 때문에 list나 tuple로 바꿔서 접근해야 함

  - `집합 = list(집합)`
  - `집합 = tuple(집합)`



## 2. 교집합, 합집합, 차집합

```python
s1 = set([1, 2, 3, 4, 5, 6])
s2 = {4, 5, 6, 7, 8, 9}
```

- 교집합
  - `&`  
    - s1 & s2 = s1과 s2의 교집합
  - `.inintersection()` 
    - s1.intersection(s2) =  s1과 s2의 교집합

- 합집합
  - `|`
    - s1 | s2 = s1과 s2의 합집합
  - `.union()`
    - s1.union(s2) = s1과 s2의 합집합
- 차집합
  - `-`
    - s1 - s2 = s1과 s2의 차집합
  - `.difference()`
    - s1.difference(s2) = s1과 s2의 차집합



## 3. 추가, 삭제

- 추가하기
  - `집합.add(객체)`
  - `집합1.update(집합2)`

- 삭제하기
  - `집합.remove(객체)`
  - `집합.discard(객체)` : 사용하지 않는다
  - dicard를 사용하지 않는 이유 :
    - 없는 객체의 삭제를 시도할 경우 `remove` 는 에러 발생
    - `discard`는 따로 return 값이 없기 때문에 :star:**확인의 어려움**이 있다.