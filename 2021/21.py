'''
https://adventofcode.com/2021/day/21
'''
DAY = 21

BOARDSIZE = 10


from utils import *
from functools import lru_cache


def parser(test=False):
    input = Input(DAY, 2021, test=test, line_parser=integers)
    return [input[0][1],  input[1][1]]


def part1(positions):
    positions = positions.copy()
    scores = [0, 0]

    die = 1
    while True:
        # Player 1
        total_die = 3*die + 3
        die += 3
        positions[0] = mod1(positions[0]+total_die, BOARDSIZE)
        scores[0] += positions[0]
        if scores[0] >= 1000:
            break

        # Player 2
        total_die = 3*die + 3
        die += 3
        positions[1] = mod1(positions[1]+total_die, BOARDSIZE)
        scores[1] += positions[1]
        if scores[1] >= 1000:
            break

    return min(scores) * (die-1)


@lru_cache(maxsize=None)
def dirac_dice(positions, scores, turn):
    p = turn > 2 # Player number (0 or 1)
    pos = list(positions)

    delta_scores = [0, 0]
    wins = [0, 0]
    newscores = scores

    # Create three universes
    for d in range(1,4):
        newpos = pos.copy()
        newpos[p] = mod1(pos[p]+d, BOARDSIZE)
        if (turn == 2) or (turn == 5):
            # Three rolls have been thrown: udpate scores
            delta_scores[p] = newpos[p]
            newscores = addc(scores, delta_scores)

            if (newscores[0] >= 21):
                wins = addc(wins, (1, 0))
                continue

            if (newscores[1] >= 21):
                wins = addc(wins, (0, 1))
                continue

        # No winner, another roll needed
        wins = addc(wins, dirac_dice(tuple(newpos), newscores, (turn + 1) % 6))

    return wins


def part2(positions):
    return max(dirac_dice(tuple(positions), (0,0), 0))
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [739785], part2, [444356092776315])
    main()