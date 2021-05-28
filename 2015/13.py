from collections import defaultdict
from itertools import permutations

TESTS1 = [
('''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
'''.strip().split('\n'), 330),
]


def parseRelations(inputlst):
    relations = defaultdict(dict)
    for inputstr in inputlst:
        inputstr = inputstr.strip('.')
        inputstr = inputstr.replace('happiness units by sitting next to ', '')
        inputstr = inputstr.replace('gain ', '+')
        inputstr = inputstr.replace('lose ', '-')
        [A, _, hu, B] = inputstr.split()
        relations[A][B] = int(hu)

    return relations


def computeHappiness(arrangement, relations):
    happ = 0
    for i, s in enumerate(arrangement):
        happ += relations[s][ arrangement[i-1] ]
        happ += relations[s][ arrangement[(i+1)%len(arrangement)] ]

    return happ


def part1(relations):
    atendees = relations.keys()

    max_happ = -float('inf')
    for arrangement in permutations(atendees):
        happ = computeHappiness(arrangement, relations)
        if happ > max_happ:
            max_happ = happ
            # max_arr = arrangement

    # print(max_arr)
    return max_happ


def part2(relations):
    '''I think it could be done trying to insert "Me" in every position 
    possible of the optimal combination obtained from part1. '''
    atendees = list(relations.keys())

    for a in atendees:
        relations[a]['Me'] = 0
        relations['Me'][a] = 0

    return part1(relations)


def test():
    for inp, res in TESTS1:
        if part1(parseRelations(inp)) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputlst = open('2015/inputs/13.txt', 'r').read().strip().split('\n')
    relations = parseRelations(inputlst)
    print(f'Part 1: {part1(relations)}')
    print(f'Part 1: {part2(relations)}')
