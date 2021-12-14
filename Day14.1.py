from inputs.input import get_input

inp = get_input(14).read().split("\n\n")

rules = [i[:1]+i[-1]+i[1:2] for i in inp[1].split("\n")]

polymer = inp[0]

for _ in range(10):
    polymer = "*".join(polymer)
    for rule in rules:
        polymer = polymer.replace(rule[0]+"*"+rule[2], rule)
        polymer = polymer.replace(rule[0]+"*"+rule[2], rule)

num = {}

for i in polymer:
    num[i] = (num[i] + 1) if num.get(i) else 1

print(max(num.values()) - min(num.values()))
