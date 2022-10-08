'''
https://adventofcode.com/2017/day/16
'''
DAY = 16


from utils import *
from collections import deque
from string import ascii_lowercase
import re


N = 1_000_000_000


def parser(test=False):
    return Input(DAY, 2017, test=test)[0].split(',')


def swap(l, p1, p2):
    # Order the positiops
    if p2 < p1: p1, p2 = p2, p1
    # Get the values
    v1, v2 = l[p1], l[p2]
    # Remove the values
    l.remove(v1)
    l.remove(v2)
    # Insert them in swapped positions
    l.insert(p1, v2)
    l.insert(p2, v1)

    return l


def dance(input, l):
    for i in input:
        if n := re.match(r's(\d+)', i):
            l.rotate(int(n.group(1)))
        
        elif m := re.match(r'x(\d+)/(\d+)', i):
                p1, p2 = m.groups()
                swap(l, int(p1), int(p2))

        elif m := re.match(r'p(\w)/(\w)', i):
            a,b = m.groups()
            p1 = l.index(a)
            p2 = l.index(b)
            swap(l, p1, p2)

    return l


def part1(input, nprogs=16, l=None):
    l = deque(ascii_lowercase[:nprogs])
    l = dance(input, l)

    return ''.join(l)


def part2(input):
    initial_config = deque(ascii_lowercase[:16])
    l = deque(ascii_lowercase[:16])
    seen = set()
    # Find the first time a configuration goes to the starting point
    l = dance(input, l=l)
    d = 1
    while True:
        l = dance(input, l=l)
        d +=1
        if l == initial_config:
            break
    
    # We only have to compute the last dances after the last time the 
    # programs return to the initial configuration (the remainder of N / d)
    for _ in range(N%d):
        l = dance(input, l=l)

    return ''.join(l)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, lambda i: part1(i, nprogs=5), ['baedc'], 
        part2, [])
    main()