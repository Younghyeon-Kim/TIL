# 평균은 넘겠지
c = int(input())
for _ in range(c):
    n = list(map(int, input().split()))
    score = n[1:]
    avg = sum(score)/n[0]
    result = 0
    for i in score:
        if i > avg:
            result += 1
    rate = result / n[0] * 100
    print(f'{rate:.3f}%')