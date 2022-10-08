'''
https://adventofcode.com/2020/day/11
'''
DAY = 11

from utils import *
import numpy as np
from scipy import ndimage


KERNEL = np.array([[1,1,1],[1,0,1],[1,1,1]])


def parser(test=False):
    seats = []
    for row in Input(DAY, 2020, test=test):
        seat_row = []
        for s in row:
            if s == '.':
                seat_row.append(0)
            elif s == 'L':
                seat_row.append(1)
            else:
                raise ValueError
        seats.append(seat_row)

    return np.array(seats)


def print_state(state, seats):
    room = ''
    for r, row in enumerate(state):
        for c, s in enumerate(row):
            if s:
                room += '#'
            else: 
                if seats[r,c]:
                    room += 'L'
                else:
                    room += '.'
        room += '\n'
    print(room)


def update(state, seats):
    ''' Rules:
    If a seat is empty (0) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (1) and four or more seats adjacent to it are also occupied, the seat becomes empty. 
       => If a seat is occupied (1) and (strictly) less than four adjacent seats are free, it stays occupied'''
    new_state = np.zeros([np.size(state, 0), np.size(state, 1)], dtype = int) 

    adjacents = ndimage.convolve(state, KERNEL, mode='constant', cval=0.0)

    # Seats that become occupied (0 -> 1)
    new_state += ( np.logical_not(state) & (adjacents == 0) ) & seats
    
    # Seats that become empty
    new_state += state & (adjacents < 4)

    return new_state


def part1(seats):
    # Everything is empty
    state = np.zeros([np.size(seats, 0), np.size(seats, 1)], dtype = int) 
    # print_state(state, seats)

    t = 0
    while True:
        t += 1
        prev_state = np.copy(state)
        state = update(state, seats)
        # print_state(state, seats)
        if (state==prev_state).all():
            # print_state(state, seats)
            # print_state(prev_state, seats)
            return np.sum(state)


def update2(state, seats):
    seats_indices = np.nonzero(seats)
    new_state = np.zeros([np.size(state, 0), np.size(state, 1)], dtype = int)

    for i, (r, c) in enumerate( zip(*seats_indices) ):
        # print(f'Seat: {r}, {c}')
        # Same row, left and right
        left_idx = np.nonzero( seats[r,:c] )[0][-1:]
        left = state[r,:c][left_idx]
        right_idx = np.nonzero( seats[r,c+1:] )[0][:1]
        right = state[r,c+1:][right_idx]
    
        # Same column, above and below
        above_idx = np.nonzero( seats[:r,c] )[0][-1:]
        above = state[:r,c][ np.nonzero( seats[:r,c])[0][-1:]]
        below_idx = np.nonzero( seats[r+1:,c:] )[0][:1]
        below = state[r+1:,c][np.nonzero( seats[r+1:,c] )[0][:1]]

        # Diagonals
        # Above and left (main diagonal)
        al_idx = np.nonzero( np.flipud(np.fliplr(seats[:r,:c])).diagonal() )[0][:1]
        al = np.flipud(np.fliplr(state[:r,:c])).diagonal()[al_idx]
        
        # Below and right (main diagonal)
        br_idx = np.nonzero( seats[r+1:,c+1:].diagonal() )[0][:1]
        br = state[r+1:,c+1:][br_idx, br_idx]

        # Above and right (flipped diagonal)
        ar_idx = np.nonzero( np.flipud( seats[:r,c+1:] ).diagonal() )[0][:1]
        ar = np.flipud( state[:r,c+1:] ).diagonal()[ar_idx]

        # Below and left (flipped diagonal)
        bl_idx = np.nonzero( np.fliplr( seats[r+1:,:c] ).diagonal() )[0][:1]
        bl = np.fliplr( state[r+1:,:c] ).diagonal()[bl_idx]

        # Apply rules
        occupied = sum(left) + sum(right) + sum(above) + sum(below) + sum(al) + sum(br) + sum(ar) + sum(bl)
        if state[r,c] and (occupied < 5):
            new_state[r,c] = 1
        elif not state[r,c] and (not occupied):
            new_state[r,c] = 1
        elif state[r,c] and (occupied >= 5):
            pass

    return new_state


def part2(seats):
    # Everything is empty
    state = np.zeros([np.size(seats, 0), np.size(seats, 1)], dtype = int) 
    # print_state(state, seats)

    t = 0
    while True:
        t += 1
        prev_state = np.copy(state)
        state = update2(state, seats)
        # print_state(state, seats)
        if (state==prev_state).all():
            # print_state(state, seats)
            # print_state(prev_state, seats)
            return np.sum(state)


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [37], part2, [26])
    main()