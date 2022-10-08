'''
https://adventofcode.com/2021/day/15
'''
DAY = 15


from utils import *
import numpy as np


BIG = 999999999


def parser(test=False):
    input = Input(DAY, 2021, test=test)
    return np.array([[int(i) for i in line] for line in input])


def min_idx(a):
    return np.unravel_index(np.argmin(a, axis=None), a.shape)


def neigbours(node, lr, lc):
    ns = []
    if node[0] > 0:
        ns.append((node[0]-1, node[1]))
    if node[0] < (lr-1) :
        ns.append((node[0]+1, node[1]))
    if node[1] > 0:
        ns.append((node[0], node[1]-1))
    if node[1] < (lc-1) :
        ns.append((node[0], node[1]+1))

    return ns


def dijkstra(input, start=(0,0), end=(9,9)):
    lr, lc = input.shape

    unvisited = np.array([[BIG for i in line] for line in input])
    unvisited_set = {(r,c) for r in range(lr) for c in range(lc)}
    unvisited[start] = 0 # set start vertex to 0
    visited = {} # list of all visited nodes
    parent = {} # predecessors
    
    while unvisited_set:
        min_node = min_idx(unvisited)
        if min_node == end:
            break

        for neighbour in neigbours(min_node, lr, lc):
            if neighbour not in visited:
                new_distance = unvisited[min_node] + input[neighbour]
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parent[neighbour] = min_node

        visited[min_node] = unvisited[min_node]
        unvisited_set.remove(min_node)
        unvisited[min_node] = 999999999999

    # Compute the path
    node = end
    inverted_path = [end]
    while node != start:
        node = parent[node]
        inverted_path.append(node)

    return list(reversed(inverted_path)), unvisited[end]


def part1(input):
    lr, lc = input.shape
    return dijkstra(input, (0,0), (lr-1, lc-1))[1]


def part2(input):
    # Generate new input
    rows = []
    for r in range(5):
        new_base = input + r
        columns = []
        for c in range(5):
            columns.append(new_base+c)
        
        new_row = np.concatenate(columns, axis=1)
        rows.append(new_row)

    new_input = np.concatenate(rows, axis=0)
    
    # Wrap values (it can only wrap once)
    new_input[new_input>9] = new_input[new_input>9] - 9
    
    # A bit slow but fast enough (< 1 min)
    return part1(new_input)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [40], part2, [315])
    main()