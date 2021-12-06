from inputs.input import get_input

inp = [int(i) for i in get_input(6).read().split(",")]

for i in range(80):
    for j in range(len(inp)):
        inp[j] -= 1
        if (inp[j] == -1):
            inp[j] = 6
            inp.append(8)

print(len(inp))
