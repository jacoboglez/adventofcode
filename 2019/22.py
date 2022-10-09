'''
https://adventofcode.com/2019/day/22
'''
DAY = 22

from functools import reduce
from utils import *
from collections import defaultdict, deque
import re


TIMES = 101741582076661


def deal(dq, N):
    table = deque(range(len(dq)))
    start_value = dq[0]

    while dq:
        table[0] = dq.pop()
        table.rotate(N)

    # Order the table
    index_of_start = table.index(start_value)
    table.rotate(-index_of_start)
    # Equivalent:
    # while table[0] != start_value:
    #     table.rotate()

    return table


def shuffle(deck, actions):
    for action in actions:
        if (action[0] == 'deal') and (action[1] == 'into'):
            # deal into new stack
            deck.reverse()
        elif (action[0] == 'cut'):
            # cut N cards
            Ncut = int(action[-1])
            deck.rotate(-Ncut)
        elif (action[0] == 'deal') and (action[1] == 'with'):
            Ndeal = int(action[-1])
            deck = deal(deck, Ndeal)

    return deck


def reduce_instructions(input, Ncards):
    '''See
    https://www.reddit.com/r/adventofcode/comments/ee56wh/comment/fc0xvt5/
    '''
    instructions = input
    reduced_instructions = []

    # Expand "deal into new stack" to "deal with increment (count-1)" and "cut 1"
    for inst in instructions:
        if inst[1] == 'into':
            reduced_instructions.append(['deal', 'with', 'increment', str(Ncards-1)])
            reduced_instructions.append(['cut', '1'])
        else:
            reduced_instructions.append(inst)

    instructions = reduced_instructions
    
    # Iteratively reduce the instructions until only two
    while len(reduced_instructions) > 2:
        reduced_instructions = []
        i = 0
        while i < len(instructions):

            if (i) >= len(instructions)-1:
                reduced_instructions.append(instructions[i])
                break

            if (instructions[i][0] == "cut") and (instructions[i+1][0] == "cut"):
                x = int(instructions[i][1])
                y = int(instructions[i+1][1])
                reduced_instructions.append(['cut', str((x+y)%Ncards)])
                i += 2
            elif (instructions[i][1] == "with") and (instructions[i+1][1] == "with"):
                x = int(instructions[i][3])
                y = int(instructions[i+1][3])
                reduced_instructions.append(['deal', 'with', 'increment', str((x*y)%Ncards)])
                i += 2
            elif (instructions[i][0] == "cut") and(instructions[i+1][1] == "with"):
                x = int(instructions[i][1])
                y = int(instructions[i+1][3])
                reduced_instructions.append(['deal', 'with', 'increment', str(y)])
                reduced_instructions.append(['cut', str((x*y)%Ncards)])
                i += 2
            else:
                reduced_instructions.append(instructions[i])
                i += 1

        instructions = reduced_instructions

    return reduced_instructions


def reduce_shuffles(input, Ncards, Nshuffles):
    N_tot = 0
    tot_input = []
    while N_tot < Nshuffles:
        N = 1
        N_input = input
        while N < ((Nshuffles-N_tot)/2):
            N_input = N_input + N_input
            N *= 2
            N_input = reduce_instructions(N_input, Ncards)

        tot_input = reduce_instructions(tot_input+N_input, Ncards)
        N_tot += N

    return tot_input, N_tot


def gcdExtended(a, b):
    '''Modified from (removed global variables):
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/'''
 
    # Base Case
    if (a == 0):
        return b, 0, 1
 
    # To store results of recursive call
    gcd, x1, y1 = gcdExtended(b % a, a)
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd, x, y
 
 
def modInverse(A, M):
    '''Modified from: 
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/'''
    g, x, y = gcdExtended(A, M)
    if (g != 1):
        return None
 
    else:
        # m is added to handle negative x
        res = (x % M + M) % M
        return res


def part1(input, N=10007):
    # deck = shuffle(deque(range(N)), input)
    
    reduced_input = reduce_instructions(input, N)   
    deck = shuffle(deque(range(N)), reduced_input)

    return deck.index(2019)


def part2(input, N=119315717514047):
    '''Based on some comments on the solution thread on Reddit:
    MegaGreenLightning: 
    https://www.reddit.com/r/adventofcode/comments/ee56wh/comment/fbr0vjb/
    and 
    franbcn: 
    https://www.reddit.com/r/adventofcode/comments/ee56wh/comment/fc0xvt5/
    '''

    # Reduce the input instructions using the ideas from franbcn to only tow instructions
    reduced_input = reduce_instructions(input, N)   
    # Now, repeating the instructions the number of times required and reducing them after that,
    # obtain the two instructions equivalent to TIMES shuffles
    reduced_shuffles, _ = reduce_shuffles(reduced_input, N, TIMES)

    # The cut happens afther the deal with.
    # The card that is in possition 2020 was in position (2020+x)%Ncards before "cut x"
    x = int(reduced_shuffles[1][1])
    position = (2020+x) % N

    # Finally, we compute the answer using the modular multiplicative inverse:
    # A·X = 1 (mod M) ---MMI---> X
    # What "deal with increment" does is taking card C and puting it into possition increment·C % Ncards
    # So I need to find the MMI of increment (mod Ncards)
    increment = int(reduced_shuffles[0][3])
    return ((position)*modInverse(increment, N)) % N


def main():
    input = Input(DAY, 2019, line_parser=lambda l: l.strip('\n').split(' '))

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    print('')
    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()
