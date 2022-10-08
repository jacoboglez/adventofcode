'''
https://adventofcode.com/2017/day/3
'''
DAY = 3

INPUT = [
289326, # Puzzle Input
12, 15, 23, 1024, # Tests part 1
130, 750 # Tests part 2
]

from utils import *
import urllib.request


def parser(test=False):
    if not test:
        return INPUT[0]
    else:
        return INPUT[test]


def part1(input):
    # Find the containing square
    square = 1
    while input > square**2:
        square += 2
    
    # Steps on the outer square
    length = input - (square-2)**2

    # Steps on the edge
    edge_steps = length % (square-1)

    # Distance to the center of the edge
    from_center = abs((square-1)//2 - edge_steps)

    # Steps to the outer square + steps from the center of the edge
    return (square-1)//2 + from_center


def part2(input):
    '''See: https://oeis.org/A141481
    Look up table of the sequence: https://oeis.org/A141481/b141481.txt'''
    
    table = urllib.request.urlopen('https://oeis.org/A141481/b141481.txt') # it's a file like object and works just like a file
    for line in table: # files are iterable
        text =  line.decode('ascii')
        if text[0] == "#":
            continue
        entry = integers(text)[1]
        if entry > input:
            return entry
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [3, 2, 2, 31], part2, [None, None, None, None, 133, 806])
    main()