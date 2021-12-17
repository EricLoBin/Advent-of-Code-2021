from inputs.input import get_input

inp = [[int(j) for j in i] for i in get_input(15).read().split("\n")]

cave = []
for i in range(5):
    for line in inp:
        cave.append([j+i for j in line] + [j+1+i for j in line] + [j+2+i for j in line] + [j+3+i for j in line] + [j+4+i for j in line])

for line in cave:
    for i in range(len(cave)):
        if (line[i] > 9): line[i] -= 9


points = {(0, 0): 0}
risk_lowest_in_end = float('inf')

while True:
    new_points = {}

    for point, risk in points.items():
        x, y = point

        if (risk > risk_lowest_in_end):
            continue

        if ((y == (len(cave)-1)) and (x == (len(cave[0])-1))):
            new_points[point] = risk
            risk_lowest_in_end = risk
            continue

        if (y+1 < len(cave)):
            if ((x, y+1) not in new_points):
                new_points[(x, y+1)] = (risk+cave[x][y+1])
            elif ((new_points.get((x, y+1))) > (risk+cave[x][y+1])):
                new_points[(x, y+1)] = (risk+cave[x][y+1])

        if (x+1 < len(cave[0])):
            if ((x+1, y) not in new_points):
                new_points[(x+1, y)] = (risk+cave[x+1][y])
            elif ((new_points.get((x+1, y))) > (risk+cave[x+1][y])):
                new_points[(x+1, y)] = (risk+cave[x+1][y])

        if (y-1 > 0):
            if ((x, y-1) not in new_points):
                new_points[(x, y-1)] = (risk+cave[x][y-1])
            elif ((new_points.get((x, y-1))) > (risk+cave[x][y-1])):
                new_points[(x, y-1)] = (risk+cave[x][y-1])

        if (x-1 > 0):
            if ((x-1, y) not in new_points):
                new_points[(x-1, y)] = (risk+cave[x-1][y])
            elif ((new_points.get((x-1, y))) > (risk+cave[x-1][y])):
                new_points[(x-1, y)] = (risk+cave[x-1][y])

    points = new_points
    print(min(new_points.values()), len(new_points.values()))
