''' Utils to solve the Advent of Code puzzles.
Some based on:
https://nbviewer.jupyter.org/github/norvig/pytudes/blob/master/ipynb/Advent-2018.ipynb
'''
import re
from collections import deque, defaultdict
from collections.abc import MutableMapping

import pprint
pp = pprint.PrettyPrinter(indent=4)
dprint = pp.pprint


def Input(day, year, line_parser=str.strip, test=False):
    "For this day's input file, return a tuple of each line parsed by `line_parser`."
    return mapt(line_parser, open(f'./inputs/{year}_{day}.txt')) if not test \
    else mapt(line_parser, open(f'./inputs/{year}_{day}_test{test}.txt'))


def integers(text): 
    "A tuple of all integers in a string (ignore other characters)."
    return mapt(int, re.findall(r'-?\d+', text))


def mapt(fn, *args): 
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


def test(DAY, parser, part1=lambda x:None, results_part_1=[], part2=lambda x:None, results_part_2=[]):

    if results_part_1 or results_part_2:
        print('TESTS')
    else:
        return

    if results_part_1:
        print('Part 1:')

    for test_i, test_result in enumerate(results_part_1, 1):
        if not test_result:
            continue
        input = parser(test=test_i)
        result = part1(input)
        if result == test_result:
            print(f'Test {test_i} CORRECT')
        else:
            print(f'Test {test_i} FAILED')
            print(f'  result: {result}')
            raise AssertionError
    

    if results_part_2:
        print('Part 2:')

    for test_i, test_result in enumerate(results_part_2, 1):
        if not test_result:
            continue
        input = parser(test=test_i)
        result = part2(input)
        if result == test_result:
            print(f'Test {test_i} CORRECT')
        else:
            print(f'Test {test_i} FAILED')
            print(f'  result: {result}')
            raise AssertionError

    print('-----------------------------------------\n')


# Graphs

def addc(a, b):
    ''' Add two coordinates by components, or a coordinate and a scalar'''
    if isinstance(b, tuple):
        return (a[0]+b[0], a[1]+b[1])
    elif isinstance(b, int):
        return (a[0]+b, a[1]+b)
    else:
        raise NotImplementedError

def mulc(a, b):
    ''' Add two coordinates by components, or a coordinate and a scalar'''
    if isinstance(b, tuple):
        return (a[0]*b[0], a[1]*b[1])
    elif isinstance(b, int):
        return (a[0]*b, a[1]*b)
    else:
        raise NotImplementedError


def paint(mapp, legend, default = 0):
    '''Print a map of coordinates with a legend:
    mapp is a dict containing the 2d coordinates of the points as keys
    and the type of point as value.
    legend is a list of chars that provide the char that must be used for each value'''
    xmax = max(mapp.keys(), key=lambda a: a[0])[0] + 1
    ymax = max(mapp.keys(), key=lambda a: a[1])[1] + 1
    xmin = min(mapp.keys(), key=lambda a: a[0])[0] - 1
    ymin = min(mapp.keys(), key=lambda a: a[1])[1] - 1

    line = ''
    for y in range(ymax, ymin-1, -1):
        for x in range(xmin, xmax+1):
            line += legend[ mapp.get((x, y), default) ]
        line += '\n'

    print(line)
    

def bfs(graph, root): 
    '''Yield nodes of a graph given as a dict, where adjacent nodes are sets
    following the BFS algorithm.
    Source: 
    https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3 '''

    visited, queue = set(), deque([root])
    while queue: 
        vertex = queue.popleft()
        yield vertex
        visited.add(vertex)
        queue.extend(n for n in graph[vertex] if n not in visited)


def bfs_adjacents(graph, start, goals):
    '''Return the shortest path from start to all the goals (generator) 
    in a graph given as a dict, where goals is a list. 
    Following the BFS algorithm.
    Source:
    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/ '''

    goals_set = set(goals)

    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next in goals_set:
                goals_set.remove(next)
                yield path + [next]

                # change by yield if you want all paths
            # else:
            #     queue.append((next, path + [next]))
            queue.append((next, path + [next]))


def bfs_path(graph, start, goal):
    '''Return the shortest path from start to goal in a graph given as a dict, 
    where adjacent nodes are sets, following the BFS algorithm.
    It is a particular case of bfs_adjacents.
    Source:
    https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/ '''

    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
                # change by yield if you want all paths
            else:
                queue.append((next, path + [next]))


def dfs(graph, start, visited=set()):
    '''Source: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python'''

    visited.add(start)
    print(start)
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)

    return visited   


def weight_graph(graph, key_locations=None):
    '''Transform a unweighted graph into a weighted graph removing "corridors"
    of the form:
    {node: {adjacent:distance, adj2:dist2}, node2: {adj:dist}, ... }
    '''

    if not key_locations:
        # Find key locations: bifurcations and dead ends
        key_locations = []
        for k, v in graph.items():
            if len(v) != 2: # If it is 2 it will only connect to T previous and next nodes
                key_locations.append(k)

    weighted_graph = defaultdict(dict)

    # Find the paths from a key to adjacent keys
    # keeping track of steps to weight the new graph
    for key in key_locations:
        for path_to_adjacent in bfs_adjacents(graph, key, key_locations):
            adjacent_key = path_to_adjacent[-1]
            distance_to_adjacent = len(path_to_adjacent) - 1
            weighted_graph[key][adjacent_key] = distance_to_adjacent

    return weighted_graph


def dijkstra(graph, start, end):
    ''' Dijkstra shortest path algorithm for a graph of the  form:
    graph = {'A': {'B':2, 'C':9}, 'B': {'C':4}, ... }
    Source:
    https://stackoverflow.com/questions/40871864/dijkstra-s-algorithm-in-python '''

    BIG = float("inf")

    unvisited = {n: BIG for n in graph.keys()} #unvisited node & distance
    unvisited[start] = 0 # set start vertex to 0
    visited = {} # list of all visited nodes
    parent = {} # predecessors
    # dprint(unvisited)
    while unvisited:
        min_node = min(unvisited, key=unvisited.get) #get smallest distance
        if min_node == end:
            break

        for neighbour in graph[min_node].keys():
            if neighbour not in visited:
                new_distance = unvisited[min_node] + graph[min_node].get(neighbour, BIG)
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parent[neighbour] = min_node

        visited[min_node] = unvisited[min_node]
        unvisited.pop(min_node)

    # Compute the path
    node = end
    inverted_path = [end]
    while node != start:
        node = parent[node]
        inverted_path.append(node)

    return list(reversed(inverted_path)), unvisited[end]


if __name__ == "__main__":
    pass