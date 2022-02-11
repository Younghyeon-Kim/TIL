foul = list(input().split())
players = {}

for i in foul:
    players[i] = foul.count(i)

for k in players.keys():
    if players[k] == min(players.values()):
        print(k)

print(min(players.values()))