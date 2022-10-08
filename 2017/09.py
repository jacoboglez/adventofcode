'''
https://adventofcode.com/2017/day/9
'''
DAY = 9

'''
!. -> ''
<[^>]*> -> ''
'''

from utils import *
import re


def parser(test=False):
    input = Input(DAY, 2017, test=test)[0]
    # Remove comments
    cleaned = re.sub(r'!.', '', input)
    return cleaned


def part1(input):
    # Remove garbage
    input = re.sub(r'<[^>]*>', '', input)

    level = 0
    count = 0
    for c in input:
        if c == '{':
            level +=1
        if c == '}':
            count += level
            level -= 1
    
    return count


def part2(input):
    # Count garbage
    garbage_groups =  re.findall(r'<[^>]*>', input)

    count = 0
    for group in garbage_groups:
        count += len(group)-2

    return count
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [1+6+5+16+1+9+9+3], part2, [None, 17+3+2+10])
    main()