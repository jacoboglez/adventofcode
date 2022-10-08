'''
https://adventofcode.com/2017/day/17
'''
DAY = 17


from utils import *
from collections import deque


def parser(test=False):
    return int(Input(DAY, 2017, test=test)[0])


def part1(step):
    buffer = deque([])
    for i in range(2017+1):
        buffer.rotate(-step)
        buffer.append(i)
    idx_2017 = buffer.index(2017)
    return buffer[(idx_2017+1)%len(buffer)]


def part2(step):
    after0 = 0
    current = 0
    for i in range(50_000_000):
        # The insert position of i+1 is:
        # the current position + step size + 1 (bc next position)
        # mod the number of things already inserted (i+1 because 0 counts)
        current = (current + step + 1)%(i+1)
        if current == 0:
            # We only care about the value inserted after 0
            after0 = i+1

    return after0


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [638], part2, [])
    main()