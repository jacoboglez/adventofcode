'''
https://adventofcode.com/2021/day/4
'''
DAY = 4


from utils import *
from itertools import chain


def parser(test=False):
    draws, *boards_input = Input(DAY, 2021, test=test, line_parser=integers)
    all_boards = []
    board = []
    for line in boards_input[1:]: # First line is blank
        # Blank lines indicate new board
        if not line:
            all_boards.append(board)
            board = []
            continue
        board.append(list(line))

    # Add the last board
    all_boards.append(board)

    return draws, all_boards


def draw_and_check(board, d):
    # Possible winner rows and cols
    row_winner = set(range(5))
    col_winner = set(range(5))

    # Iteration through elements
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            # If drawn value: mark with -1
            if value == d:
                board[r][c] = -1

            # If value not drawn: r and c not a winner
            if board[r][c] != -1:
                row_winner.discard(r)
                col_winner.discard(c)
    
    if row_winner or col_winner:
        return board, True

    return board, False


def score(board, d):
    s = 0
    for b in chain(*board): # Flatten the board
        if b != -1:
            s += b

    return s*d


def part1(input):
    draws = input[0]
    all_boards = input[1]

    for d in draws:
        for i, board in enumerate(all_boards):
            new_board, winner = draw_and_check(board, d)
            if winner:
                return score(board, d)
            all_boards[i] = new_board


def part2(input):
    draws = input[0]
    all_boards = input[1]
    
    while all_boards:
        remove_boards = [] # Winned boards to remove
        for d in draws:
            for i, board in enumerate(all_boards):
                new_board, winner = draw_and_check(board, d)
                all_boards[i] = new_board # Update the board
                if winner:
                    # If the board is a winner:
                    s = score(board, d) # Save its score
                    remove_boards.append(i) # Mark it to be removed

            if remove_boards:
                # Remove the boards from end to beginning to avoid index shifting
                for i in sorted(remove_boards, reverse=True):
                    del all_boards[i]
                remove_boards = []
                    
    return s # The last score saved            
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [4512], part2, [1924])
    main()