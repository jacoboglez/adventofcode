'''
https://adventofcode.com/2021/day/1
'''
DAY = 1


from utils import *


def parser(test=False):
    return [int(i) for i in Input(DAY, 2021, test=test)]


def part1(input):
    counter = 0
    for a,b in zip(input[:-1], input[1:]):
        if b > a:
            counter +=1

    return counter


def part2(input):
    blocks = [sum(input[i:i+3]) for i in range(len(input)-2)]
    return part1(blocks)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [7], part2, [5])
    main()