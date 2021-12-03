from inputs.input import get_input

inp = get_input(3)
lines = sum(1 for i in get_input(3))

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in inp:
    for i, char in enumerate(line):
        if (char != "\n"):
            arr[i] += int(char)

gamma = ""
epsilon = ""
for i in arr:
    if i > (lines/2):
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

print(int(gamma, 2)* int(epsilon, 2))