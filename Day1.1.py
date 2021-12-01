from inputs.input import get_input

inp = get_input(1)

count = 0
previous = int(inp.readline())
for i in inp:
    if int(i) > previous:
        count += 1
    previous = int(i)

print(count)
