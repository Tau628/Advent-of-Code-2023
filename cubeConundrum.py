#Advent of Code 2023, Day 3, Part 1

import re

grid = []
output_sum = 0

while(True):
    line = input()

    if line.upper() == "END":
        break

    grid.append(line)

HEIGHT = len(grid)
WIDTH = len(grid[0])


re_number = re.compile(r"\d+")
re_symbol = re.compile(r"[^.\d]")
for nRow, rowstring in enumerate(grid):

    my_numbers = re_number.finditer(rowstring)

    for number in my_numbers:

        xmin, xmax = number.span()
        xmin = max(0, xmin-1)
        xmax = min(xmax, WIDTH-1)

        ymin = max(0, nRow-1)
        ymax = min(nRow+1, HEIGHT-1)

        symbol_search = ''.join([row[xmin:xmax+1] for row in grid[ymin:ymax+1]])
        
        my_match = re_symbol.search(symbol_search) is not None

        print(f"{number.group(0)}: ({xmin}, {ymin}); ({xmax}, {ymax})\t {my_match}")

        if my_match:
            output_sum += int(number.group(0))
