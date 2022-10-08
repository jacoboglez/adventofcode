'''
Report Repair
https://adventofcode.com/2020/day/1
'''
DAY = 1

from utils import *


TARGET = 2020


def parser(test=False):
    return [i[0] for i in Input(DAY, 2020, integers, test=test)]


def part1(input):
    for i, a in enumerate(input):
        for b in input[i:]:
            if a + b == TARGET:
                return a*b


def part2(input):
    for ia, a in enumerate(input):
        for ib, b in enumerate(input[ia:], ia):
            if a + b >= TARGET:
                continue
            for ic, c in enumerate(input[ib:], ib):
                if a + b + c == TARGET:
                    return a*b*c


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [514579], part2, [241861950])
    main()