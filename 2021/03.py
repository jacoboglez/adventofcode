'''
https://adventofcode.com/2021/day/3
'''
DAY = 3


from utils import *


def parser(test=False):
    return Input(DAY, 2021, test=test)


def part1(input):
    counter_0 = [0]*len(input[0])
    counter_1 = [0]*len(input[0])
    for binnum in input:
        for i,b in enumerate(binnum):
            if b == '0':
                counter_0[i] += 1
            else:
                counter_1[i] += 1

    gamma = ''
    epsilon = ''
    for c0, c1 in zip(counter_0, counter_1):
        if c0 > c1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
            
    return int(gamma,2) * int(epsilon,2)


def bit_criteria(input, bit=0, opposite=False):
    counter_0 = 0
    counter_1 = 0
    for binnum in input:
        if binnum[bit] == '0':
            counter_0 += 1
        else:
            counter_1 += 1

    if not opposite:
        return '0' if counter_0 > counter_1 else '1'

    return '1' if counter_0 > counter_1 else '0'


def filter_by(input, criteria, bit=0):
    filtered = set()
    for binnum in input:
        if binnum[bit] == criteria:
            filtered.add(binnum)
    
    return filtered


def part2(input):
    OX_candidates = set(input)
    CO2_candidates = set(input)
    
    # Filter Oxygen bits
    bit = 0
    while len(OX_candidates) > 1:
        OX_criteria = bit_criteria(OX_candidates, bit)
        OX_candidates = filter_by(OX_candidates, OX_criteria, bit)
        bit += 1

    # Filter CO2 bits
    bit = 0
    while len(CO2_candidates) > 1:
        CO2_criteria = bit_criteria(CO2_candidates, bit, opposite=True)
        CO2_candidates = filter_by(CO2_candidates, CO2_criteria, bit)
        bit += 1

    return int(OX_candidates.pop(), 2) * int(CO2_candidates.pop(), 2)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [198], part2, [230])
    main()