'''
https://adventofcode.com/2020/day/7
'''
DAY = 7

from utils import *
from collections import defaultdict
import re


MY_BAG = ('shiny', 'gold')


def parser(test=False):
    contains = defaultdict(dict)
    is_contained = defaultdict(list)

    for rule in Input(DAY, 2020, test=test):
        match_container = re.search(r"((\w+) (\w+)) bags? contain", rule).groups()
        # ('light red', 'light', 'red')
        match_contained = re.findall(r"((\d+) (\w+) (\w+) bags?)", rule)
        # [('1 bright white bag', '1', 'bright', 'white'), ('2 muted yellow bags', '2', 'muted', 'yellow')]

        for contained in match_contained:
            contains[ (match_container[1:]) ][contained[2:]] = int(contained[1])
            is_contained[contained[2:]].append( (match_container[1:]) )

    return contains, is_contained    


def recursive_containers(is_contained, my_bag, reached):
    for container_bags in is_contained[my_bag]:
        if container_bags in reached:
            continue
        
        reached.add(container_bags)
        reached = recursive_containers(is_contained, container_bags, reached)
    return reached


def part1(input):
    _, is_contained = input

    valid_containers = set([])
    valid_containers = recursive_containers(is_contained, MY_BAG, valid_containers)

    return len(valid_containers)


def recursive_bags(contains, my_bag):
    # Can be optimized with some memoization.
    # However, it runs fast enough as is.
    my_total = 0
    for bag, s in contains[my_bag].items():
        my_total += s
        my_total += s*recursive_bags(contains, bag) # The sub-bags

    return my_total


def part2(input):
    contains, _ = input
    return recursive_bags(contains, MY_BAG)


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [4, 0], part2, [32, 126])
    main()