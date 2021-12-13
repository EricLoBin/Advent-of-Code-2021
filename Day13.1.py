from inputs.input import get_input

inp = get_input(13).read().split("\n\n")

inp[0] = [(int(i.split(",")[0]), int(i.split(",")[1])) for i in inp[0].split("\n")]
inp[1] = [(i.split("=")[0][-1], int(i.split("=")[1])) for i in inp[1].split("\n")]

paper = {}

fold = inp[1][0]
for pos in inp[0]:
    if (fold[0] == "x" and pos[0] > fold[1]):
        pos = (fold[1] - (pos[0] - fold[1]), pos[1])
    if (fold[0] == "y" and pos[1] > fold[1]):
        pos = (pos[0], fold[1] - (pos[1] - fold[1]))
    
    paper[pos] = "@"

print(len(paper))
