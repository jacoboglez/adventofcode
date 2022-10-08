'''
https://adventofcode.com/2017/day/14
'''
DAY = 14


from utils import *
from day_10 import knothash
from collections import defaultdict


def parser(test=False):
    return Input(DAY, 2017, test=test)[0]


def binrep(hsh):
    return ''.join(f'{int(d,16):04b}' for d in hsh)


def part1(input):
    counter = 0
    for i in range(128):
        l = binrep(knothash(f'{input}-{i}'))
        counter += l.count('1')

    return counter
    

def explore_grid(grid):
    graph = defaultdict(list)
    for i, line in enumerate(grid[:-1]):
        for j, l in enumerate(line[:-1]):
            if l == '1':
                if not graph[(i,j)]:
                    graph[(i,j)] = []
                if line[j+1]=='1':
                    graph[(i,j)].append( (i,j+1) )
                    graph[(i,j+1)].append( (i,j) )
                if grid[i+1][j]=='1':
                    graph[(i,j)].append( (i+1,j) )
                    graph[(i+1,j)].append( (i,j) )
                
    return graph


def part2(input):
    # Build the grid adding an extra space and extra line at the end to handle edge nodes.
    grid = [binrep(knothash(f'{input}-{i}'))+' ' for i in range(128)]
    grid.append(' '*129)

    graph = explore_grid(grid)

    groups = 0
    while graph:
        current_root = list(graph.keys())[0]
        graph_cop = graph.copy()
        groups += 1
        for i in bfs(graph, current_root):
            if i in graph_cop:
                del graph_cop[i]

        graph = graph_cop.copy()

    return groups


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [8108], part2, [1242])
    main()