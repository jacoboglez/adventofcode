'''
https://adventofcode.com/2021/day/2
'''
DAY = 2


from utils import *


def parser(test=False):
    return Input(DAY, 2021, test=test)


def part1(input):
    position = 0
    depth = 0

    for i in input:
        match i.split(' '):
            case 'forward', X:
                position += int(X)
            case 'down', X:
                depth += int(X)
            case 'up', X:
                depth -= int(X)

    return position * depth


def part2(input):
    position = 0
    depth = 0
    aim = 0

    for i in input:
        match i.split(' '):
            case 'forward', X:
                position += int(X)
                depth += aim * int(X)
            case 'down', X:
                aim += int(X)
            case 'up', X:
                aim -= int(X)

    return position * depth
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [150], part2, [900])
    main()