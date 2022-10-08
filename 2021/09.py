'''
https://adventofcode.com/2021/day/9
'''
DAY = 9


from utils import *


def parser(test=False):
    raw_input = Input(DAY, 2021, test=test)
    return [[int(c) for c in row] for row in raw_input]


def find_lows(input):
    lows = {}
    for r, row in enumerate(input):
        for c, h in enumerate(row):
            # Top (negated)
            if (r > 0) and (input[r-1][c] <= h):
                continue
            # Bottom (negated)
            if (r < len(input)-1) and (input[r+1][c] <= h):
                continue
            # Left (negated)
            if (c > 0) and (input[r][c-1] <= h):
                continue
            # Right (negated)
            if (c < len(row)-1) and (input[r][c+1] <= h):
                continue
            
            lows[(r,c)] = h
            
    return lows


def flood(input, start):
    visited, queue = set(), deque([start])
    while queue: 
        vertex = queue.popleft()
        visited.add(vertex)

        # Find all adjacents (if not 9)
        adjacents = []
        r,c = vertex
        # Top
        if (r > 0) and (input[r-1][c] != 9):
            adjacents.append((r-1,c))
        # Bottom
        if (r < len(input)-1) and (input[r+1][c] != 9):
            adjacents.append((r+1,c))
        # Left
        if (c > 0) and (input[r][c-1] != 9):
            adjacents.append((r,c-1))
        # Right
        if (c < len(input[0])-1) and (input[r][c+1] != 9):
            adjacents.append((r,c+1))

        queue.extend(n for n in adjacents if n not in visited)

    return len(visited)


def part1(input):
    lows = find_lows(input)
    
    risk_level = 0
    for h in lows.values():
        risk_level += h+1

    return risk_level


def part2(input):
    lows = find_lows(input)
    # The number of basins is reasonable to store them all
    basin_sizes = [flood(input, start) for start in lows.keys()]
    basin_sizes.sort()

    return basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [15], part2, [1134])
    main()