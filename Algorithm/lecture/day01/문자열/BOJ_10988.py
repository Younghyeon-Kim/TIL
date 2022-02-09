#팰린드롬 = 뒤집어도 같은 문자열
word = input()
if word == word[::-1]:
    print(1)
else:
    print(0)