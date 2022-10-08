'''
https://adventofcode.com/2021/day/20
'''
DAY = 20


from utils import *
import numpy as np


def parser(test=False):
    input = Input(DAY, 2021, test=test)
    algorithm = [1 if a == '#' else 0 for a in input[0]]
    original = np.array([[1 if a == '#' else 0 for a in l] for l in input[2:]])

    # Original pad with 0 for the check
    original = np.pad(original, pad_width=10, mode='constant', constant_values=0)

    return algorithm, original


def bool2int(x):
    y = 0
    for i,j in enumerate(x):
        y += j<<i
    return y


def print_image(bits):
    printrow = ''
    for row in bits:
        for c in row:
            printrow += '#' if c else '.'
        printrow += '\n'

    print(printrow)
        

def enhancement_iteration(original, algorithm):
    '''Trim not optimized, a bit slow.'''
    # Pad continuing the edge
    original = np.pad(original, pad_width=5, mode='edge')
    rows, columns = original.shape

    # Generate new empty image
    new = np.zeros([rows, columns], dtype=np.int0)

    for r in range(rows-3):
        for c in range(columns-3):
            submatrix = original[r:r+3,c:c+3]
            dec = bool2int( np.flip(submatrix.flatten()) )
            new[r,c] = algorithm[dec]

    # Trim
    n = 3
    new = new[n:-n,n:-n]
    return new


def part1(input, cycles=2):
    algorithm, image = input
    for _ in range(cycles):
        image = enhancement_iteration(image, algorithm)

    return sum(sum(image))


def part2(input):
    return part1(input, cycles=50)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [35], part2, [3351])
    main()