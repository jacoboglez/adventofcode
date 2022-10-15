'''
https://adventofcode.com/2015/day/18
'''
DAY = 18
YEAR = 2015

import sys
sys.path.insert(0, '.')
from utils import *

import numpy as np
from scipy import ndimage


KERNEL = np.array([[1,1,1],[1,0,1],[1,1,1]])


def parse_input(input):
    state = []
    
    for line in input:
        row = []
        for c in line:
            if c == '.':
                row.append(0)
            elif c == '#':
                row.append(1)
            else:
                raise ValueError('Unexpected tile.')

        state.append(row)

    return np.array(state)


def print_state(state):
    bugs = ''
    for row in state:
        for c in row:
            bugs += '#' if c else '.'
        bugs += '\n'

    print(bugs)


def update(state):
    new_state = np.zeros([np.size(state, 0), np.size(state, 0)], dtype = int) 

    adjacents = ndimage.convolve(state, KERNEL, mode='constant', cval=0.0)

    # If the light is on: keep on if 2 or 3 neighbours
    new_state += state & ( (adjacents == 2) | (adjacents == 3) )

    # If the light is on: turn on if 3 neighbours
    new_state += np.logical_not(state) & ( (adjacents == 3) )

    return new_state


def parser(test=False):
    input = Input(DAY, YEAR, test=test)
    state = []
    
    for line in input:
        row = []
        for c in line:
            if c == '.':
                row.append(0)
            elif c == '#':
                row.append(1)
            else:
                raise ValueError('Unexpected tile.')

        state.append(row)

    return np.array(state)


def part1(input, steps=4):
    state = input
    for _ in range(steps):
        state = update(state)

    return np.sum(state)


def part2(input, steps=5):
    state = input
    # Turn on corners
    state[[0,0,-1,-1], [0,-1,0,-1]] = 1

    for _ in range(steps):
        state = update(state)
        state[[0,0,-1,-1], [0,-1,0,-1]] = 1

    return np.sum(state)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input, steps=100)
    print(f'Part 1: {result_1}')

    result_2 = part2(input, steps=100)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [4], part2, [17])
    main()
