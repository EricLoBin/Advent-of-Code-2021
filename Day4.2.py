from sys import exit
from inputs.input import get_input

inp = get_input(4).read().split("\n\n")

num = inp[0].split(",")
num = [int(i) for i in num]
cards = inp[1:]

for i in range(len(cards)):
    cards[i] = cards[i].replace("  ", " ").split("\n")
    for j in range(len(cards[i])):
        cards[i][j] = [int(k) for k in cards[i][j].split(" ") if k != ""]

def run():
    for n in num:
        for i, card in enumerate(cards):
            for line in card:
                for col in range(len(line)):
                    if (line[col] == n):
                        line[col] = None
                    if (5 == sum(1 for i in line if i == None) or
                        (card[0][col] == None and card[1][col] == None and card[2][col] == None and card[3][col] == None and card[4][col] == None)
                    ):
                        if (len(cards) == 1): print(sum(sum(j for j in i if j != None) for i in card)*n)
                        return i

while len(cards) > 0:
    cards.pop(run())