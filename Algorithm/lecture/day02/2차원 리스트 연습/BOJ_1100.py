# 하얀 칸
board = [list(input()) for _ in range(8)]
total = 0

# 이중 for 문
for i in range(8):
    for j in range(8):
        # 하얀 칸의 인덱스 패턴 파악
        # if (i + j) % 2 == 0:
        # 반대로도 가능 board[j][i]
        if i % 2 == j % 2 and board[i][j] == 'F':
            total +=1

print(total)