TESTS1 = [
("ugknbfddgicrmopn", True),
("aaa", True),
("jchzalrnumimnmhp", False),
("haegwjzuvuyypxyu", False),
("dvszwmarrgswjxmb", False),
]

TESTS2 = [
("qjhvhtzxzqqjkmpb", True),
("xxyxx", True),
("uurcxstgmygtbstg", False),
("ieodomkazucvgmuy", False),
]


VOWELS = "a e i o u".split(" ")
NOTSTRS = ["ab", "cd", "pq", "xy"]


def isnice(inputstr):
    # Contains three vowels
    if sum( inputstr.count(v) for v in VOWELS ) < 3:
        return False

    # Contains at least one letter that appears twice in a row
    for c1, c2 in zip(inputstr[:-1], inputstr[1:]):
        if c1 == c2:
            break
    else: #nobreak
        return False

    # It does not contain the strings ab, cd, pq, or xy
    if sum( n in inputstr for n in NOTSTRS ) > 0:
        return False
    
    return True


def isverynice(inputstr):
    # It contains a pair of any two letters that appears at least twice 
    # in the string without overlapping
    for i in range(len(inputstr)-1):
        if inputstr.count(inputstr[i:i+2]) >= 2:
            break
    else: #nobreak
        return False

    # It contains at least one letter which repeats with exactly one 
    # letter between them, like xyx,
    for c1, c3 in zip(inputstr[:-2], inputstr[2:]):
        if c1 == c3:
            break
    else: #nobreak
        return False

    return True


def part1(inputlst):
    return sum( isnice(inputstr) for inputstr in inputlst )


def part2(inputlst):
    return sum( isverynice(inputstr) for inputstr in inputlst )


def test():
    for inp, res in TESTS1:
        if isnice(inp) != res:
            raise AssertionError

    for inp, res in TESTS2:
        if isverynice(inp) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputlst = open('2015/inputs/05.txt', 'r').read().strip().split('\n')
    print(f'Part 1: {part1(inputlst)}')
    print(f'Part 2: {part2(inputlst)}')

