# AoC2022 day2
points = 0

with open('input.txt') as f:
    for game in f.read().splitlines():
        if game == "A X": #rock rock
            points += 1 #rock
            points += 3 #tie
        elif game == "A Y": #rock paper
            points += 2 #paper
            points += 6 #win
        elif game == "A Z": #rock scissors
            points += 3 #scissors
        elif game == "B X": #paper rock
            points += 1 #rock
        elif game == "B Y": #paper paper
            points += 2 #paper
            points += 3 #tie
        elif game == "B Z": #paper scissors
            points += 3 #scissors
            points += 6 #win
        elif game == "C X": #scissors rock
            points += 1 #rock
            points += 6 #win
        elif game == "C Y": #scissors paper
            points += 2 #paper
        elif game == "C Z": #scissors scissors
            points += 3 #scissors
            points += 3 #tie
print(points)