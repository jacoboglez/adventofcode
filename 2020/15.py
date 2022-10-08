'''
https://adventofcode.com/2020/day/15
'''
DAY = 15

from utils import *


INPUTS = [
    [0,13,16,17,1,10,6], # My input
    [0,3,6], # Test 1
    [1,3,2], # Test 2
    [2,1,3], # Test 3
    [1,2,3], # Test 4
    [2,3,1], # Test 5
    [3,2,1], # Test 6
    [3,1,2], # Test 7
]


def parser(test=False):
    if not test:
        return INPUTS[0]
    else:
        return INPUTS[test]


def part1(input, final_number=2020):
    seen = {n: i for i,n in enumerate(input[:-1],1)}
    last_spoken = input[-1]
    for t in range(len(input), final_number):
        if last_spoken in seen:
            say = (t) - seen[last_spoken]
        else:
            say = 0
        seen[last_spoken] = t
        last_spoken = say
        # print(f'Turn {t+1}: {say}  {seen}')

    return say


def part2(input):
    return part1(input, final_number=30000000)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test_results_1 = [436, 1, 10, 27, 78, 438, 1836]
    test_results_2 = [175594, 2578, 3544142, 261214, 6895259, 18, 362]

    test(DAY, parser, part1, test_results_1, part2, test_results_2)
    main() 