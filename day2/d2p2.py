# AoC2022 day2 part2
points = 0

# x lose
# y tie
# z win

with open('input.txt') as f:
    for game in f.read().splitlines():
        if game == "A X": #rock lose
            points += 3 #scissors
        elif game == "A Y": #rock tie
            points += 1 #rock
            points += 3 #tie
        elif game == "A Z": #rock win
            points += 2 #paper
            points += 6 #win
        elif game == "B X": #paper lose
            points += 1 #rock
        elif game == "B Y": #paper tie
            points += 2 #paper
            points += 3 #tie
        elif game == "B Z": #paper win
            points += 3 #scissors
            points += 6 #win
        elif game == "C X": #scissors lose
            points += 2 #paper
        elif game == "C Y": #scissors tie
            points += 3 #scissors
            points += 3 #tie
        elif game == "C Z": #scissors win
            points += 1 #rock
            points += 6 #win
print(points)