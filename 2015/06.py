from collections import defaultdict

TESTS1 = [
(["turn on 0,0 through 999,999"], 1000*1000),
(["toggle 0,0 through 999,0"], 1000),
(["turn off 499,499 through 500,500"], 0),
]

TESTS2 = [
(["turn on 0,0 through 0,0"], 1),
(["toggle 0,0 through 999,999"], 2000000),
]


VOWELS = "a e i o u".split(" ")
NOTSTRS = ["ab", "cd", "pq", "xy"]


def parseline(inputstr):
    inputstr = inputstr.replace('turn ', '')
    instr, range_s, _, range_f = inputstr.split()
    range_s = (int(range_s.split(',')[0]), int(range_s.split(',')[1])) 
    range_f = (int(range_f.split(',')[0]), int(range_f.split(',')[1])) 
    
    return instr, range_s, range_f


def part1(inputlst):
    lights = defaultdict(bool)
    for inputstr in inputlst:
        instr, range_s, range_f = parseline(inputstr)
        for i in range(range_s[0], range_f[0]+1):
            for j in range(range_s[1], range_f[1]+1):
                if instr == 'on':
                    lights[(i,j)] = 1
                elif instr == 'off':
                    lights[(i,j)] = 0
                elif instr == 'toggle':
                    lights[(i,j)] = not lights[(i,j)]



    return sum(lights.values())


def part2(inputlst):
    lights = defaultdict(int)
    for inputstr in inputlst:
        instr, range_s, range_f = parseline(inputstr)
        if instr == 'on':
            br = +1
        elif instr == 'off':
            br = -1
        elif instr == 'toggle':
            br = +2

        for i in range(range_s[0], range_f[0]+1):
            for j in range(range_s[1], range_f[1]+1):
                    lights[(i,j)] = max(lights[(i,j)]+br, 0)


    return sum(lights.values())


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
    inputlst = open('2015/inputs/2015_06.txt', 'r').read().strip().split('\n')
    print(f'Part 1: {part1(inputlst)}')
    print(f'Part 2: {part2(inputlst)}')

