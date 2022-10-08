from hashlib import md5

TESTS1 = [
("abcdef", 609043),
("pqrstuv", 1048970),]


def part1(inputstr):
    '''2357000 too high '''
    i = 0
    while md5(f'{inputstr}{i}'.encode()).hexdigest()[:5] != "00000":
        i += 1

    return i


def part2(inputstr):
    i = 0
    while md5(f'{inputstr}{i}'.encode()).hexdigest()[:6] != "000000":
        i += 1

    return i


def test():
    for inp, res in TESTS1:
        if part1(inp) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputstr = open('2015/inputs/2015_04.txt', 'r').read().strip()
    print(f'Part 1: {part1(inputstr)}')
    print(f'Part 2: {part2(inputstr)}')