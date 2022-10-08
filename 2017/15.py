'''
https://adventofcode.com/2017/day/15
'''
DAY = 15

FACTOR_A = 16807
FACTOR_B = 48271
DIVISOR = 2147483647

from utils import *


def parser(test=False):
    return [i[0] for i in Input(DAY, 2017, test=test, line_parser=integers)]


def generator(factor, starting_value):
    previous_value = starting_value
    while True:
        next_value = (previous_value * factor) % DIVISOR
        previous_value = next_value
        yield next_value


def part1(input):
    generator_A = generator(FACTOR_A, input[0])
    generator_B = generator(FACTOR_B, input[1])
    counter = 0
    for _ in range(40_000_000):
        lowest_bin_A = bin(next(generator_A))[-16:]
        lowest_bin_B = bin(next(generator_B))[-16:]
        if lowest_bin_A == lowest_bin_B:
            counter += 1

    return counter


def generator2(factor, starting_value, mult):
    previous_value = starting_value
    while True:
        next_value = (previous_value * factor) % DIVISOR
        previous_value = next_value
        if next_value % mult == 0:
            yield next_value


def part2(input):
    generator_A = generator2(FACTOR_A, input[0], 4)
    generator_B = generator2(FACTOR_B, input[1], 8)
    counter = 0
    for _ in range(5_000_000):
        lowest_bin_A = bin(next(generator_A))[-16:]
        lowest_bin_B = bin(next(generator_B))[-16:]
        if lowest_bin_A == lowest_bin_B:
            counter += 1

    return counter
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [588], part2, [309])
    main()