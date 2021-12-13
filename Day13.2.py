from inputs.input import get_input

inp = get_input(13).read().split("\n\n")

inp[0] = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in inp[0].split("\n")]
inp[1] = [(i.split("=")[0][-1], int(i.split("=")[1])) for i in inp[1].split("\n")]

paper = {}

def fold(fold_position, positions):
    paper = {}
    for pos in positions:
        if (fold_position[0] == "x" and pos[0] > fold_position[1]):
            pos = (fold_position[1] - (pos[0] - fold_position[1]), pos[1])
        if (fold_position[0] == "y" and pos[1] > fold_position[1]):
            pos = (pos[0], fold_position[1] - (pos[1] - fold_position[1]))
        
        paper[pos] = "@"
    return paper

paper = inp[0]

for i in inp[1]:
    paper = fold(i, paper)

max_x = 0
max_y = 0
for i in paper:
    if i[0] > max_x:
        max_x = i[0]
    if i[1] > max_y:
        max_y = i[1]

for i in range(max_y+2):
    for j in range(max_x+2):
        print(paper[(j, i)] if paper.get((j, i)) else " ", end="")
    print()
