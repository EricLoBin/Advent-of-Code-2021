from inputs.input import get_input

inp = get_input(8).read().split("\n")

inp = [[j for j in i.split(" ")] for i in inp]

# 1 = 2 segments
# 7 = 3 segments
# 4 = 4 segments
# 8 = 7 segments

result = 0

for i in inp:
    num = {
        0: None, # 6 segments
        1: None, # 2 segments #####
        2: None, # 5 segments
        3: None, # 5 segments
        4: None, # 4 segments #####
        5: None, # 5 segments
        6: None, # 6 segments
        7: None, # 3 segments #####
        8: None, # 7 segments #####
        9: None  # 6 segments
    }

    for j in i:
        match len(j):
            case 2:
                num[1] = j
            case 3:
                num[7] = j
            case 4:
                num[4] = j
            case 7:
                num[8] = j
            case 1:
                break

    for j in i[:10]:
        j_minus = num[4].translate({ord(i): None for i in j})
        if len(j_minus) == 1:
            if len(j) == 6:
                j_minus = num[1].translate({ord(i): None for i in j})
                if len(j_minus) == 0:
                    num[0] = j # 0
                else:
                    num[6] = j # 6
            else:
                j_minus = num[1].translate({ord(i): None for i in j})
                if len(j_minus) == 0:
                    num[3] = j # 3
                else:
                    num[5] = j # 5
        elif (len(j_minus) == 0) and (j != num[4] and j != num[8]):
            num[9] = j # 9
        else:
            j_minus = j.translate({ord(i): None for i in num[4]})
            if (len(j_minus) == 3) and (j != num[8]):
                num[2] = j # 2

    for j in num:
        num[j] = "".join(sorted(num[j]))

    number = ""
    for j, numb in enumerate(i[11:]):
        number += str(list(num.keys())[list(num.values()).index("".join(sorted(numb)))])

    result += int(number)


print(result)
