# 별 찍기 - 2

T = int(input())
for i in range(T):
    print(' '* (T - (i+1)) + '*' * (i+1))