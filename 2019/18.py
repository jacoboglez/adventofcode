'''
https://adventofcode.com/2019/day/18


The trick is to use a combination of depth first search first to find all relevant 
weighted paths to nearest keys and Dijkstra to find the final minimum path. 
Incredible how easy it is once you've seen the light. No hacking required, 
no multi threading, just a plain simple algorithm.
https://www.reddit.com/r/adventofcode/comments/ec8090/2019_day_18_solutions/
'''
DAY = 18

from utils import *
from collections import defaultdict
import heapq as hq
import time

STEPS = [(0, 1), (0, -1), (-1, 0), (1, 0) ]
BIG = float("inf")


def parse_input(input, show=False):

    if show:
        # Print the maze
        print('')
        for line in input:
            print(' ', end='')
            print(line)
        print('')

    # Get the dict
    mapp = {}
    for y, line in enumerate(input):
        for x, p in enumerate(line):
            mapp[(x, y)] = p

    return mapp


def generate_graph(mapp):
    key_locations = {}
    door_locations = {}
    graph = defaultdict(set)

    for point, value in mapp.items():
        if value == '#': # It's a wall, not on the graph
            continue

        if value.isalpha() and value.islower(): # It's a key
            key_locations[point] = value

        if value.isalpha() and value.isupper(): # It's a door
            door_locations[point] = value

        if value == '@':
            my_location = point

        for step in STEPS:
            adjacent = addc(point, step)
            adj_value = mapp.get(adjacent, '#')
            if adj_value != '#':
                graph[point].add(adjacent)

    return graph, my_location, key_locations, door_locations


def generate_weighted_graph(graph, key_locations, door_locations):

    weighted_graph = defaultdict(dict)
    doors = set(door_locations.keys()) # Set of coordinates of the doors
    # Find the paths from a key to adjacent keys
    # keeping track of steps to weight the new graph
    for key in key_locations:
        for path_to_adjacent in bfs_adjacents(graph, key, key_locations):
            adjacent_key = path_to_adjacent[-1]
            distance_to_adjacent = len(path_to_adjacent) - 1
            # Check if there is a door in the path
            doors = set(path_to_adjacent).intersection(door_locations.keys())
            weighted_graph[ key_locations[key] ][ key_locations[adjacent_key] ] = \
                ( distance_to_adjacent, {door_locations[d] for d in doors} )

    return weighted_graph


def get_distance(graph, node, keys: set):
    distance, doors = graph[node]
    doors_lower = {D.lower() for D in doors}

    if (doors_lower - keys): # There is at least a door without key
        return BIG
    else:
        return distance


def obtained_keys(parent, current, start='@'):
    node = current
    inverted_path = [current]
    while node != start:
        node = parent.get(node, '')
        inverted_path.append(node)

    return set(inverted_path)


def dijkstra_doors(graph, start):
    ''' Dijkstra shortest path algorithm for a graph of the  form:
    graph = {'A': {'B':2, 'C':9}, 'B': {'C':4}, ... }
    Source:
    https://stackoverflow.com/questions/40871864/dijkstra-s-algorithm-in-python '''

    BIG = float("inf")

    unvisited = {n: BIG for n in graph.keys()} #unvisited node & distance
    unvisited[start] = 0 # set start vertex to 0
    visited = {} # list of all visited nodes
    parent = {} # predecessors

    keys = {}

    while unvisited: # THIS SEEMS OFF
        min_node = min(unvisited, key=unvisited.get) #get smallest distance

        for neighbour in graph[min_node].keys():
            if neighbour not in visited: # THIS SEEMS OFF
                keys = obtained_keys(parent, min_node)
                new_distance = unvisited[min_node] + get_distance(graph[min_node], neighbour, keys)
                if new_distance > 999999999999999:
                    continue
                elif new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parent[neighbour] = min_node

        visited[min_node] = unvisited[min_node]
        unvisited.pop(min_node)

    # # Compute the path
    # node = min_node
    # inverted_path = [min_node]
    # while node != start:
    #     node = parent[node]
    #     inverted_path.append(node)

    return parent, unvisited


def distanceToCollectKeys(currentKey, keys, graph, cache): 
    '''https://www.reddit.com/r/adventofcode/comments/ec8090/2019_day_18_solutions/fbd8y0b/?utm_source=reddit&utm_medium=web2x&context=3'''
    ALLKEYS = set( graph.keys() )
    if not keys:
        return 0, cache

    cacheKey = ( currentKey, ''.join( sorted(list(keys)) ) )
    if cacheKey in cache:
        return cache[cacheKey], cache

    result = float("inf")
    for key, (distance, doors) in graph[ currentKey ].items():

        if {d.lower() for d in doors} - (ALLKEYS - keys): # Not reachable
            continue
        elif key not in keys: # Already collected
            continue

        # Distance from key (reachable from currentKey) to all remaining keys
        dtck, cache = distanceToCollectKeys(key, keys - {key}, graph, cache)
        d = distance + dtck

        # If that distance is less than from other key, store it
        result = min(result, d)

    cache[cacheKey] = result
    return result, cache


def distanceToCollectKeys2(currentKey, keys, graph, cache): 
    '''https://www.reddit.com/r/adventofcode/comments/ec8090/2019_day_18_solutions/fbd8y0b/?utm_source=reddit&utm_medium=web2x&context=3'''
    ALLKEYS = set( graph.keys() )
    if not keys:
        return 0, cache

    cacheKey = ( currentKey, ''.join( sorted(list(keys)) ) )
    if cacheKey in cache:
        return cache[cacheKey], cache

    result = float("inf")
    for key, (distance, doors) in graph[ currentKey ].items():

        # Now there are no doors effectively
        # if {d.lower() for d in doors} - (ALLKEYS - keys): # Not reachable
        #     continue
        if key not in keys: # Already collected
            continue

        # Distance from key (reachable from currentKey) to all remaining keys
        dtck, cache = distanceToCollectKeys2(key, keys - {key}, graph, cache)
        d = distance + dtck

        # If that distance is less than from other key, store it
        result = min(result, d)

    cache[cacheKey] = result
    return result, cache


def part1(input):
    mapp = parse_input(input)

    
    graph, my_location, key_locations, door_locations = generate_graph(mapp)

    tic = time.time()
    weighted_graph = generate_weighted_graph(graph, 
                                            {my_location:'@', **key_locations},
                                             door_locations)
    toc = time.time()
    print(f'Time graph build: {toc-tic}')
    # dprint(weighted_graph)

    tic = time.time()
    distance, _ = distanceToCollectKeys('@', set(weighted_graph.keys()) - {'@'}, weighted_graph, dict())
    toc = time.time()
    print(f'Time search: {toc-tic}')

    return distance


def part2(input):
    mapp = parse_input(input)

    
    tic = time.time()
    graph, my_location, key_locations, door_locations = generate_graph(mapp)
    # print(key_locations.values())
    # print(door_locations.values())
    weighted_graph = generate_weighted_graph(graph, 
                                            {my_location:'@', **key_locations},
                                             door_locations)
    toc = time.time()
    # print(f'Time graph build: {toc-tic}')
    # dprint(weighted_graph)

    tic = time.time()
    distance, _ = distanceToCollectKeys2('@', set(weighted_graph.keys()) - {'@'}, weighted_graph, dict())
    toc = time.time()
    # print(f'Time search: {toc-tic}')
    
    # print(distance)
    return distance
    

def test():
    # Test number:    1    2    3   4
    tests_results = [86, 132, 136, 81]

    print('Part 1:')
    for test_i, test_result in enumerate(tests_results, 1):
        input = Input(DAY, 2019, test=test_i)
        result = part1(input)
        if result == test_result:
            print(f'Test {test_i} CORRECT')
        else:
            print(f'XXXXXXXXXXXXXXXXXXXX')
            print(f'Test {test_i} FAILED')
            print(f'Result: {result}')
            print(f'XXXXXXXXXXXXXXXXXXXX')
            break
    else: # nobreak
        print('All tests passed.')
    
    print('-----------------------------------------')
    # print(' ')
    # print('Part 2:')

    # # Test number:   
    # tests_results_2 = []

    # for test_i, test_result in enumerate(tests_results_2, 1):
    #     input = Input(DAY, 2019, test=test_i)
    #     result = part2(input)
    #     assert result == test_result
    #     print(f'Test {test_i} CORRECT')
    

def main():
    input = Input(DAY, 2019)
    
    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    # Part 2
    result_2 = 0
    for v in range(1,5):
        input = Input(f'{DAY}_2{v}', 2019)
        result_v = part2(input)
        result_2 += result_v

    print(f'Part 2: {result_2}')
    

if __name__ == "__main__":
    # test()
    main()