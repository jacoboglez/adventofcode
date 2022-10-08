'''
https://adventofcode.com/2019/day/15
'''
DAY = 15

from utils import *
from icc import intCodeComputer
from collections import defaultdict, deque
# from time import sleep


# How to print:
# 0: The repair droid hit a wall. Its position has not changed.
# 1: The repair droid has moved one step in the requested direction.
# 2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
# 
#        0    1    2    -2   -1
FILL = ['█', '·', 'X', 'O', ' ']

SHOW_MAP = False
#         NONE    NORTH   SOUTH    WEST     EAST
STEP = [ (0, 0), (0, 1), (0, -1), (-1, 0), (1, 0) ]
OPPOSITE = [0, 2, 1, 4, 3]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def paint(mapp):
    xmax = max(mapp.keys(), key=lambda a: a[0])[0] + 1
    ymax = max(mapp.keys(), key=lambda a: a[1])[1] + 1
    xmin = min(mapp.keys(), key=lambda a: a[0])[0] - 1
    ymin = min(mapp.keys(), key=lambda a: a[1])[1] - 1

    line = ''
    for y in range(ymax, ymin-1, -1):
        for x in range(xmin, xmax+1):
            line += FILL[ mapp.get((x, y), -1) ]
        line += '\n'

    print(line)


def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


def part1(program):
    software = intCodeComputer(program, id=1, verbose=False)

    droid = (0, 0)
    visited = set([droid]) # Add the origin
    mapp = {droid: -2} # Mark the origin
    graph = defaultdict(set)
    
    queue = [1, 2, 3, 4]
    backtrack = []
    available = {droid: [1,2,3,4]}

    cont = 0 # DEBUG

    while True:

        if not available[droid]:
            if not backtrack:
                # print('No remaining movements.')
                break
            else:
                movement = backtrack.pop()
                software.inputArray = [ movement ]
                software.compute()
                droid = add( droid, STEP[movement] )
                continue
                

        # print(f'queue: {queue}')
        movement = available[droid].pop()
        # print(f'movement: {movement}')

        # The Droid moves
        software.inputArray = [ movement ]
        software.compute()
        found = software.outputArray[-1]

        next_pos = add( droid, STEP[movement] ) # Compute next position
        mapp[next_pos] = found # Add what was encountered to the map

        # if found == 1:
        if found in {1, 2}:
            # Add the coming back to the queue
            backtrack.append( OPPOSITE[movement] )
            # Add the next movements to explore
            next_movements = [1,2,3,4]
            next_movements.remove( OPPOSITE[movement] ) # Withouth the backtrack
            queue = next_movements
            available[next_pos] = next_movements
            graph[droid].add(next_pos)
            graph[next_pos].add(droid)
            droid = next_pos
            if found == 2: # found the oxygen
                oxygen = droid

        # DEBUG
        cont += 1
        if cont > 5000:
            break


    paint(mapp)
    # print(f'steps: {cont}')
    # print(f'Oxygen: {oxygen}')
    # print()
    # Find the shortest path
    shortest = bfs_shortest_path(graph, (0, 0), oxygen)

    return len(shortest) -1, graph, oxygen

 
def part2(graph, oxygen):
    empty_locations = set([])
    for subset in graph.values():
        empty_locations = empty_locations.union(subset)
    n_empty_locations = len(empty_locations)

    filling = set([ oxygen ])
    filled_locations = set([])

    t = 0
    while len(filled_locations) < n_empty_locations:
        annex = set([])
        for f in filling:
            annex.update( graph[f] )

        filled_locations = filled_locations.union(annex)
        filling = filling.union(annex)

        t += 1

    return t


def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])

    result_1, graph, oxygen = part1(program)
    print(f'Part 1: {result_1}')

    print('')
    result_2 = part2(graph, oxygen)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()