'''
https://adventofcode.com/2020/day/23
'''
DAY = 23

from utils import *
from collections import deque
from array import array


INPUTS = [
    '792845136', # My input
    '389125467', # Test 1
]


def parser(test=False):
    if not test:
        return INPUTS[0]
    else:
        return INPUTS[test]


def part1(input):
    cups = deque([int(i) for i in input])

    for t in range(100):
        # Find current cup
        current = cups[0]

        # Rotate to be right to the group to be picked
        cups.rotate(-1)
        
        # Pick the group of three
        picked = [cups.popleft() for _ in range(3)]
        
        # Find the destination point
        destination = (current - 2)%9 + 1
        while destination in picked:
            destination = (destination - 2) %9 +1

        # Rotate to the destination point (to extend on the left)
        cups.rotate( -cups.index(destination)-1 )

        # Insert the picked cups
        cups.extend(picked)

        # Rotate to have the next current cup on [0]
        cups.rotate( -cups.index(current)-1 )

    # Rotate to have the 1 on the right
    cups.rotate( -cups.index(1)-1 )

    return int(''.join([str(cups.popleft()) for _ in range(8)]))


def part2(input):
    '''Optimized solution based on:
     https://github.com/ephemient/aoc2020/blob/main/py/src/aoc2020/day23.py '''

    first_cups = [int(i) for i in input]
    # Working with 1-indexed and the value on [0] is a dummy
    next_cup = array('I', range(1,1_000_000+2))
    total = len(next_cup)-1

    # Writhe the input of the problem
    for cup1, cup2 in zip(first_cups[:-1], first_cups[1:]):
        next_cup[cup1] = cup2
    # Link the last cup
    next_cup[ first_cups[-1] ] = 10 # Last of the input to the range
    next_cup[ -1 ] = first_cups[0] # Last of the range to the first

    current = first_cups[0]
    for t in range(10_000_000):

        # Pick the group of three
        p1 = next_cup[current]
        p2 = next_cup[p1]
        p3 = next_cup[p2]
        after_group = next_cup[p3]

        # Find the destination point
        destination = (current - 2)%total + 1
        while destination in (p1, p2, p3):
            destination = (destination - 2)%total + 1 

        # Update list
        aux = next_cup[destination]
        next_cup[current] = after_group
        next_cup[destination] = p1
        next_cup[p3] = aux

        # Update current
        current = after_group

    star1 = next_cup[1]
    star2 = next_cup[star1]
    
    return star1*star2
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [67384529], part2, [149245887792])
    main()