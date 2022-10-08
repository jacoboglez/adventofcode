'''
https://adventofcode.com/2020/day/2
'''
DAY = 2

from utils import *
import re
from collections import namedtuple


def parser(test=False):
    raw_input = Input(DAY, 2020, test=test)

    Password = namedtuple('Password', ['min', 'max', 'let', 'pas'])
    passwords = []
    for line in raw_input:
        found = re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
        passwords.append( Password(int(found[0]), int(found[1]), found[2], found[3]) )

    return passwords


def part1(input):
    '''The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.'''
    
    valid = 0
    for pwd in input:
        occurrences = pwd.pas.count(pwd.let)
        if pwd.min <= occurrences <= pwd.max:
            valid += 1

    return valid 


def part2(input):
    '''Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. Exactly one of these positions must contain the given letter.'''

    valid = 0
    for pwd in input:
        if (pwd.pas[pwd.min-1] == pwd.let) ^ (pwd.pas[pwd.max-1] == pwd.let):
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
    test(DAY, parser, part1, [2], part2, [1])
    main()