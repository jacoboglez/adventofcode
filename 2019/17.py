'''
https://adventofcode.com/2019/day/17
'''
DAY = 17

from utils import *
from icc import intCodeComputer
from collections import defaultdict, deque
# from time import sleep


SHOW_MAP = False
#        NORTH   SOUTH    WEST     EAST
STEPS = [(0, 1), (0, -1), (-1, 0), (1, 0) ]
OPPOSITE = [0, 2, 1, 4, 3]


def get_cameras(program):
    software = intCodeComputer(program, id=1, verbose=False)
    software.compute()
    ascii_out = software.outputArray

    # Convert the ascii codes to the visible image
    line = ''.join( [chr(a) for a in ascii_out] )
    # print(line)

    # Generate the mapp dict
    x = 0
    y = 0
    mapp = {}
    for a in ascii_out:
        if a == 10: # newline
            y += 1
            x = 0
            continue
        mapp[(x, y)] = chr(a)
        x += 1
    return mapp


def generate_graph(mapp):
    graph = defaultdict(list)

    for point, value in mapp.items():
        if value not in {'#', '^', 'v', '<', '>'}: # empty point
            continue

        if value in {'^', 'v', '<', '>'}:
            roomba = point 

        for step in STEPS:
            adjacent = addc(point, step)
            adj_value = mapp.get(adjacent, '.')
            if adj_value in {'#', '^', 'v', '<', '>'}:
                graph[point].append(adjacent)

    return graph, roomba


def part1(program):
    mapp = get_cameras(program)

    # Get the intersection points
    intersections = []
    for point, value in mapp.items():
        if value not in {'#', '^', 'v', '<', '>'}: # empty point
            continue

        for step in STEPS:
            adjacent = addc(point, step)
            adj_value = mapp.get(adjacent, '.')
            if adj_value == '.':
                break
        else: #nobreak => its an interesection
            intersections.append( point )

    # print(f'Intersection points: {intersections} ({len(intersections)})')
    return sum( [a[0]*a[1] for a in intersections] )

 
def part2(program):

    # Start with the roomba movements
    software = intCodeComputer(program, id=2, verbose=False)
    # Wake the roomba
    software.memory[0] = 2

    # Program the roomba
    # Main movement
    main_mov = 'A,B,A,C,B,C,B,C,A,C'
    # Movement functions
    A = 'L,10,R,12,R,12'
    B = 'R,6,R,10,L,10'
    C = 'R,10,L,10,L,12,R,6'

    # Video feed
    video = 'n'

    roomba = '\n'.join([main_mov, A, B, C, video, ''])
    roomba_ascii = [ord(a) for a in roomba]

    # Upload the roomba code
    software.inputArray = roomba_ascii

    # Run the roomba
    software.compute()

    # Video
    ascii_out = software.outputArray

    # Convert the ascii codes to the visible image
    line = ''.join( [chr(a) for a in ascii_out] )
    dust = ascii_out[-1]
    # print(line)
    # print(f'Dust: {dust}')
    return dust


def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])
    
    result_1 = part1(program)
    print(f'Part 1: {result_1}')

    print('')
    result_2 = part2(program)
    print(f'Part 2: {result_2}')
    # print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()