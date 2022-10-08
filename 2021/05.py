'''
https://adventofcode.com/2021/day/5
'''
DAY = 5


from utils import *
from collections import defaultdict
from itertools import product


def parser(test=False):
    return Input(DAY, 2021, test=test, line_parser=integers)


def count_overlaps(grid):
    counter = 0
    for v in grid.values():
        if v > 1: 
            counter += 1

    return counter


def line_range(x1, y1, x2, y2):
    if x1 == x2:
        step_y = (y2-y1)//abs(y2-y1) # Account for decreasing range
        return product([x1], range(y1, y2+step_y, step_y))
    
    if y1 == y2:
        step_x = (x2-x1)//abs(x2-x1) # Account for decreasing range
        return product(range(x1, x2+step_x, step_x), [y1])

    step_x = (x2-x1)//abs(x2-x1)
    step_y = (y2-y1)//abs(y2-y1)
    return zip(range(x1, x2+step_x, step_x), range(y1, y2+step_y, step_y))


def part1(input):
    grid = defaultdict(int)

    for x1, y1, x2, y2 in input:
        if (x1 == x2) or (y1 == y2):
            for p in line_range(x1, y1, x2, y2):
                grid[p] += 1

    return count_overlaps(grid)


def part2(input):
    grid = defaultdict(int)

    for x1, y1, x2, y2 in input:
        for p in line_range(x1, y1, x2, y2):
            grid[p] += 1
    
    return count_overlaps(grid)


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [5], part2, [12])
    main()