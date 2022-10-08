'''
https://adventofcode.com/2020/day/6
'''
DAY = 6

from utils import *


def parser(test=False):
    return Input(DAY, 2020, test=test)


def part1(input):
    yes = set([])
    total = 0
    for passanger in input:
        if not passanger:
            total += len(yes)
            yes = set([])
            continue
        
        yes.update(passanger)
    
    # Add the last group
    total += len(yes)
    return total


def part2(input):
    yes = set('abcdefghijklmnopqrstuvwxyz')
    total = 0
    for passanger in input:
        if not passanger:
            total += len(yes)
            yes = set('abcdefghijklmnopqrstuvwxyz')
            continue

        yes = yes.intersection( set(passanger) )
    
    # Add the last group
    total += len(yes)
    return total
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [11], part2, [6])
    main()