# 리스트 3 - 자가진단 6
a = [list(map(int, input().split())) for _ in range(2)]
b = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    for j in range(4):
        print(a[i][j] * b[i][j], end=" ")
    print()