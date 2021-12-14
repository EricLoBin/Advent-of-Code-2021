from inputs.input import get_input

inp = get_input(14).read().split("\n\n")

rules = {i[:2]:i[-1] for i in inp[1].split("\n")}

polymer = {}
for i in range(len(inp[0])-1):
    polymer[inp[0][i:i+2]] = polymer[inp[0][i:i+2]] + 1 if polymer.get(inp[0][i:i+2]) else 1

for _ in range(40):
    new_polymer = {}
    for i in polymer:
        new_polymer[i[0]+rules[i]] = new_polymer[i[0]+rules[i]] + polymer[i] if new_polymer.get(i[0]+rules[i]) else polymer[i]
        new_polymer[rules[i]+i[1]] = new_polymer[rules[i]+i[1]] + polymer[i] if new_polymer.get(rules[i]+i[1]) else polymer[i]
    polymer = new_polymer


num = {}

for i in polymer:
    num[i[0]] = num[i[0]] + polymer[i] if num.get(i[0]) else polymer[i]

print((max(num.values()) - min(num.values()))+1)
