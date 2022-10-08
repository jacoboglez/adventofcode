'''
https://adventofcode.com/2019/day/22
'''
DAY = 22

from utils import *
from collections import defaultdict, deque
import re



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


def part1(input, N=10007):
    
    deck = shuffle(deque(range(N)), input)

    return deck.index(2019)


def part2(input, N=119315717514047):
    pass
    # deck = deque(range(N))

    # for it in range(101741582076661):
    #     print(it)
    #     deck = shuffle(deck, input)   


def main():
    input = Input(DAY, 2019, line_parser=lambda l: l.strip('\n').split(' '))

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    # print('')
    result_2 = part2(input)
    # print(f'Part 2: {result_2}')


def test():
    deck = deque(range(10))
    # deck.reverse() #  # deal into new stack
    deck = deal(deck, 3)
    print(deck)




if __name__ == "__main__":
    main()
