from inputs.input import get_input

inp = get_input(1)

val = [int(i) for i in inp]
count = 0
for i in range(len(val)):
    if ((i + 3) == len(val)):
        break
    if ((val[i] + val[i+1] + val[i+2]) < (val[i+1] + val[i+2] + val[i+3])):
        count += 1

print(count)
