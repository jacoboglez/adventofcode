'''
https://adventofcode.com/2017/day/7
'''
DAY = 7

from utils import *
from collections import Counter


def parser(test=False):
    return Input(DAY, 2017, test=test)


def structure(input):
    aboves = dict()
    belows = dict()
    weigths = dict()
    for line in input:
        match line.split(' '):
            case [program, weight]:
                weight = int(weight.strip('()'))
                above_programs = []

            case [program, weight, _, *above_programs]:
                weight = int(weight.strip('()'))
                for ap in above_programs:
                    belows[ap.strip(',')]= program
        
        weigths[program.strip(',')] = weight
        aboves[program.strip(',')] = [ap.strip(',') for ap in above_programs]
            
    return aboves, belows, weigths


def cumweight(program, aboves, weights):
    # if not aboves[program]:
    #     return weights[program]
    # sum = 0

    sum = weights[program]
    for p in aboves[program]:
        sum += cumweight(p, aboves, weights)

    return sum


def different_index(l):
    counts = Counter(l)
    for k, v in counts.items():
        if v == 1:
            return l.index(k)
    return -1


def check_imbalance(base, aboves, weights):
    ws = []
    for p in aboves[base]:
        ws.append(cumweight(p, aboves, weights))

    unbalanced_idx = different_index(ws)

    if unbalanced_idx == -1:
        # No imbalance with this base
        return -1

    first_inbalanced = aboves[base][unbalanced_idx]

    ws = []
    for p in aboves[first_inbalanced]:
        ws.append(cumweight(p, aboves, weights))
    
    unbalanced_idx_2 = different_index(ws)
    second_imbalanced = aboves[first_inbalanced][unbalanced_idx_2]
    if unbalanced_idx_2 == -1:
        # The imbalance was in the previous step
        # Find the correct weigth
        return correct_weigth(base, unbalanced_idx, aboves, weights)
    else: # The imbalance is higher up
        return check_imbalance(second_imbalanced, aboves, weights)


def correct_weigth(base, imbalanced_idx, aboves, weights):
    if imbalanced_idx == 0:
        balanced_prog = aboves[base][1]
    else:
        balanced_prog = aboves[base][0]

    imbalanced_prog = aboves[base][imbalanced_idx]
    good_weight = cumweight(balanced_prog, aboves, weights)
    wrong_weight =  cumweight(imbalanced_prog, aboves, weights)
    
    correction = good_weight - wrong_weight

    return weights[imbalanced_prog] + correction


def part1(input):
    aboves, belows, weights = structure(input)
    # weigths.keys() contains all programas
    # belows.keys() contain all programs with another below
    return (set(weights.keys()) - set(belows.keys())).pop()


def part2(input):
    base = part1(input)
    aboves, belows, weights = structure(input)

    return check_imbalance(base, aboves, weights)
    
    

def main():
    input = parser()

    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, ['tknk'], part2, [60])
    main()