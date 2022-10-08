'''
https://adventofcode.com/2017/day/2
'''
DAY = 2

from utils import *


def parser(test=False):
    return Input(DAY, 2017, test=test, line_parser=integers)


def part1(input):
    sum = 0
    for row in input:
        sum += max(row) - min(row)

    return sum


def part2(input):
    sum = 0
    for row in input:
        for i in row:
            for j in row:
                if i == j:
                    continue
                if i%j == 0:
                    sum += i // j

    return sum
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [18], part2, [None, 9])
    main()