#Advent of Code 2023, Day 3, Part 2

import re
from math import prod

grid = []
output_sum = 0

while(True):
    line = input()

    if line.upper() == "END":
        break

    grid.append(line)

HEIGHT = len(grid)
WIDTH = len(grid[0])
GEAR_RANGE = {2, 3, 4, 10, 11, 12, 18, 19, 20}

re_number = re.compile(r"\d+")
re_gear = re.compile(r"\*")
for nRow, rowstring in enumerate(grid):

    my_gears = re_gear.finditer(rowstring)

    for gear in my_gears:

        xmiddle = gear.start()
        xmin = max(0, xmiddle-1)
        xmax = min(xmiddle+1, WIDTH-1)

        ymin = max(0, nRow-1)
        ymax = min(nRow+1, HEIGHT-1)

        search_string = '\n'.join([row[xmin:xmax+1] for row in grid[ymin:ymax+1]])
        gear_numbers = re_number.finditer(search_string)

        close_number = len(list(gear_numbers))

        xmin = max(0, xmiddle-3)
        xmax = min(xmiddle+3, WIDTH-1)

        search_string = '\n'.join([row[xmin:xmax+1] for row in grid[ymin:ymax+1]])
        gear_numbers = re_number.finditer(search_string)

        gear_numbers = list(gear_numbers)
        far_number = len(gear_numbers)

        if close_number == 2:
            if far_number == 2:
                
                output_sum += prod([int(n.group(0)) for n in gear_numbers])
            else:
                valid_numbs = []
                for gear_num in gear_numbers:
                    num_range = set(range(gear_num.start(), gear_num.end()))
                    if num_range & GEAR_RANGE != set():
                        valid_numbs.append(int(gear_num.group(0)))
                if len(valid_numbs) == 2:
                    output_sum += prod(valid_numbs)
                else:
                    print('hey')
        
        
