'''
https://adventofcode.com/2020/day/10
'''
DAY = 10

from utils import *


MEMO = {}


def parser(test=False):
    return sorted([int(i) for i in Input(DAY, 2020, test=test)])


def part1(input):
    differences = [0, 0, 0, 0]

    current_jolt = 0
    for jolt in input:
        current_diff = jolt - current_jolt
        current_jolt = jolt
        differences[current_diff] += 1

    # The adapter is always 3 jolts higher, so the final difference is 3
    differences[3] += 1
    return differences[1] * differences[3]


def memoize(f):
    def helper(x, input):
        if x not in MEMO:            
            MEMO[x] = f(x, input)
        return MEMO[x]
    return helper


@memoize
def combinations_from(x, input):
    if x == max(input):
        return 1

    combinations = 0
    for y in range(x+1, x+4):
        if y in input:
            combinations += combinations_from(y, input)
    return combinations


def part2(input):
    MEMO.clear()
    return combinations_from(0, input)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [35, 220], part2, [8, 19208])
    main()