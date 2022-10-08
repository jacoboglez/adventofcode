'''
https://adventofcode.com/2020/day/20
'''
DAY = 20

from utils import *
from collections import defaultdict
import numpy as np


def parser(test=False):
    input_raw = Input(DAY, 2020, test=test)
    tiles = defaultdict(list)
    current_tile = -1
    for line in input_raw:
        if 'Tile' in line:
            current_tile = int(line.strip(':').split(' ')[1])
            continue
        elif not line: # Finished the previous tile
            tiles[current_tile] = np.array( tiles[current_tile] )
            continue

        tiles[current_tile].append(  [1 if c == "#" else 0 for c in line]  )

    return tiles


def matcher(tiles):
    edges = defaultdict(list)
    matches = {ID: [0, 0, 0, 0, 0, 0, 0, 0] for ID in tiles.keys()}

    slices = [np.index_exp[0,:], # Top
              np.index_exp[-1,:], # Bottom
              np.index_exp[:,0], # Left
              np.index_exp[:,-1], ] # Right

    for ID, tile in tiles.items():
        for i,s in enumerate(slices):
            if edges[str( tile[s] )]: # Found a match
                otherID, otheri = edges[str( tile[s] )][0]
                matches[ID][i] = (otherID, otheri)
                matches[otherID][otheri] = (ID, i)

            elif edges[str( np.flip(tile[s]) )]: #+4 means that orientation flipped
                otherID, otheri = edges[str( np.flip(tile[s]) )][0]
                matches[ID][i+4] = (otherID, otheri)
                matches[otherID][otheri] = (ID, i+4)
            
            edges[str( tile[s] )].append( (ID, i) )
            edges[str( np.flip(tile[s]) )].append( (ID, i+4) )
    
    return matches


def part1(input):
    matches = matcher(input)
    corners = 1

    for tile, edges in matches.items():
        connected_edges = sum([0 if not e else 1 for e in edges])
        if connected_edges == 2: # It is a corner
            corners *= tile

    return corners


def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [20899048083289], part2, [])
    main()