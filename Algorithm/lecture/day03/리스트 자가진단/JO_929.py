#리스트3 - 형성평가1
n = int(input())
a = []

for i in range(1, n+1):
    numbers = f'No.{i}'
    a.append(numbers)

print(a)

# 리스트 컴프리헨션
# n = int(input())
# a = [f'No.{i}' for i in range(1, n+1)]
# print(a)