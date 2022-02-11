# 나무 조각
pieces = list(map(int, input().split()))

while True:
    for i in range(len(pieces) - 1):
        if pieces[i] > pieces[i+1]:
            temp = pieces[i]
            pieces[i] = pieces[i+1]
            pieces[i+1] = temp
            print(' '.join(map(str, pieces)))
    
    if pieces == [1, 2, 3, 4, 5] : break
