'''
https://adventofcode.com/2020/day/12
'''
DAY = 12

from utils import *
from collections import deque


def parser(test=False):
    return Input(DAY, 2020, test=test)


def part1(input):
    position = (0,0)
    #                        E      S         W       N
    orientations = deque([ (1,0), (0, -1), (-1, 0), (0, 1)])

    for movement in input:
        instruction = movement[0]
        value = int(movement[1:])

        if instruction == 'N':
            position = addc( position, mulc( (0, 1), value) )
        elif instruction == 'S':
            position = addc( position, mulc( (0, -1), value) )
        elif instruction == 'E':
            position = addc( position, mulc( (1, 0), value) )
        elif instruction == 'W':
            position = addc( position, mulc( (-1, 0), value) )
        elif instruction == 'L':
            orientations.rotate( value//90 )
        elif instruction == 'R':
            orientations.rotate( -value//90 )
        elif instruction == 'F':
            position = addc( position, mulc(orientations[0], value) )
        else:
            raise NotImplementedError

    return abs(position[0]) + abs(position[1])


def part2(input):
    ship = (0, 0)
    waypoint = (10, 1)

    for movement in input:
        instruction = movement[0]
        value = int(movement[1:])

        if instruction == 'N':
            waypoint = addc( waypoint, mulc( (0, 1), value) )
        elif instruction == 'S':
            waypoint = addc( waypoint, mulc( (0, -1), value) )
        elif instruction == 'E':
            waypoint = addc( waypoint, mulc( (1, 0), value) )
        elif instruction == 'W':
            waypoint = addc( waypoint, mulc( (-1, 0), value) )
        elif instruction == 'L':
            for _ in range(value//90):
                waypoint = (-waypoint[1], waypoint[0])
        elif instruction == 'R':
            for _ in range(value//90):
                waypoint = (waypoint[1], -waypoint[0])
        elif instruction == 'F':
            ship = addc( ship, mulc(waypoint, value) )
        else:
            raise NotImplementedError

    return abs(ship[0]) + abs(ship[1])
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [25], part2, [286])
    main()