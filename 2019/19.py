'''
https://adventofcode.com/2019/day/19
'''
DAY = 19

from utils import *
from icc import intCodeComputer
from itertools import count


SANTA_X = 100
SANTA_Y = 100


def get_beam(program, coordinates):
    software = intCodeComputer(program, id=1, verbose=False)
    software.inputArray = coordinates
    software.compute()

    return software.outputArray[0]


def part1(program, show_beam = False):
    '''Bruteforce the question'''
    points_affected = 0
    for y in range(50):
        line = f'{y}'
        for x in range(50):
            coordinates = [x, y]
            affected = get_beam(program, coordinates)
            points_affected += affected
            if affected:
                line += '#'
            else:
                line += '.'
        if show_beam: print(line)

    return points_affected

 
def part2(program):
    # Start after the initial transient
    y = 11
    x_start = 0
    x_end = 6
    while True: # for y in range(0, infty):
        # Update the y
        y += 1
        # print(f'y: {y}') # See where we are

        # Check where the beam starts 
        affected = 0
        while not affected:
            affected = get_beam(program, [x_start, y])
            x_start += 1
        x_start -= 1# We added one extra regardless of the affected
        # We know where it starts at that y

        # Check where the beam ends
        affected = 1
        while affected: # We stop when the beam stops
            affected = get_beam(program, [x_end, y])
            x_end += 1
        x_end -= 2 # We added one extra and counted the not-beam tile
        # We know where it starts at that x
        
        # Check if it would fit in that stripe
        if (x_end - x_start) < SANTA_X:
            # It wouldn't fit
            # print(f'{x_start}:{x_end}')
            continue

        # Check if it fits in y
        y_santa_end = y + SANTA_Y -1
        x_start_santa = x_end - SANTA_X + 1
        affected = get_beam(program, [x_start_santa, y_santa_end])
        if affected:
            # It fits
            return x_start_santa*10000 + y
        

def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])
    
    result_1 = part1(program)
    print(f'Part 1: {result_1}')

    print('')
    result_2 = part2(program)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()