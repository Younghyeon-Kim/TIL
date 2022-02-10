# 수 정렬하기
n = int(input())
numbers = [int(input()) for _ in range(n)]
# unpacking 활용
sorted_numbers = sorted(numbers)

print(*sorted_numbers, sep='\n')