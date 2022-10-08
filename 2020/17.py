'''
https://adventofcode.com/2020/day/17
'''
DAY = 17

from utils import *
import numpy as np
from scipy import ndimage


BOOT_PROCESS = 6
KERNEL3 = np.pad([[[0]]], 1, 'constant', constant_values=1 )
KERNEL4 = np.pad([[[[0]]]], 1, 'constant', constant_values=1 )


def parser(test=False):
    input_raw = Input(DAY, 2020, test=test)
    cubes = []
    for line in input_raw:
        cubes.append( [1 if c == "#" else 0 for c in line] )

    return cubes


def update(state, KERNEL=KERNEL3):
    '''You could make use of the fact that the solution is symmetric with respect to the original slice.
    Since the performance is fine and the code is clear I decided to not implement that.'''
    padded_state = np.pad(state, 1, 'constant', constant_values=0 )
    adjacents = ndimage.convolve(padded_state, KERNEL, mode='constant', cval=0)

    new_state = (adjacents == 3) + ((adjacents == 2) & padded_state)
    return new_state


def part1(input):
    state = np.array([input])
    
    for t in range(BOOT_PROCESS):
        state = update(state)

    return np.sum(state)


def part2(input):
    state = np.array([[input]])
    
    for t in range(BOOT_PROCESS):
        state = update(state, KERNEL4)

    return np.sum(state)


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [112], part2, [848])
    main()