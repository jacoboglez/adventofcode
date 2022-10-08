'''
https://adventofcode.com/2017/day/6
'''
DAY = 6

from utils import *
from collections import deque


def parser(test=False):
    return deque(Input(DAY, 2017, test=test, line_parser=integers)[0])


def reallocate(banks):

    red_blocks = max(banks)
    rot = -banks.index(red_blocks)
    banks.rotate(rot)
    banks[0] = 0

    banks.rotate(-1)
    rot -= 1

    while red_blocks:
        banks[0] += 1
        red_blocks -= 1
        banks.rotate(-1)
        rot -= 1

    banks.rotate(-rot)
    
    return banks


def part1(input):
    banks = input
    visited = set()
    visited.add(tuple(banks))

    cycles = 0
    while True:
        
        banks = reallocate(banks)
        cycles += 1

        t_banks = tuple(banks)
        if t_banks in visited:
            return cycles, banks

        visited.add(t_banks)
        
    

def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1, rep_config = part1(input)
    print(f'Part 1: {result_1}')

    result_2, _ = part1(rep_config)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, 
        lambda i: part1(i)[0], [5], 
        lambda i: part1(part1(i)[1])[0], [4])
    main()