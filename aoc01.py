# AOC2022 day 1

summa = 0
elves = []

with open('input.txt', 'r+') as f:
    lines = [line[:-1] for line in f]

for line in lines:
    if line == "":
        elves.append(summa)
        summa = 0
    else:
        summa += int(line)

elves.sort(reverse=True)
top3 = sum(elves[:3])
print(top3)