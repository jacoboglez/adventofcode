'''
https://adventofcode.com/2021/day/10
'''
DAY = 10

CHECKER_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137, }

MATCHING_OPEN = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<', }

AUTOCOMPLETE_P = {
    '(': 1, 
    '[': 2, 
    '{': 3, 
    '<': 4, }


from utils import *


def parser(test=False):
    return Input(DAY, 2021, test=test)


def compute_scores(input):
    checker_score = 0
    autocomplete_board = []
    for line in input:
        queue = []
        autocomp_score = 0
        for c in line:
            if c in MATCHING_OPEN: # It's a closer
                op = queue.pop()
                if MATCHING_OPEN[c] != op: # Corrupted line
                    checker_score += CHECKER_POINTS[c]
                    break
            else: # It's an opener
                queue.append(c)
        else: # Nobreak: incomplete line
            for c in reversed(queue): # We close from last to first
                autocomp_score *= 5
                autocomp_score += AUTOCOMPLETE_P[c]

            autocomplete_board.append(autocomp_score)

    # Sort to return middle score
    autocomplete_board.sort()
    return checker_score, autocomplete_board[len(autocomplete_board)//2]


def part1(input):
    return compute_scores(input)[0]


def part2(input):
    return compute_scores(input)[1]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [26397], part2, [288957])
    main()