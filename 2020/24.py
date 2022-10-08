'''
https://adventofcode.com/2020/day/24
'''
DAY = 24

from utils import *


# Directions -> grid movement (row, column)
E = (0, -2)
SE = (1, -1)
SW = (1, 1)
W = (0, 2)
NW = (-1, 1)
NE = (-1, -1)
DIRS = [E, SE, SW, W, NE, NW]

'''
    1  2  3  
       __
1   __/  \__
2  /  \__/  \
3  \__/  \__/
4  /  \__/  \
5  \__/  \__/
      \__/    
 
'''


def parser(test=False):
    return Input(DAY, 2020, test=test)


def got_to_tile(directions):
    current = (0, 0)
    p = 0

    while p < len(directions):
        if directions[p] == 'e':
            current = addc(current, E)
            p += 1
        elif directions[p] == 'w':
            current = addc(current, W)
            p += 1
        elif directions[p:p+2] == 'ne':
            current = addc(current, NE)
            p += 2
        elif directions[p:p+2] == 'nw':
            current = addc(current, NW)
            p += 2
        elif directions[p:p+2] == 'se':
            current = addc(current, SE)
            p += 2
        elif directions[p:p+2] == 'sw':
            current = addc(current, SW)
            p += 2
        else:
            raise NotImplementedError

    return current


def part1(input):
    black_tiles = set([])

    for directions in input:
        tile = got_to_tile(directions)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return len(black_tiles)


def count_black_adjacents(tile, black_tiles):
    b_adjacents = 0

    for direction in DIRS:
        adjacent = addc(tile, direction)
        if adjacent in black_tiles:
            b_adjacents += 1

    return b_adjacents


def update_tiles(black_tiles):
    '''     
    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    => Any black tile with 1 or 2 black tiles adjacent is kept black.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    '''

    # Find boundaries
    minr = min(black_tiles, key=lambda t: t[0])[0] - 2
    maxr = max(black_tiles, key=lambda t: t[0])[0] + 2

    # Adjust to have x values in the odd columns
    minc = min(black_tiles, key=lambda t: t[1])[1] - 2
    if minc%2: minc -= 1
    maxc = max(black_tiles, key=lambda t: t[1])[1] + 2
    if maxc%2: maxc += 1

    new_blacks = set([])
    for r in range(minr, maxr+1):
        o = 1 if r%2 else 0 # Move 1 in odd rows
        for c in range(minc-o, maxc+1+o, 2):
            tile = (r, c)

            b_adjacents = count_black_adjacents(tile, black_tiles)
            if (tile in black_tiles) and (b_adjacents in (1,2)):
                new_blacks.add(tile)
            elif (tile not in black_tiles) and (b_adjacents == 2):
                new_blacks.add(tile)

    return new_blacks


def part2(input):

    # Compute the initial setup
    black_tiles = set([])
    for directions in input:
        tile = got_to_tile(directions)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    for t in range(100):
        black_tiles = update_tiles(black_tiles)
        # if not (t+1)%10:
        #     print(f'Day {t+1}: {len(black_tiles)}')

    return len(black_tiles)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [10], part2, [2208])
    main()