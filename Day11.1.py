from inputs.input import get_input

inp = [[int(j) for j in i] for i in get_input(11).read().split("\n")]

flashes = 0

def flash(y, x):
    if (inp[y][x] == None or inp[y][x] <= 9):
        return
    inp[y][x] = None
    global flashes
    flashes += 1
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (0 > i or i > len(inp[0])-1 or 0 > j or j > len(inp[0])-1):
                continue
            if (inp[i][j] == None):
                continue
            inp[i][j] += 1
            flash(i, j)

def step():
    for line in inp:
        for i in range(len(line)):
            line[i] += 1
    
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            flash(y, x)
    
    for i in inp:
        for j in range(len(i)):
            if i[j] == None:
                i[j] = 0


for _ in range(100):
    step()
print(flashes)
