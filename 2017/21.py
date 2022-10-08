'''
https://adventofcode.com/2017/day/21
'''
DAY = 21

SEED = '''.#.
..#
###'''


from utils import *


def parser(test=False):
    return Input(DAY, 2017, test=test)


def part1(input):
    pass


def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [], part2, [])
    main()