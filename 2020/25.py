'''
https://adventofcode.com/2020/day/25
'''
DAY = 25

from utils import *


INPUTS = [
    (1614360, 7734663), # My input
    (5764801, 17807724), # Test 1
]


def parser(test=False):
    if not test:
        return INPUTS[0]
    else:
        return INPUTS[test]


def part1(input):
    card_PK = input[0]
    door_PK = input[1]

    # Compute loop sizes
    subject_number = 7
    loop_sizes = []
    for PK in input:
        value = 1
        loop_size = 0
        while value != PK:
            value *= subject_number
            value = value % 20201227

            loop_size += 1

        loop_sizes.append(loop_size)

    # Compute encryption keys
    encryption_keys = []
    for PK, loop_size in zip(input, loop_sizes[::-1]):
        value = 1
        for _ in range(loop_size):
            value *= PK
            value = value % 20201227

        encryption_keys.append(value)

    assert encryption_keys[0] == encryption_keys[1]

    return encryption_keys[0]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')


if __name__ == "__main__":
    test(DAY, parser, part1, [14897079], None, [])
    main()