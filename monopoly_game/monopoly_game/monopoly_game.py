import random


class City:

    def __init__(self, name):
        self.name = name
        self.owner = 0
        self.whoIsHere = 0


class Player:

    def __init__(self):
        self.balance = 5000
        self.locate_city = 0


def play(city, player, d1, d2):
    for i in range(2):
        if i == 0:
            player[i].locate_city = (player[i].locate_city + d1) % 10
        elif i == 1:
            player[i].locate_city = (player[i].locate_city + d2) % 10
        city[player[i].locate_city].whoIsHere += i + 1
        if player[i].locate_city == 0:
            continue
        if city[player[i].locate_city].owner == 0:
            city[player[i].locate_city].owner = i + 1
            if player[i].balance > 300:
                player[i].balance -= 300
        elif city[player[i].locate_city].owner == 1:
            if i == 1:
                player[1].balance -= 600
                player[0].balance += 600
        elif city[player[i].locate_city].owner == 2:
            if i == 0:
                player[0].balance -= 600
                player[1].balance += 600


def print_map(city):

    clen = []
    for i in range(10):
        clen.append(len(city[i].name))
    for i in range(5):
        print(" ----------------", end="\t")
    print()
    for i in range(5):
        print("|                |", end="\t")
    print()
    for i in range(5):
        if i == 0:
            print("|      %s  " % city[i].name, end="")
            for j in range(8-clen[i]):
                print(" ", end="")
            print("|", end="\t")
        else:
            print("|    %s : %d" % (city[i].name, city[i].owner), end="")
            for j in range(8-clen[i]):
                print(" ", end="")
            print("|", end="\t")
    print()

    for i in range(5):
        if city[i].whoIsHere == 0:
            print("|       ( )      |", end="\t")
        elif city[i].whoIsHere == 1:
            print("|       (1)      |", end="\t")
        elif city[i].whoIsHere == 2:
            print("|       (2)      |", end="\t")
        elif city[i].whoIsHere == 3:
            print("|     (1, 2)     |", end="\t")
    print()
    for i in range(5):
        print(" ----------------", end="\t")
    print()
    print("        ^        ", end="\t")
    for i in range(3):
        print("                ", end="\t")
    print("                 |")
    print("        |        ", end="\t")

    for i in range(3):
        print("                ", end="\t")
    print("                 v")

    for i in range(5):
        print(" ----------------", end="\t")
    print()
    for i in range(5):\
        print("|                |", end="\t")
    print()
    for i in range(9, 4, -1):
        print("|  %s : %d" % (city[i].name, city[i].owner), end="")
        for j in range(10-clen[i]):
            print(" ", end="")
        print("|", end="\t")
    print()
    for i in range(9, 4, -1):
        if city[i].whoIsHere == 0:
            print("|       ( )      |", end="\t")
        elif city[i].whoIsHere == 1:
            print("|       (1)      |", end="\t")
        elif city[i].whoIsHere == 2:
            print("|       (2)      |", end="\t")
        elif city[i].whoIsHere == 3:
            print("|     (1, 2)     |", end="\t")
    print()
    for i in range(5):
        print(" ----------------", end="\t")
    print()


cities = [City("Start"), City("Seoul"), City("Tokyo"), City("Sydney"), City("LA"), City("Cairo"), City("Phuket"),
          City("New Delhi"), City("Hanoi"), City("Paris")]

players = [Player(), Player()]

for i in range(0, 30):
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    print(" Turn %d" % (i + 1))
    play(cities, players, dice1, dice2)
    print_map(cities)

    cities[players[0].locate_city].whoIsHere = 0
    cities[players[1].locate_city].whoIsHere = 0

    print("player 1 잔고 :  %d, player 2 잔고 : %d" % (players[0].balance, players[1].balance))
    print("player 1 주사위 :  %d, player 2 주사위 : %d" % (dice1, dice2))

    if players[0].balance < 0:
        print("player 1이 파산하였습니다.")
        break
    elif players[1].balance < 0:
        print("player 2가 파산하였습니다.")
        break
    if i == 29:
        if players[0].balance > players[1].balance:
            print("player 1이 이겼습니다.")
        elif players[0].balance < players[1].balance:
            print("player 2가 이겼습니다.")
        elif players[0].balance == players[1].balance:
            printf("무승부")

