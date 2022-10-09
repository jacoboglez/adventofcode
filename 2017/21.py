'''
https://adventofcode.com/2017/day/21
'''
DAY = 21


from utils import *
import numpy as np


SEED = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
    

def str2array(s):
    l = []
    for row in s.split('/'):
        l.append([1 if c=='#' else 0 for c in row])
    return np.array(l)


def allRotations(a):
    b = a.copy()
    for _ in range(4):
        b = np.rot90(b)
        yield b
    b = np.fliplr(b)
    for _ in range(4):
        b = np.rot90(b)
        yield b


def parser(test=False):
    raw_input = Input(DAY, 2017, test=test)
    rules = dict()
    for line in raw_input:
        a, b = line.split(' => ')
        a = str2array(a)
        b = str2array(b)
        for aa in allRotations(a):
            rules[str(aa)] = b
    return rules


def enhance(image, rules):
    length = np.shape(image)[0]
    if length%2 == 0:
        # Divide into 2x2 blocks
        bs = 2
    elif length%3 == 0:
        # Divide into 3x3 blocks
        bs = 3
    else:
        raise

    enhanced_blocks = []

    for r in range(0, length, bs):
        row_blocks = []
        for c in range(0, length, bs):
            original_block = image[r:r+bs,c:c+bs]
            enhanced_block = rules[str(original_block)]
            row_blocks.append(enhanced_block)

        enhanced_blocks.append(row_blocks)

    return np.block(enhanced_blocks)


def part1(rules, iterations=5):
    image = SEED
    iterations = 18
    for step in range(iterations):
        print(step)
        image = enhance(image, rules)
    return np.sum(image)


def part2(rules):
    # Not optimized, runs in a reasonable amount of time.
    return part1(rules, iterations=18)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()