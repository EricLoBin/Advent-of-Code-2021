from inputs.input import get_input

inp = get_input(2)

x, y = 0, 0
for move in inp:
    match move[:1]:
        case "u":
            y -= int(move.split(" ")[1])
        case "d":
            y += int(move.split(" ")[1])
        case "f":
            x += int(move.split(" ")[1])

print(x * y)
