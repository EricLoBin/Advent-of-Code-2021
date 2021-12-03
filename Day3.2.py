from inputs.input import get_input

inp = [line for line in get_input(3)]
lines = sum(1 for i in inp)

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def scan(inp):
    global arr
    global lines
    lines = sum(1 for i in inp)
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in inp:
        for i, char in enumerate(line):
            if (char != "\n"):
                arr[i] += int(char)

oxygen_generator = [i for i in inp]
for i in range(len(inp[0])-1):
    scan(oxygen_generator)
    oxygen_generator = [j for j in oxygen_generator if j[i] == ("1" if (arr[i] == lines/2) else ("1" if arr[i] > lines/2 else "0")) ]
    if (len(oxygen_generator) == 1):
        break
oxygen_generator = int(oxygen_generator[0], 2)

CO2_scrubber = [i for i in inp]
for i in range(len(inp[0])-1):
    scan(CO2_scrubber)
    CO2_scrubber = [j for j in CO2_scrubber if j[i] == ("0" if (arr[i] == lines/2) else ("1" if arr[i] < lines/2 else "0")) ]
    if (len(CO2_scrubber) == 1):
        break
CO2_scrubber = int(CO2_scrubber[0], 2)

print(oxygen_generator*CO2_scrubber)