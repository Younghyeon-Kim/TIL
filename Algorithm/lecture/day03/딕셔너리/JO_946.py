n = int(input())

countries = {}

for _ in range(n):
    k, v = input().split()
    countries[k] = v

print(countries.get(input(), 'Unknown Country'))