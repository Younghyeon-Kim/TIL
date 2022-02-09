# 문자열 반복

for T in range(int(input())):
    n,s = input().split()
    n = int(n)
    for i in s:
        print(i * n, end='')
    print()