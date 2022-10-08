'''
https://adventofcode.com/2020/day/19
'''
DAY = 19

from utils import *
import regex as re


def parser(test=False):
    input_raw = Input(DAY, 2020, test=test)
    rules = {}
    for l, line in enumerate(input_raw[:]):
        if line == '': break
        code, rule_raw = line.split(':')
        rules[int(code)] = rule_raw.strip('" ')

    message = input_raw[l+1:]
    return rules, message


def generate_regex(rules, r=0):
    expression = '('
    for c in rules[r].split(' '):
        if c.isalpha():
            return c
        elif c.isnumeric():
            expression += generate_regex(rules, int(c))
        elif c == '|':
            expression += '|'
        else:
            raise NotImplementedError
    expression += ')'
    return expression


def part1(input):
    rules, message = input
    regex_expression = generate_regex(rules)
    regex_expression += '$' # Don't allow extra characters
    pattern = re.compile(regex_expression)
    counter = 0
    for line in message:
        found = pattern.match(line)
        if found:
            counter += 1
    return counter


def part2(input):
    '''0: 8 11
       8: 42 | 42 8 -> 42 | 42 42 | 42 42 42 | ...
       11: 42 31 | 42 11 31 -> 42 31 | 42 42 31 31 | 42 42 ... 31 31 ...
       This means:
       0: 42+ 42{n} 31{n}
       or
       0: 42{m} 31{n} with m > n'''

    rules, message = input
    regex_42 = generate_regex(rules, 42)
    regex_31 = generate_regex(rules, 31)

    regex_expression = f'(?P<g42>{regex_42})+(?P<g31>{regex_31})+$'
    pattern = re.compile(regex_expression)
    
    counter = 0
    for line in message:
        found = pattern.match(line)
        if found: # It matched 42+31+ (m 42 and n 31)
            d = found.capturesdict()
            if len(d['g42']) > len(d['g31']): # Check that m > n
                counter += 1
    return counter


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [2, 3], part2, [False, 12])
    main()