from itertools import groupby


def countFirstEquals(s):
    count = 0
    for c in s:
        if c == s[0]:
            count += 1
        else:
            break
    return count, s[0]


def part1(inputstr, N):
    for _ in range(N):
        newstr = ''
        while inputstr:
            c, d = countFirstEquals(inputstr)
            newstr += str(c) + d
            inputstr = inputstr[c:]
        inputstr = newstr

    return newstr


def part2(inputstr, N):
    for i in range(N):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(inputstr)])
    return input_string


if __name__ == "__main__":
    inputstr = open('2015/inputs/10.txt', 'r').read().strip().split('\n')[0]
    print(f'Part 1: {len(part1(inputstr, 40))}')
    print(f'Part 2: {len(part2(inputstr, 50))}')
