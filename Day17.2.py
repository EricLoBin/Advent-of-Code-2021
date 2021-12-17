from inputs.input import get_input

inp = get_input(17).read()[13:].split(", ")

target_area = {
    "x": [
        int(inp[0].split("..")[0][2:]),
        int(inp[0].split("..")[1])
    ],
    "y": [
        int(inp[1].split("..")[0][2:]),
        int(inp[1].split("..")[1])
    ]
}


def move(xv, yv):
    x, y = 0, 0
    highest_y = 0

    while True:
        # increase position by its velocity
        x += xv
        y += yv

        # change the velocity
        if xv != 0: xv += -1 if (xv > 0) else 1
        yv -= 1

        if (
            target_area["x"][0] <= x <= target_area["x"][1] and
            target_area["y"][0] <= y <= target_area["y"][1]
            ):
            return True

        if (
            (x > target_area["x"][1]) or
            (y < target_area["y"][0])
            ):
            return False


successful = 0

for xv in range(0, 200):
    for yv in range(-200, 200):
        res = move(xv, yv)
        if (res):
            successful += 1

print(successful)
