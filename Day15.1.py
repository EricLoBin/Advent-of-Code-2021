from inputs.input import get_input

inp = [[int(j) for j in i] for i in get_input(15).read().split("\n")]


points = {(0, 0): 0}
risk_lowest_in_end = float('inf')

while True:
    new_points = {}

    for point, risk in points.items():
        x, y = point

        if (risk > risk_lowest_in_end):
            continue

        if ((y == (len(inp)-1)) and (x == (len(inp[0])-1))):
            new_points[point] = risk
            risk_lowest_in_end = risk
            continue

        if (y+1 < len(inp)):
            if ((x, y+1) not in new_points):
                new_points[(x, y+1)] = (risk+inp[x][y+1])
            elif ((new_points.get((x, y+1))) > (risk+inp[x][y+1])):
                new_points[(x, y+1)] = (risk+inp[x][y+1])

        if (x+1 < len(inp[0])):
            if ((x+1, y) not in new_points):
                new_points[(x+1, y)] = (risk+inp[x+1][y])
            elif ((new_points.get((x+1, y))) > (risk+inp[x+1][y])):
                new_points[(x+1, y)] = (risk+inp[x+1][y])

    points = new_points
    print(min(new_points.values()), len(new_points.values()))
