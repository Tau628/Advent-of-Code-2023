#Advent of Code 2023, Day 4, Part 2

output_sum = 0
card_multiplicities = {}

while(True):
    line = input()

    if line.upper() == "END":
        break


    curr_card, allNumbers = line.split(": ")
    _, curr_card = curr_card.split()
    curr_card = int(curr_card)

    if curr_card in card_multiplicities:
        card_multiplicities[curr_card] += 1
    else:
        card_multiplicities[curr_card] = 1
    
    winningNumbers, drawnNumbers = allNumbers.split("|")

    winningNumbers = list(map(int, winningNumbers.split()))
    drawnNumbers = list(map(int, drawnNumbers.split()))

    winningCount = sum([drawnNum in winningNumbers for drawnNum in drawnNumbers])

    newCards = [curr_card+(i+1) for i in range(winningCount)]

    for newCard in newCards:
        if newCard in card_multiplicities:
            card_multiplicities[newCard] += card_multiplicities[curr_card]
        else:
            card_multiplicities[newCard] = card_multiplicities[curr_card]
        
output_sum = sum(card_multiplicities.values())
print(output_sum)
