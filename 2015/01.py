
TESTS1 = [
("(())", 0),
("()()", 0),
("(((", 3),
("(()(()(", 3),
("))(((((", 3),
("())", -1),
("))(", -1),
(")))", -3),
(")())())", -3) ]

TESTS2 = [
(")", 1),
("()())", 5) ]


def part1(inputstr):
    return inputstr.count("(") - inputstr.count(")")


def part2(inputstr):
    pos = 0
    floor = 0
    for i, _ in enumerate(inputstr):
        f = part1(inputstr[:i+1])
        if f < 0: return i+1


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
    inputstr = open('2015/inputs/2015_01.txt', 'r').read().strip()
    print(f'Part 1: {part1(inputstr)}')
    print(f'Part 2: {part2(inputstr)}')