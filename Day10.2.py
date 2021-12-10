from inputs.input import get_input

inp = get_input(10).read().split("\n")

score = []

for line in inp:
    s = 0
    for _ in line:
        line = line.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")
    if (line.count(")")+line.count("]")+line.count("}")+line.count(">")):
        continue
    for j in reversed(line):
        s *= 5
        match j:
            case "(":
                s += 1
            case "[":
                s += 2
            case "{":
                s += 3
            case "<":
                s += 4
    score.append(s)

print(sorted(score)[int((len(score))/2)])
