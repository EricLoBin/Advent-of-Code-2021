from inputs.input import get_input

inp = get_input(5).read()

inp = inp.split("\n")
for i in range(len(inp)):
    inp[i] = [[int(k) for k in j.split(",")] for j in (inp[i].split(" -> "))]

ar = [[0 for i in range(1000)] for j in range(1000)]


for line in inp:
    if (line[0][0] == line[1][0]):
        for i in range(line[0][1], line[1][1]-1 if line[0][1] > line[1][1] else line[1][1]+1, -1 if line[0][1] > line[1][1] else 1):
            ar[i][line[0][0]] += 1
    elif (line[0][1] == line[1][1]):
        for i in range(line[0][0], line[1][0]-1 if line[0][0] > line[1][0] else line[1][0]+1, -1 if line[0][0] > line[1][0] else 1):
            ar[line[0][1]][i] += 1

count = sum(sum(1 for i in line if i > 1) for line in ar)

print(count)