#리스트3 - 자가진단 7
score = [list(map(int, input().split())) for _ in range(5)]
success = 0

# [i][j] 한칸 씩 도는 방법
# for i in range(5):
#     # total 지정이 아래로 가면 칸마다 0으로 초기화됨
#     total = 0
#     for j in range(4):
#         total += score[i][j]
#     avg = total / 4
#     if avg >= 80:
#         success += 1
#         print('pass')
#     else:
#         print('fail')

# print(f'Successful : {success}')

# sum 함수를 사용하는 방법
for i in score:
    if (sum(i) / 4) >= 80:
        success += 1
        print('pass')
    else:
        print('fail')

print(f'Successful : {success}')