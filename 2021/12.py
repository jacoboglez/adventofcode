'''
https://adventofcode.com/2021/day/12
'''
DAY = 12


from utils import *
from collections import defaultdict


def parser(test=False):
    input = Input(DAY, 2021, test=test)
    graph = defaultdict(list)
    for line in input:
        a, b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)

    return graph


def visit_caves(graph, start, visited=None, paths=None, special_cave=''):
    if visited is None: visited = []
    if paths is None: paths = set()

    this_visited = visited.copy()
    this_visited.append(start)

    if start == 'end':
        paths.add(','.join(this_visited))
        return paths

    small_visited = set(c for c in this_visited if c.islower())

    # Deal with the special case
    if this_visited.count(special_cave) == 1:
        small_visited.remove(special_cave)

    for next in set(graph[start]) - small_visited:
        paths = visit_caves(graph, next, this_visited, paths, special_cave)

    return paths


def part1(graph):
    paths = visit_caves(graph, 'start')
    # print('\n'.join(paths))
    return len(paths)


def part2(graph):
    small_caves = [c for c in graph.keys() if c.islower()]
    small_caves.remove('start')
    small_caves.remove('end')

    paths = set()
    for sc in small_caves:
        paths.update(visit_caves(graph, 'start', special_cave=sc))

    # print('\n'.join(paths))
    return len(paths)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [10, 19, 226], part2, [36, 103, 3509])
    main()