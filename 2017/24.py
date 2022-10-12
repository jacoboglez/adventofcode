'''
https://adventofcode.com/2017/day/24
'''
DAY = 24

import sys
sys.path.insert(0, '.')

from utils import *
from collections import defaultdict
# from functools import cache


def parser(test=False):
    components = []
    inventory = defaultdict(list)
    for cmp in  Input(DAY, 2017, test=test):
        cmp_int = [int(c) for c in cmp.split('/')]
        # I store them ordererd so the representation is unique
        i = min(cmp_int)
        j = (max(cmp_int))
        components.append((i, j))
        inventory[i].append(j)
        if i != j:
            inventory[j].append(i)

    # Check that all components are unique
    assert(len(set(components)) == len(components))

    return inventory


# @cache # Cannot be used with sets and dicts
def builder(port, used, inventory):
    max_strength = 0

    for q in inventory[port]:
        if (this_port := (min(port, q), max(port, q))) not in used:
            new_used = used.copy()
            new_used.add(this_port)
            this_strength = builder(q, new_used, inventory)
            this_strength += port + q
            if this_strength > max_strength:
                max_strength = this_strength
    
    return max_strength


def long_builder(port, used, inventory, length=0):
    max_strength = 0
    max_length = 0
    for q in inventory[port]:
        if (this_port := (min(port, q), max(port, q))) not in used:
            new_used = used.copy()
            new_used.add(this_port)
            this_strength, this_length = long_builder(q, new_used, inventory,length)

            this_strength += port + q
            this_length += 1
            if this_length > max_length:
                max_length = this_length
                max_strength = this_strength
            elif (this_length == max_length) and \
                 (this_strength > max_strength):
                max_strength = this_strength
    
    return max_strength, max_length


def part1(inventory):
    initial_port = 0
    return builder(initial_port, set(), inventory)


def part2(inventory):
    initial_port = 0
    return long_builder(0, set(), inventory)[0]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [31], part2, [19])
    main()