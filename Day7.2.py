from inputs.input import get_input

inp = [int(i) for i in get_input(7).read().split(",")]

max = max(inp)

fuel = []

def move(distance):
    r = 0
    for i in range(distance + 1):
        r += i
    return r

for i in range(max):
    print(str(round((i/max)*100, 2)) + "%")
    fuel.append(0)
    for j in inp:
        fuel[i] += move(i - j if ((i - j) >= 0) else j - i)

print(min(fuel))
