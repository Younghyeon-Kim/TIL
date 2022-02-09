# 테스트 케이스 갯수에 따라 유동적으로 입력받기

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A + B)

# 더 깔끔한 방법
# for T in range(int(input())):
#     a, b = map(int, input().split())
#     print(a + b)