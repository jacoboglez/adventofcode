'''
https://adventofcode.com/2020/day/9
'''
DAY = 9

from utils import *


PREAMBLE = 25
MEMORY = {}


def parser(test=False):
    return [i[0] for i in Input(DAY, 2020, integers, test=test)]


def find_sum(expected, previous, index):
    if expected in MEMORY:
        if MEMORY[expected] > (index - PREAMBLE):
            return True

    for i, a in enumerate(previous):
        if a > expected:
            continue
        for j, b in enumerate(previous[i:]):
            if a + b == expected:
                MEMORY[expected] = index - PREAMBLE + min(i, j)
                return True

    return False


def part1(input):
    index = PREAMBLE

    while True:
        actual = input[index]
        if not find_sum(actual, input[index-PREAMBLE:index], index):
            return actual
        index += 1


def part2(input):
    weak = part1(input)

    start = 0
    finish = 2
    while True:
        current_sum = sum(input[start:finish])

        if current_sum < weak:
            finish += 1
        elif current_sum > weak:
            start += 1
        else:
            # Found the correct sum
            break

    # Compute the problem solution
    return min(input[start:finish]) + max(input[start:finish])
  

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    PREAMBLE = 5
    test(DAY, parser, part1, [127], part2, [62])

    PREAMBLE = 25
    main()