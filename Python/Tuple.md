# Tuple

:star: **'튜플은 값을 바꿀 수 없다'** 라는 특징을 활용하여 바뀌면 안되는 값이 있을 때 사용한다

## 1. 생성

```python
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
t6 = tuple()
```

## 2. 응용

1. 인덱싱

```python
t1 = (1, 2, 'a', 'b')

t1[0]
>>> 1
```

2. 슬라이싱

```python
t1 = (1, 2, 'a', 'b')

t1[1:]
>>> (2, 'a', 'b')
```

3. 연산(+,*), len

```python
t1 = (1, 2, 'a', 'b')
t2 = ('c', 'd')

t1 + t2
>>> (1, 2, 'a', 'b', 'c', 'd')

t2 * 4
>>> ('c', 'd', 'c', 'd', 'c', 'd', 'c', 'd')

len(t1)
>>> 4
```

4. 튜플을 리스트로 바꾸기
   - `튜플1 = list(튜플1)`

5. Packing, Unpacking

```python
# packing
cell = ('apple', 'samsung', '샤오미', '화웨이', '레노버')

# unpacking
a, s, x, h, l = cell

a
>>> 'apple'

h
>>> '화웨이'
```

