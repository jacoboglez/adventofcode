'''
https://adventofcode.com/2021/day/6
'''
DAY = 6


from utils import *
from collections import Counter, deque


def parser(test=False):
    input = Input(DAY, 2021, test=test, line_parser=integers)[0]
    return Counter(input)


def part1(input, N_days=80):
    fish_stages = deque([])
    for i in range(9):
        fish_stages.append(input[i])

    for _ in range(N_days):
        born = fish_stages.popleft()
        # Add the recent parents to stage 6
        fish_stages[6] += born
        # Add the newborns to stage 8
        fish_stages.append(born)

    return sum(fish_stages)


def part2(input):
    return part1(input, N_days=256)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [5934], part2, [26984457539])
    main()