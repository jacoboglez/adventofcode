'''
https://adventofcode.com/2021/day/22
'''
DAY = 22


from utils import *


def parser(test=False):
    coordinates = Input(DAY, 2021, test=test, line_parser=integers)
    switches = [1 if l.split(' ')[0]=='on' else 0 for l in Input(DAY, 2021, test=test)]
    return switches, coordinates


def cuboid(xa, xb, ya, yb, za, zb, l=50):
    # l is the limit of the initialization procedure area
    cubes = set()
    for x in range(max(xa,-l), min(xb,l)+1):
        for y in range(max(ya,-l), min(yb,l)+1):
            for z in range(max(za,-l), min(zb,l)+1):
                cubes.add((x,y,z))

    return cubes


def part1(input):
    switches, coordinates = input
    on_cubes = set()
    for s, range in zip(switches, coordinates):
        cubes = cuboid(*range)
        if s: # Switch on
            on_cubes |= cubes
        else: # Switch off
            on_cubes -= cubes

    return len(on_cubes)


def cuboid2(xa, xb, ya, yb, za, zb):
    # l is the limit of the initialization procedure area
    cubes = set()
    for x in range(xa, xb+1):
        for y in range(ya, yb+1):
            for z in range(za, zb+1):
                cubes.add((x,y,z))

    return cubes


def part2(input):
    switches, coordinates = input
    on_cubes = set()
    for s, range in zip(switches, coordinates):
        cubes = cuboid2(*range)
        if s: # Switch on
            on_cubes |= cubes
        else: # Switch off
            on_cubes -= cubes

    return len(on_cubes)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [590784, 474140], part2, [None, 2758514936282235]) # 2758514936282235
    main()