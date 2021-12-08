from inputs.input import get_input

inp = get_input(8).read().split("\n")

inp = [[j for j in i[61:].split(" ")] for i in inp]

# 1 = 2 segments
# 7 = 3 segments
# 4 = 4 segments
# 8 = 7 segments

num = {
    1: 0,
    7: 0,
    4: 0,
    8: 0
}

for i in inp:
    for j in i:
        match len(j):
            case 2:
                num[1] += 1
            case 3:
                num[7] += 1
            case 4:
                num[4] += 1
            case 7:
                num[8] += 1

print(sum(num.values()))
