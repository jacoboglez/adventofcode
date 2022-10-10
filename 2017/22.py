'''
https://adventofcode.com/2017/day/22
'''
DAY = 22

import sys
sys.path.insert(0, '.')

from utils import *


DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]

def parser(test=False):
    whitespace_remover = lambda s: s.replace(' ', '').strip('\n')
    raw_input = Input(DAY, 2017, line_parser=whitespace_remover, test=test)
    return map2dict(raw_input)[0]


def burst(map, vector, dir):
    current_node = map.get(vector, '.')

    if current_node == '.': # Clean
        dir = (dir+1) % 4 # Turn left
        map[vector] = '#' # Become infected
        infection = 1
    elif current_node == '#': # Infected
        dir = (dir-1) % 4 # Turn right
        map[vector] = '.' # Become clean
        infection = 0
    else:
        raise(NotImplementedError)

    # Advance one step
    vector = addc(vector, DIRECTIONS[dir])

    return map, vector, dir, infection


def evolvedBurst(map, vector, dir):
    current_node = map.get(vector, '.')

    if current_node == '.': # Clean
        dir = (dir+1) % 4 # Turn left
        map[vector] = 'W' # weakened
        infection = 0
    elif current_node == 'W': # Weakened 
        # Do not turn
        map[vector] = '#' # infected 
        infection = 1
    elif current_node == '#': # Infected
        dir = (dir-1) % 4 # Turn right
        map[vector] = 'F' # flagged
        infection = 0
    elif current_node == 'F': # Flagged
        dir = (dir+2) % 4 # Reverse
        map[vector] = '.' # clean
        infection = 0
    else:
        raise(NotImplementedError)

    # Advance one step
    vector = addc(vector, DIRECTIONS[dir])

    return map, vector, dir, infection


def part1(mapp, bursts=70):
    # The virus carrier begins in the middle of the mapp facing up.
    grid_size = list(mapp.keys())[-1]
    vector = (grid_size[0]//2, grid_size[1]//2)
    
    dir = 2
    # paint(mapp, {'.':'.', '#':'#'}, default='.')
    counterr = 0
    for _ in range(bursts):
        mapp, vector, dir, infection = burst(mapp, vector, dir)
        counterr += infection
        # paint(mapp, {'.':'.', '#':'#'}, default='.')
        # print()

    return counterr


def part2(mapp, bursts=10000000):
    # The virus carrier begins in the middle of the mapp facing up.
    grid_size = list(mapp.keys())[-1]
    vector = (grid_size[0]//2, grid_size[1]//2)
    
    dir = 2
    # paint(mapp, {'.':'.', '#':'#', 'W':'W', 'F':'F'}, default='.')
    counter = 0
    for _ in range(bursts):
        mapp, vector, dir, infection = evolvedBurst(mapp, vector, dir)
        counter += infection
        # paint(mapp, {'.':'.', '#':'#', 'W':'W', 'F':'F'}, default='.')
        # print()

    return counter
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input.copy(), bursts=10000)
    print(f'Part 1: {result_1}')

    result_2 = part2(input.copy(), bursts=10000000)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [41], part2, [2511944])
    main()