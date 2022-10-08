'''
https://adventofcode.com/2017/day/8
'''
DAY = 8

from os import register_at_fork
from utils import *
from collections import defaultdict


def parser(test=False):
    return Input(DAY, 2017, test=test)


def part12(input):
    REGISTERS = defaultdict(int)
    maxval = 0
    for line in input:
        [reg, oper, val, _, reg_cond, cond, val_cond] = line.split(' ')
        
        # Evaluate condition
        if not eval(f'{REGISTERS[reg_cond]} {cond} {val_cond}'):
            continue

        # Execute operation
        if oper == 'inc':
            REGISTERS[reg] += int(val)

        elif oper == 'dec':
            REGISTERS[reg] -= int(val)

        else:
            raise(NotImplementedError)

        if REGISTERS[reg] > maxval:
                maxval = REGISTERS[reg]

    return max(REGISTERS.values()), maxval



def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1, result_2 = part12(input)
    print(f'Part 1: {result_1}')

    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, lambda i: part12(i)[0], [1], 
                      lambda i: part12(i)[1], [10])
    main()