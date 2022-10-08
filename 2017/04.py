'''
https://adventofcode.com/2017/day/4
'''
DAY = 4

from utils import *
from collections import Counter


def parser(test=False):
    return Input(DAY, 2017, test=test)


def part1(input):
    valid = 0
    for passphrase in input:
        words = passphrase.split(' ')
        if len(set(words)) == len(words):
            valid += 1
    
    return valid


def part2(input):

    valid = 0
    for passphrase in input:
        words = passphrase.split(' ')
        counters = []
        for w in words:
            d = Counter(c for c in w)
            if d in counters:
                break
            counters.append(d)
        else: #nobreak
            valid += 1
    
    return valid
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [2], part2, [None, 3])
    main()