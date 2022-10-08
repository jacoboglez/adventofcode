'''
https://adventofcode.com/2017/day/5
'''
DAY = 5

from utils import *


def parser(test=False):
    return [i[0] for i in Input(DAY, 2017, test=test, line_parser=integers)]


def part1(input):
    ex = len(input)

    current = 0
    steps = 0
    while current < ex:
        steps += 1
        jump = input[current]
        input[current] += 1

        current += jump

    return steps

def part2(input):
    ex = len(input)

    current = 0
    steps = 0
    while current < ex:
        steps += 1
        jump = input[current]

        if input[current] >= 3:
            input[current] -= 1
        else:
            input[current] += 1

        current += jump

    return steps
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    # Use the original input, not the mutated one
    result_2 = part2(parser())  
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [5], part2, [10])
    main()