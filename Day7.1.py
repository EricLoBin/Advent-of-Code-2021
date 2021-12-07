from inputs.input import get_input

inp = [int(i) for i in get_input(7).read().split(",")]

max = max(inp)

fuel = []

for i in range(max):
    fuel.append(0)
    for j in inp:
        fuel[i] += i - j if ((i - j) >= 0) else j - i

print(min(fuel))
