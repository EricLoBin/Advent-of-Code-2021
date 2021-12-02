from inputs.input import get_input

inp = get_input(2)

x, y, aim = 0, 0, 0
for move in inp:
    match move[:1]:
        case "u":
            aim -= int(move.split(" ")[1])
        case "d":
            aim += int(move.split(" ")[1])
        case "f":
            x += int(move.split(" ")[1])
            y += aim * int(move.split(" ")[1])

print(x * y)
