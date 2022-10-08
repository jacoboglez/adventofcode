'''
https://adventofcode.com/2020/day/14
'''
DAY = 14

from utils import *
import re
from itertools import product


def parser(test=False):
    return Input(DAY, 2020, test=test)


def apply_mask(int_value, mask):
    bin_value = list(f'{int_value:#038b}')
    for i, m in enumerate(mask, 2):
        if m != 'X':
            bin_value[i] = m

    return int(''.join(bin_value), 2)


def part1(input):
    mem = {}
    mask = 'X'*36
    for instruction in input:

        match_mem = re.search(r"mem\[(\d+)\] = (\d+)", instruction)
        if match_mem:
            address, value = match_mem.groups()
            mem[int(address)] = apply_mask(int(value), mask)
            continue

        match_mask = re.search(r"mask = (.+)", instruction)
        if match_mask:
            mask = match_mask.groups()[0]

    return sum(mem.values())


def address_decoder(int_value, mask):
    bin_value = list(f'{int_value:#038b}')
    N_floating = mask.count('X')
    combinations = product('01', repeat=N_floating)
    for comb in combinations:
        c = 0
        for i, m in enumerate(mask, 2):
            if m == 'X':
                bin_value[i] = comb[c]
                c += 1
            elif m == '1':
                bin_value[i] = '1'

        yield int(''.join(bin_value), 2)


def part2(input):
    mem = {}
    mask = 'X'*36
    for instruction in input:

        match_mem = re.search(r"mem\[(\d+)\] = (\d+)", instruction)
        if match_mem:
            address, value = match_mem.groups()
            for dec_address in address_decoder(int(address), mask):
                mem[dec_address] = int(value)
            continue

        match_mask = re.search(r"mask = (.+)", instruction)
        if match_mask:
            mask = match_mask.groups()[0]

    return sum(mem.values())
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [165], part2, [False, 208])
    main()