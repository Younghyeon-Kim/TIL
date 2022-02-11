# 리스트 3 - 자가진단1
n = int(input())
a = []

for i in range(1, n+1):
    square_num = i * i
    a.append(square_num)

print(a)

# 리스트 컴프리헨션
# a = [i * i for i in range(1, n+1)]
# print(a)