from functools import reduce


TESTS1 = [
("2x3x4", 58),
("1x1x10", 43)]

TESTS2 = [
("2x3x4", 34),
("1x1x10", 14) ]


def surface(inputstr):
    l, w, h = [int(a) for a in inputstr.split("x")]
    a = (l*w, w*h, h*l)
    return 2*sum(a) + min(a)


def ribbon(inputstr):
    sides = [int(a) for a in inputstr.split("x")]
    return reduce(lambda a,b: a*b, sides) + 2*sum(sorted(sides)[:2])


def part1(inputlst):
    return sum(surface(inputstr) for inputstr in inputlst)


def part2(inputlst):
    return sum(ribbon(inputstr) for inputstr in inputlst)


def test():
    for inp, res in TESTS1:
        if surface(inp) != res:
            raise AssertionError

    for inp, res in TESTS2:
        if ribbon(inp) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputlst = open('2015/inputs/2015_02.txt', 'r').read().strip().split("\n")
    print(f'Part 1: {part1(inputlst)}')
    print(f'Part 2: {part2(inputlst)}')