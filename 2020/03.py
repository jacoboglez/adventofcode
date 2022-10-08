'''
https://adventofcode.com/2020/day/3
'''
DAY = 3

from utils import *


SLOPES = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]


def parser(test=False):
    return Input(DAY, 2020, test=test)


def part1(input, slope=SLOPES[1]):
    # input[r][c] gives the value of the r row an c column
    width = len(input[0])
    height = len(input)

    r = 0
    c = 0
    trees = 0
    while r < height:
        if input[r][c] == '#':
            trees += 1
        
        r += slope[0]
        c += slope[1]
        c = c % width # To wrap around when we finish the input

    return trees


def part2(input):
    trees = 1
    for slope in SLOPES:
        trees *= part1(input, slope)

    return trees


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [7], part2, [336])
    main()