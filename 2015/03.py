TESTS1 = [
(">", 2),
("^>v<", 4),
("^v^v^v^v^v", 2)]

TESTS2 = [
("^v", 3),
("^>v<", 3),
("^v^v^v^v^v", 11)]

DIR = {
">": 1,
"<": -1,
"^": 1j,
"v": -1j
}


def part1(inputstr):
    house = 0 + 0j
    visited = {house}

    for d in inputstr:
        house += DIR[d]
        visited.add(house)

    return len(visited)


def part2(inputstr):
    santa = 0 + 0j
    robosanta = 0 + 0j
    visited = {santa, robosanta}

    for d in inputstr[::2] :
        santa += DIR[d]
        visited.add(santa)
    for d in inputstr[1::2] :
        robosanta += DIR[d]
        visited.add(robosanta)
    return len(visited)


def test():
    for inp, res in TESTS1:
        if part1(inp) != res:
            raise AssertionError

    # for inp, res in TESTS2:
    #     if part2(inp) != res:
    #         raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputstr = open('2015/inputs/03.txt', 'r').read().strip()
    print(f'Part 1: {part1(inputstr)}')
    # print(f'Part 2: {part2(inputstr)}')