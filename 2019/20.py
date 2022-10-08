'''
https://adventofcode.com/2019/day/20
'''
DAY = 20

from utils import *
from collections import defaultdict
import re


STEPS = [(0, 1), (0, -1), (-1, 0), (1, 0) ]




def generate_graph(input):
    graph = defaultdict(set)
    portals = defaultdict(set)

    for y, line in enumerate(input[2:-2], 2):
        # print(line[2:-2])
        for x, pos in enumerate(line[2:-2], 2):
            if pos.isupper() or (pos in {' ', '#'}): # Not part of the maze
                continue

            for sx, sy in STEPS:
                adjacent = input[y+sy][x+sx]

                if adjacent == '.':
                    graph[(x, y)].add( (x+sx, y+sy) )

                elif adjacent.isupper(): # Found a portal
                    portal = [adjacent]
                    # Make another step in that direction to find the other letter
                    adjacent2 = input[y+sy+sy][x+sx+sx]
                    portal.append(adjacent2)
                    portal = ''.join(sorted(portal)) # So XY = YX

                    # Add the portal to the graph
                    graph[(x, y)].add( portal )

                    # Track the portal
                    portals[portal].add( (x, y) )

    return graph, portals


def unfold_portals(graph, portals):
    for node, adjacents in graph.items():
        for adj in adjacents:
            if isinstance(adj, str): 
                # Found a portal, replace it with the destination node
                # print(f'{node}: {adjacents}')
                blue_portal = portals[adj] - set((node,))
                graph[node].discard(adj) 
                if blue_portal:
                    graph[node].add( blue_portal.pop() )
                # print(f'{node}: {adjacents}')
                # print()
                break

    return graph


def part1(input):
    graph, portals = generate_graph(input)
    dprint(graph)
    print(portals)
    graph = unfold_portals(graph, portals)
    print(portals)
    # Find shortest path
    path = bfs_path(graph, portals['AA'].pop(), portals['ZZ'].pop())
    return len(path) -1


def part2(input):
    '''
    https://www.reddit.com/r/adventofcode/comments/ed5ei2/2019_day_20_solutions/
    Python part 2. I thought the portal parsing came out pretty messy, but most other posts I see here are even messier, so I'm posting my mess too :) It's just BFS with (x, y, level) coordinates, runs in 1.6s for the real input without any tricks.'''

    graph, portals = generate_graph(input)
    # dprint(graph)
    y_ext = set([2, len(input)-3])
    x_ext = set([2, len(input[0])-3])
    
    # print(f'{y_ext=}')
    # print(f'{x_ext=}')
    # dprint(portals)
    # print(len(portals))

    # BFS shortest path implementation with levels
    start = (*portals['AA'], 0)
    goal = (*portals['ZZ'], 0)

    # print(f'{goal=}')
    # v_coords, v_level = start  
    # print(f'{v_coords=}')
    # print(f'{v_level=}')
    # return -1


    path = bfs_path_levels(graph, start, goal, portals, x_ext, y_ext)
    return len(path) - 1



def bfs_path_levels(graph, start, goal, portals, x_ext, y_ext):
    max_depth = len(portals) + 1

    queue = deque([ (start, [start]) ])
    while queue:
        (vertex, path) = queue.popleft()
        _, v_level = vertex
        if v_level > max_depth:
            continue

        # print(v_level)

        for next in get_adjacents(graph, vertex, portals, x_ext, y_ext):
            if next == goal:
                return path + [next]
            elif next in set(path):
                continue
            else:
                queue.append((next, path + [next]))


def get_adjacents(graph, vertex, portals, x_ext, y_ext):
    # vertex = ((x, y), level)
    v_coords, v_level = vertex
    raw_adjacents = graph[v_coords]

    for ad in raw_adjacents:
        if isinstance(ad, tuple):
            yield (ad, v_level)
            continue
        # We have a portal
        if v_level == 0:
            if ad == 'ZZ': # Found the exit
                yield ('ZZ', 0)
                continue 

            elif (v_coords[0] in x_ext) or (v_coords[1] in y_ext):
                # Level 0 exterior wall
                continue
        # We have a portal not in level 0
        if ad in {'AA', 'ZZ'}: # It is a wall
            continue
        else:
            arrival = portals[ad] - {v_coords}
            if (v_coords[0] in x_ext) or (v_coords[1] in y_ext):
                # It is a exterior portal, substract a level
                level = v_level - 1
                yield (*arrival, level)
            else:
                # It is an interior portal, add a level
                level = v_level + 1
                yield (*arrival, level)


def test():
    # Test number:    1   2
    tests_results = [23, 58]

    print('Part 1:')
    for test_i, test_result in enumerate(tests_results, 1):
        input = Input(DAY, 2019, line_parser=lambda l: l.strip('\n'), test=test_i)
        result = part1(input)
        assert result == test_result
        print(f'Test {test_i} CORRECT')
    
    print('-----------------------------------------')
    print(' ')
    # print('Part 2:')

    # # Test number:   
    # tests_results_2 = []

    # for test_i, test_result in enumerate(tests_results_2, 1):
    #     input = Input(DAY, 2019, test=test_i)
    #     result = part2(input)
    #     assert result == test_result
    #     print(f'Test {test_i} CORRECT')
    

def main():
    input = Input(DAY, 2019, line_parser=lambda l: l.strip('\n'), test=False)

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    print('')
    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    # test()
    main()

