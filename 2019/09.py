'''
https://adventofcode.com/2019/day/9
'''
DAY = 9

from utils import *
from icc import intCodeComputer


def part1(program):
    part1 = intCodeComputer(program, id=1, inptArr=[1])
    part1.compute()

    return part1.outputArray[0]


def part2(program):
    part2 = intCodeComputer(program, id=2, inptArr=[2])
    part2.compute()

    return part2.outputArray[0]


def main():
    input = Input(DAY, 2019, line_parser = integers, test=False)
    program = list(input[0])

    print(f'Part 1: {part1(program)}')
    print(f'Part 2: {part2(program)}')


if __name__ == "__main__":
    main()