# 별 찍기 - 20

T = int(input())

for i in range(T):
    if i % 2 == 0:
        print('* ' * T)
    else:
        print(' *' * T)
    # 한줄로 쓰는 법
    # print(' *' * T if i % 2 == 0 else ' *' * T)

    # / : 몫을 구하는 법
    # % : 나머지를 구하는 법 (홀수 짝수 구분시 사용)