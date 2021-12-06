from inputs.input import get_input

inp = [int(i) for i in get_input(6).read().split(",")]

fishes = [0 for i in range(9)]

for i in inp:
    fishes[i] += 1

for i in range(256):
    tmp = fishes[0]
    fishes = fishes[1:]
    fishes[6] += tmp
    fishes.append(tmp)

print(sum(fish for fish in fishes))
