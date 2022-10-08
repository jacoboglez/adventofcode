'''
https://adventofcode.com/2017/day/1
'''
DAY = 1

from utils import *


def parser(test=False):
    return Input(DAY, 2017, test=test)[0]


def part1(input):
    sum = 0
    l = len(input)
    for j, i in enumerate(input):
        if i == input[(j+1)%l]:
            sum += int(i)
    return sum


def part2(input):
    sum = 0
    l = len(input)
    for j, i in enumerate(input):
        if i == input[(j+l//2)%l]:
            sum += int(i)
    return sum
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [1+2+1+9], part2, [None, 4])
    main()