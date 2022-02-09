# 오타맨 고창영

for T in range(int(input())):
    num, word = input().split()
    num = int(num)
    print(word[:num-1] + word[num:])