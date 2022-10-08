'''
https://adventofcode.com/2020/day/22
'''
DAY = 22

from utils import *
from collections import deque
from itertools import islice


def parser(test=False):
    integers_input = Input(DAY, 2020, integers, test=test)
    player1 = []
    player2 = []
    current = player1
    for int_tuple in integers_input:
        if not int_tuple:
            current = player2
            continue
        current.append(int_tuple[0])

    # The first number of each player is the player number, not a card
    return player1[1:], player2[1:]


def compute_score(winner):
    score = 0
    for value, card in enumerate(reversed(winner)):
        score += (value+1) * card
    return score


def part1(input):
    player1, player2 = deque(input[0]), deque(input[1])

    round_number = 0
    while (len(player1) > 0) and (len(player2) > 0):
        round_number += 1
        if player1[0] > player2[0]:
            player1.rotate(-1)
            player1.append(player2.popleft())
        elif player2[0] > player1[0]:
            player2.rotate(-1)
            player2.append(player1.popleft())
        else:
            raise

    return compute_score(player1) if player1 else compute_score(player2)


def recursive_combat(player1, player2):
    previous_states = set([])

    round_number = 0
    while (len(player1) > 0) and (len(player2) > 0):
        round_number += 1
        # print()
        # print(f'Round {round_number}')
        # print(f'Player 1: {player1}.')
        # print(f'Player 2: {player2}.')

        # New rule 1
        current_state = ( hash(tuple(player1)), hash(tuple(player2)) )
        if current_state in previous_states:
            # print('GAME WINNED BY 1 (repeat)')
            return 1, compute_score(player1)

        previous_states.add(current_state)

        draws = [player1.popleft(), player2.popleft()]
        # print(f'Draws: 1->{draws[0]}\n       2->{draws[1]}.')

        # New rule 2
        if (len(player1) >= draws[0]) and (len(player2) >= draws[1]):
            # print('Recursive game!')
            # print('----------------------------------')
            winner, score = recursive_combat( deque(islice(player1, 0, draws[0])), 
                                              deque(islice(player2, 0, draws[1])) )
            # print('----------------------------------')
            # print(f'Recursion winned by {winner}')

            if winner == 1:
                player1.extend(draws)
            elif winner == 2:
                player2.extend(reversed(draws))
            else:
                raise ValueError('Winner different from 1 or 2')

            continue

        if draws[0] > draws[1]:
            # Player 1 wins
            player1.extend(sorted(draws, reverse=True))
            # print(f'Round winned by {1}')
        elif draws[1] > draws[0]:
            # Player 2 wins
            player2.extend(sorted(draws, reverse=True))
            # print(f'Round winned by {2}')
        else:
            raise

    if player1:
        # print('GAME WINNED BY 1')
        return 1, compute_score(player1)
    else:
        # print('GAME WINNED BY 2')
        return 2, compute_score(player2)


def part2(input):
    player1, player2 = deque(input[0]), deque(input[1])

    winner, score = recursive_combat(player1, player2)
    return score
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [306], part2, [291])
    main()