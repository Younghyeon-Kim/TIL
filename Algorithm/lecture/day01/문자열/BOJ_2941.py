# 크로아티아 알파벳

s = 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
word = input()

for i in s:
    word = word.replace(i, ' ')
print(len(word))