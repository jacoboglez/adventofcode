'''
https://adventofcode.com/2021/day/11
'''
DAY = 11


from utils import *
import numpy as np


STEPS = 100
MINFTY = -1000


def parser(test=False):
    matrix = np.array([[int(i) for i in line] for line in Input(DAY, 2021, test=test)])
    matrix = np.pad(matrix, 1, 'constant', constant_values=MINFTY)
    return matrix


def part1(octopuses, steps=STEPS):
    flashes = 0

    for s in range(steps):
        '''First, the energy level of each octopus increases by 1'''
        octopuses += 1
      
        new_octopuses = np.array(octopuses, copy=True)
        while (octopuses>9).any():
            for r, row in enumerate(octopuses[1:-1,1:-1]):
                for c, _ in enumerate(row):
                    new_octopuses[r+1, c+1] += sum(sum(octopuses[r:r+3,c:c+3]>9))
            
            # The ones that have flashed in this substep are set to -infty
            # because they can't flash again
            new_octopuses[octopuses>9] = MINFTY

            flashes += sum(sum(octopuses>9))
            octopuses = np.array(new_octopuses, copy=True)

        octopuses = octopuses[1:-1,1:-1]
        octopuses[octopuses<0] = 0

        # Check if they all flash at the same time (for part 2)
        if sum(sum(octopuses)) == 0:
            # Return the step of synchronization (won't affect part 1)
            return s+2

        octopuses = np.pad(octopuses, 1, 'constant', constant_values=MINFTY)

    return flashes


def part2(input):
    return part1(input, steps=99999999)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [1656], part2, [196])
    main()