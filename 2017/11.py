'''
https://adventofcode.com/2017/day/11
'''
DAY = 11

from utils import *

# Reference:
# https://www.redblobgames.com/grids/hexagons/

# Movements
MOVEMENTS = {
'N': (0, -2),
'S': (0, 2),
'NE': (1, -1),
'SE': (1, 1),
'NW': (-1, -1),
'SW': (-1, 1) }


def parser(test=False):
    return Input(DAY, 2017, test=test)[0].split(',')


def move(path, current=(0,0)):
    for step in path:
        current = addc(current, MOVEMENTS[step.upper()])

    return current


def distance(a, b=(0,0)):
    '''https://www.redblobgames.com/grids/hexagons/#distances-doubled'''
    drow = abs(a[1] - b[1])
    dcol = abs(a[0] - b[0])
    return dcol + max(0, (drow-dcol)//2)


def part1(input):
    position = move(input)
    dist = distance(position)
    return dist


def part2(input):
    current = (0,0)
    maxdist = 0
    for step in input:
        current = addc(current, MOVEMENTS[step.upper()])
        dist = distance(current)
        if dist > maxdist: maxdist = dist

    return maxdist
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [3,0,2,3], part2, [])
    main()