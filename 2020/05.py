'''
https://adventofcode.com/2020/day/5
'''
DAY = 5

from utils import *
from math import ceil, floor


TOTAL_ROWS = 128
TOTAL_COLUMNS = 8


def parser(test=False):
    return Input(DAY, 2020, test=test)


def test_passes():
    test_cases = {
        'FBFBBFFRLR': (44, 5, 357),
        'BFFFBBFRRR': (70, 7, 567),
        'FFFBBBFRRR': (14, 7, 119),
        'BBFFBBFRLL': (102, 4, 820),
    }

    for test, test_result in test_cases.items():
        row, column = compute_seat(test)
        ID = compute_id(row, column)
        if (row, column, ID) != test_result:
            print(f'Test FAILED for {test}')
            print(f'Expected: {test_result}')
            print(f'Obtained: {(row, column, ID)}')
            print()
            raise AssertionError

    print('Tests PASSED.')
    print('-----------------------------------------\n')


def compute_seat(boarding_pass):
    # Compute the row
    min_row = 0
    max_row = TOTAL_ROWS - 1
    for letter in boarding_pass[0:7]:
        if letter == 'F':
            max_row = floor( (min_row + max_row)/2 )
        elif letter == 'B':
            min_row = ceil( (min_row + max_row)/2 )
        else:
            raise ValueError('Expected "F" or "B" in the first 7 positions.')

    # Check that correctly computed
    if max_row == min_row:
        row = max_row
    else:
        raise ValueError(f'Discrepancy between {max_row=} and {min_row=} ({boarding_pass}).')

    # Compute the column
    min_col = 0
    max_col = TOTAL_COLUMNS - 1
    for letter in boarding_pass[7:]:
        if letter == 'L':
            max_col = floor( (min_col + max_col)/2 )
        elif letter == 'R':
            min_col = ceil( (min_col + max_col)/2 )
        else:
            raise ValueError('Expected "L" or "R" in the last 3 positions.')

    # Check that correctly computed
    if max_col == min_col:
        col = max_col
    else:
        raise ValueError(f'Discrepancy between {max_col=} and {min_col=} ({boarding_pass}).')

    return row, col


def compute_id(row, column):
    return row*8 + column


def part1(input):
    max_ID = 0
    for boarding_pass in input:
        row, column = compute_seat(boarding_pass)
        ID = compute_id(row, column)
        if ID > max_ID:
            max_ID = ID

    return max_ID


def part2(input):
    empty_seats_IDs = { compute_id(r,c) for r in range(TOTAL_ROWS) for c in range(TOTAL_COLUMNS) }

    # Check all the empty seats
    for boarding_pass in input:
        row, col = compute_seat(boarding_pass)
        empty_seats_IDs.remove( compute_id(row, col) )

    # Find the one surrounded
    for ID in empty_seats_IDs:
        if (ID+1 not in empty_seats_IDs) and (ID-1 not in empty_seats_IDs):
            return ID


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test_passes()
    main()