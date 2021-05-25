
TESTS1 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''.split('\n')

TEST1_RES = {
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456,
}


def getval(A, mem):
    if A.isnumeric():
        return int(A)
    else:
        return mem[A]


def part12(inputlst, valA=None):

    if not valA:
        mem = dict()
    else:
        mem = {'b':valA}

    failed_instructions = inputlst.copy()

    while failed_instructions:
        instructions = failed_instructions.copy()
        failed_instructions = []

        for inputstr in instructions:
            # print(inputstr)
            try:
                match inputstr.split():
                    case [A, '->', C]:
                        if valA and (C == "b"): # For part 2
                            continue
                        mem[C] = getval(A, mem)

                    case [A, 'AND', B, '->', C]:
                        mem[C] = (getval(A, mem) & getval(B, mem))%2**16

                    case [A, 'OR', B, '->', C]:
                        mem[C] = (getval(A, mem) | getval(B, mem))%2**16

                    case [A, 'LSHIFT', val, '->', C]:
                        mem[C] = (getval(A, mem) << int(val))%2**16

                    case [A, 'RSHIFT', val, '->', C]:
                        mem[C] = (getval(A, mem) >> int(val))%2**16

                    case ['NOT', A, '->', C]:
                        mem[C] = (~getval(A, mem))%2**16
            except KeyError:
                failed_instructions.append(inputstr)

    return mem


def test():
    mTest1 = part12(TESTS1)
    if mTest1 != TEST1_RES:
        raise AssertionError
    
    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputlst = open('2015/inputs/07.txt', 'r').read().strip().split('\n')
    valA = part12(inputlst)["a"]
    print(f'Part 1: {valA}')
    print(f'Part 2: {part12(inputlst, valA)["a"]}')
