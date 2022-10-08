'''
https://adventofcode.com/2019/day/11
'''
DAY = 11

from utils import *
from icc import intCodeComputer
from collections import defaultdict, deque

# How to print:
#        0    1
FILL = [' ', '█']
BIG = 9999999999999


def part1(program):
    software = intCodeComputer(program, id=1)

    painted_pannels = set([])
    colors = defaultdict(int)
    position = (0, 0)
    
    #                      UP     RIGHT   DOWN     LEFT 
    directions = deque([ (0, 1), (1, 0), (0, -1), (-1, 0) ])

    while not software.finished:

        # Compute step
        software.inputArray = [colors[position]]
        software.compute()
        # print(software.outputArray)
        out_color, out_direction = software.outputArray[-2:]

        # Paint
        colors[position] = out_color
        painted_pannels.add(position)

        # Update direction
        if out_direction: # Turn right
            directions.rotate(1)
        else: # Turn left
            directions.rotate(-1)

        # Update position
        position = ( position[0] + directions[0][0], position[1] + directions[0][1] )
        


    return len(painted_pannels)


def part2(program):

    software = intCodeComputer(program, id=2)

    painted_pannels = set([])
    colors = defaultdict(int)
    position = (0, 0)
    colors[position] = 1 # Start on a white tile
    
    #                      UP     RIGHT   DOWN     LEFT 
    directions = deque([ (0, 1), (1, 0), (0, -1), (-1, 0) ])

    xmax = -BIG
    xmin = BIG
    ymax = -BIG
    ymin = BIG


    while not software.finished:

        # Update records
        if position[0] > xmax: xmax = position[0]
        if position[0] < xmin: xmin = position[0]
        if position[1] > ymax: ymax = position[1]
        if position[1] < ymin: ymin = position[1]

        # Compute step
        software.inputArray = [colors[position]]
        software.compute()
        # print(software.outputArray)
        out_color, out_direction = software.outputArray[-2:]

        # Paint
        colors[position] = out_color
        painted_pannels.add(position)

        # Update direction
        if out_direction: # Turn right
            directions.rotate(1)
        else: # Turn left
            directions.rotate(-1)

        # Update position
        position = ( position[0] + directions[0][0], position[1] + directions[0][1] )

    # It goes from max to min because I got the answer flipped
    for y in range(ymax, ymin-1, -1):
        line = ''
        for x in range(xmax, xmin-1, -1):
            line += FILL[ colors[(x, y)] ]
        print(line)


def main():
    input = Input(DAY, 2019, line_parser = integers, test=False)
    program = list(input[0])

    print(f'Part 1: {part1(program)}')
    print('')
    print(f'Part 2:')# {part2(program)}')
    part2(program)


if __name__ == "__main__":
    main()