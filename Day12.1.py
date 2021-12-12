from collections import defaultdict
from inputs.input import get_input

inp = get_input(12).read().split("\n")

paths = []
positions = defaultdict(list)

for i in inp:
    pos1, pos2 = i.split("-")
    if not (pos2 == "start"):
        positions[pos1].append(pos2)
    if not (pos1 == "start" or pos2 == "end"):
        positions[pos2].append(pos1)


def get_possibilities(path):
    paths = []
    for i in positions[path[-1]]:
        if (i.islower() and path.count(i)):
            continue
        paths.append([j for j in path])
        paths[-1].append(i)
    return paths


for i in positions["start"]:
    paths.append([i])


while sum(True for i in paths if "end" not in i):
    new_paths = []
    for path in paths:
        if (path[-1] == "end"):
            new_paths.append(path)
            continue
        new_paths += get_possibilities(path)
    paths = new_paths

print(len(paths))
