# 색종이

# (100 X 100 행렬)도화지를 만든다. 칸 값 = 0
paper = [[0] * 100 for _ in range(100)]

# 색종이 갯수 받기
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            # 도화지가 빈칸이면
            if paper[i][j] == 0:
                paper[i][j] = 1 # 색칠
            # 도화지가 이미 색칠되어 있으면
            else:
                continue

# 영역의 넓이 출력하기
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]

# 함수 활용
# total = sum(sum(line) for line in paper)

print(total)