#Advent of Code 2023, Day 4, Part 1

output_sum = 0

while(True):
    line = input()

    if line.upper() == "END":
        break


    _, allNumbers = line.split(": ")
    winningNumbers, drawnNumbers = allNumbers.split("|")

    winningNumbers = list(map(int, winningNumbers.split()))
    drawnNumbers = list(map(int, drawnNumbers.split()))

    winningCount = sum([drawnNum in winningNumbers for drawnNum in drawnNumbers])
    if winningCount:
        output_sum += 2**(winningCount-1)

print(output_sum)
