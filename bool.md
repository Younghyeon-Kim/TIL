# Bool

### 1. 생성

**만들기**

- True의 T와 False의 F는 반드시 **대문자**
- `=` : assignment
- `==` : equal



### 2. 조건문에서

**True**

- 명시적으로 : `a = True`
-  `a = 1` (아무 값)

**False**

- 명시적으로 : `a = False`
- 암묵적으로 : 숫자 `0`, `None`, `''`(문자열인데 아무것도 없는 것)



**While** : False가 될 때까지 실행(반복문)

```python
a = [1, 2, 3, 4]

while a:
  print(a.pop())

4
3
2
1
```



**If** : 값에 따라서 다른 실행 결과

```python
# 리스트[]안에 값이 있다면 '참' 없다면 '거짓'
# 아무 값이 없는 리스트는 '거짓'으로 판단하는 경우가 있음

if []:
  print('참')
else :
  print('거짓')

>>> '거짓'

if [1, 2, 3]:
  print('참')
else :
  print('거짓')

>>> '참'
```



### 3. 추가적으로

`bool()` : True or False 확인해보기

```python
bool('Python')

>>> True

bool('')
>>> False
```

