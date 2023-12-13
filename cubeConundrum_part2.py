#Advent of Code 2023, Day 2, Part 2

from math import prod

output_sum = 0

while(True):
    line = input()

    if line.upper() == "END":
        break

    game_mins = {'red':0, 'blue': 0, 'green': 0}
    
    game, line = line.split(": ")

    _, game = game.split()
    game = int(game)

    grabs = line.split("; ")
    grabs = [{color:int(num) for num, color in map(lambda x: x.split(), grabs.split(", "))} for grabs in grabs]


    for grab in grabs:
        for color in game_mins.keys():
            if color in grab and grab[color] > game_mins[color]:
                game_mins[color] = grab[color]

    output_sum += prod(game_mins.values())
