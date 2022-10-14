'''
https://adventofcode.com/2015/day/17
'''
DAY = 17
YEAR = 2015

import sys
sys.path.insert(0, '.')

from utils import *


def parser(test=False):
    return sorted([i[0] for i in Input(DAY, YEAR, line_parser=integers, test=test)], reverse=True)


def distribute(containers, eggnog):
    counter = 0
    remaining_containers = containers.copy()
    for c in containers:
        if (eggnog > c):
            remaining_containers.remove(c)
            counter += distribute(remaining_containers, eggnog-c)
        elif eggnog == c:
            counter += 1
    return counter


def distribute_min(containers, eggnog, used_cont=0):
    list_containers = []
    remaining_containers = containers.copy()
    for c in containers:
        if (eggnog > c):
            remaining_containers.remove(c)
            lc = distribute_min(remaining_containers, eggnog-c, used_cont+1)
            list_containers.extend(lc)
        elif eggnog == c:
            list_containers.append(used_cont+1)
    return list_containers


def part1(containers, eggnog=25):
    return distribute(containers, eggnog)


def part2(containers, eggnog=25):
    list_containers = distribute_min(containers, eggnog)
    cm = min(list_containers)
    return list_containers.count(cm)


def main():
    input = parser()
    print('RESULTS')

    eggnog = 150
    result_1 = part1(input, eggnog)
    print(f'Part 1: {result_1}')

    result_2 = part2(input, eggnog)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [4], part2, [3])
    main()
