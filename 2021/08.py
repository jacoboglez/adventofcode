'''
https://adventofcode.com/2021/day/8
'''
'''
0 (6):  1 (2):  2 (5):  3 (5):  4 (4):
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

5 (5):  6 (6):  7 (3):  8 (7):  9 (6):
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
'''

DAY = 8

UNIQUE_DIGITS   = set([1, 4, 7, 8]) 
UNIQUE_SEGMENTS = set([2, 4, 3, 7])


from utils import *
from itertools import chain


def map_segments(pattern):
    # Sort them to acces by number of segments
    # order of digits: [1, 7, 4, 2/3/5, 0/6/9, 8]
    pattern.sort(key=len)
    pattern_set = [set(p) for p in pattern]
    pattern_str = [''.join(sorted(p)) for p in pattern]
    
    my_segments = {1: pattern_set[0],
                   7: pattern_set[1],
                   4: pattern_set[2],
                   8: pattern_set[9] }
    my_digits = {pattern_str[0]: 1,
                 pattern_str[1]: 7,
                 pattern_str[2]: 4,
                 pattern_str[9]: 8 }
    
    # Find segments 2, 3 and 5 between len 5
    for patt, patt_str in zip(pattern_set[3:6], pattern_str[3:6]):
        # 2: {a, c, d, e, g}
        # 4: {b, c, d, f}
        # (2-4): {a, e, g} 
        if len(patt - my_segments[4]) == 3:
            my_segments[2] = patt
            my_digits[patt_str] = 2

        # 3: {a, c, d, f, g}
        # 7: {a, c, f}
        # (3-7): {d, g}
        elif len(patt - my_segments[7]) == 2:
            my_segments[3] = patt
            my_digits[patt_str] = 3

        # 5: {a, b, d, f, g}
        # 7: {a, c, f}
        # (5-7): {b, d, g}
        elif len(patt - my_segments[7]) == 3:
            my_segments[5] = patt
            my_digits[patt_str] = 5

    # Find segments 0, 6 and 9 between len 6
    for patt, patt_str in zip(pattern_set[6:9], pattern_str[6:9]):
        # 9: {a, b, c, d, f, g}
        # 4: {b, c, d, f}
        # 3: {a, c, d, f, g}
        # (9-3-4): {}
        if len(patt - my_segments[3] - my_segments[4]) == 0:
            my_segments[9] = patt
            my_digits[patt_str] = 9

        # 0: {a, b, c, e, f, g}
        # 1: {c, f}
        # (0-1): {a, b, e, g}
        elif len(patt - my_segments[1]) == 4:
            my_segments[0] = patt
            my_digits[patt_str] = 0

        # 6: {a, b, d, e, f, g}
        # 1: {c, f}
        # (6-1): {a, b, d, e, g}
        elif len(patt - my_segments[1]) == 5:
            my_segments[6] = patt
            my_digits[patt_str] = 6
        else:
            raise

    return my_digits, my_segments


def parser(test=False):
    patterns = []
    outputs = []
    for line in Input(DAY, 2021, test=test):
        p, o = line.split(' | ')
        patterns.append(p.split())
        outputs.append(o.split())

    return patterns, outputs


def part1(input):
    _, outputs = input
    counter = 0
    for o in chain(*outputs):
        if len(o) in UNIQUE_SEGMENTS:
            counter += 1
        
    return counter


def decode_ouput(out, this_digits):
    numbers = ''
    for o in out:
        sorted_o = ''.join(sorted(o))
        n = this_digits[sorted_o] 
        numbers += str(n)

    return int(numbers)


def part2(input):
    patterns, outputs = input
    
    acum = 0
    for patt, out in zip(patterns, outputs):
        this_digits, _ = map_segments(patt)
        numeric_output = decode_ouput(out, this_digits)
        acum += numeric_output

    return acum


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [0, 26], part2, [5353, 61229])
    main()