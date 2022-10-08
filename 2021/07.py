'''
https://adventofcode.com/2021/day/7
'''
DAY = 7


from utils import *
from collections import Counter


def parser(test=False):
    return Counter(Input(DAY, 2021, test=test, line_parser=integers)[0])


def fuel_estimation_1(crabs, destination):
    fuel = 0
    for position, number in crabs.items():
        fuel += number * abs(destination-position)

    return fuel


def fuel_estimation_2(crabs, destination):
    fuel = 0
    for position, number in crabs.items():
        steps = abs(destination-position)
        fuel += number * ( steps*(steps+1)//2 )

    return fuel


def part1(input, fuel_estimation=fuel_estimation_1):
    min_fuel = float('inf')
    for p in range(min(input.keys()), max(input.keys())+1):
        p_fuel = fuel_estimation(input, p)
        if p_fuel < min_fuel:
            min_fuel = p_fuel
            # min_pos = p

    # print(f'Alignment position: {min_pos}')
    return min_fuel


def part2(input):
    return part1(input, fuel_estimation=fuel_estimation_2)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [37], part2, [168])
    main()