'''
https://adventofcode.com/2017/day/12
'''
DAY = 12

from utils import *


def parser(test=False):
    input = Input(DAY, 2017, test=test)
    pipes = {}
    for line in input:
        a, bs = line.split(' <-> ')
        pipes[int(a)] = set([int(b) for b in bs.split(', ')])

    return pipes




def part1(pipes):
    counter = 0
    for c in pipes.keys():
        if bfs_path(pipes, c, 0):
            counter += 1

    return counter+1


def part2(pipes):
    '''Not optimal, the check could be done faster than doing bfs for each case.'''
    groups = []
    for c in pipes.keys():
        for g in groups:
            if bfs_path(pipes, c, g):
                break
        else: #nobreak
            groups.append(c)

    return len(groups)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [6], part2, [2])
    main()