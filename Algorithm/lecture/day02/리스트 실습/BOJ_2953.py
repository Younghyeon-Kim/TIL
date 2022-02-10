# 나는 요리사다
score = [sum(map(int, input().split())) for i in range(5)]

print(score.index(max(score))+1, max(score))