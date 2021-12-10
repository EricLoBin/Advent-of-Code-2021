from inputs.input import get_input

inp = get_input(10).read().split("\n")

score = 0

for line in inp:
    for _ in line:
        line = line.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")
    for i in line:
        match i:
            case ")":
                score += 3
                break
            case "]":
                score += 57
                break
            case "}":
                score += 1197
                break
            case ">":
                score += 25137
                break

print(score)
