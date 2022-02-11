# 딕셔너리 만들기
animation = {
    "Pokemon" : "Pikachu",
    "Digimon" : "Agumon",
    "Yugioh" : "Black Magician"
}

word = input()

# 세 개중에 있으면 value / 없으면 i don't know
if word in animation:
    print(animation[word])
else:
    print("I don't know")

# 한줄로 요약 가능
# print(animation.get(word, "I don't know"))