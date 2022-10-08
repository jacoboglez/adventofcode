from collections import defaultdict
from itertools import permutations

TESTS1 = [
('''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''.split('\n'), 605),
]

TESTS2 = [
('''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''.split('\n'), 982),
]


def parseDistances(inputlst):
    distances = defaultdict(dict)
    for inputstr in inputlst:
        [A, _, B, _, dist] = inputstr.split()
        distances[A][B] = int(dist)
        distances[B][A] = int(dist)

    return distances


def totalDistance(itinerary, distances):
    total = 0
    for A, B in zip(itinerary[:-1], itinerary[1:]):
        total += distances[A][B]

    return total


def part1(inputlst):
    distances = parseDistances(inputlst)
    locations = list(distances.keys())
    # Bruteforce
    record_distance = float('inf')
    for itinerary in permutations(locations):
        dist = totalDistance(itinerary, distances)
        if dist < record_distance:
            record_distance = dist
            # record_itinerary = itinerary

    # print(record_itinerary)
    return record_distance


def part2(inputlst):
    distances = parseDistances(inputlst)
    locations = list(distances.keys())
    # Bruteforce
    record_distance = 0
    for itinerary in permutations(locations):
        dist = totalDistance(itinerary, distances)
        if dist > record_distance:
            record_distance = dist
            # record_itinerary = itinerary

    # print(record_itinerary)
    return record_distance


def test():
    for inp, res in TESTS1:
        if part1(inp) != res:
            raise AssertionError

    for inp, res in TESTS2:
        if part2(inp) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputlst = open('2015/inputs/2015_09.txt', 'r').read().strip().split('\n')
    print(f'Part 1: {part1(inputlst)}')
    print(f'Part 2: {part2(inputlst)}')
