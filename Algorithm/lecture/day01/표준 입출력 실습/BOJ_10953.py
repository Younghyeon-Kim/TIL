# 공백 외의 문자로 구분된 정수 입력받기

for T in range(int(input())):
    A, B = map(int, input().split(','))
    print(A + B)