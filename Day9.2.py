from inputs.input import get_input

inp = get_input(9).read()

inp = [[int(j) for j in i] for i in inp.split("\n")]
checked = [[False for j in i] for i in inp]

basin = []

def check(x, y):
    if inp[x][y] == 9: return
    checked[x][y] = True
    if x > 0 and (not checked[x-1][y]): check(x-1, y)
    if x < (len(inp)-1) and (not checked[x+1][y]): check(x+1, y)
    if y > 0 and (not checked[x][y-1]): check(x, y-1)
    if y < (len(inp[0])-1) and (not checked[x][y+1]): check(x, y+1)

for i, line in enumerate(inp):
    line_above = inp[i-1] if i > 0 else None
    line_below = inp[i+1] if i < (len(inp)-1) else None

    for j in range(len(line)):
        before = line[j-1] if j > 0 else None
        after = line[j+1] if j < (len(line)-1) else None
        lower = True

        if (before != None and (before <= line[j])): lower = False
        if (after != None and (after <= line[j])): lower = False
        if (line_above != None and (line_above[j] <= line[j])): lower = False
        if (line_below != None and (line_below[j] <= line[j])): lower = False
        
        if lower: check(i, j)
        value = sum(sum(i) for i in checked)
        if value != 0: basin.append(value)
        checked = [[False for j in i] for i in inp]

basin.sort(reverse=True)
print(basin[0]*basin[1]*basin[2])
