from inputs.input import get_input

inp = get_input(9).read()

inp = [[int(j) for j in i] for i in inp.split("\n")]

risk_level = 0

for i, line in enumerate(inp):
    line_above = inp[i-1] if i > 0 else None
    line_below = inp[i+1] if i < (len(inp)-1) else None

    for j in range(len(line)):
        before = line[j-1] if j > 0 else None
        after = line[j+1] if j < (len(line)-1) else None
        lower = True

        if (before != None and (before <= line[j])): lower = False
        if (after != None and (after <= line[j])): lower = False
        if (line_above != None and (line_above[j] <= line[j])): lower = False
        if (line_below != None and (line_below[j] <= line[j])): lower = False
        
        if lower: risk_level += 1 + line[j]

print(risk_level)
