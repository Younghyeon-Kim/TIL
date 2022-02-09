# 특정 종료 조건에서 탈출하기

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)