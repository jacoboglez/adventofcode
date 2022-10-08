'''
https://adventofcode.com/2017/day/10
'''
DAY = 10

from utils import *
from collections import deque
from itertools import islice
from functools import reduce


SUFFIX = [17, 31, 73, 47, 23]


def parser(test=False):
    return Input(DAY, 2017, test=test)[0]


def reverse_left(rope, l):
    sublist = []
    for i in range(l):
        sublist.append(rope.popleft())
    
    rope.extendleft(sublist)
    return rope


def knottying(input, length=256, current=0, skipsize=0, rope=None):
    if not rope:
        rope = deque(range(length))

    rope.rotate(current)
    rot_count = current
    for l in input:
        # Reverse the first l elements of the rope
        reverse_left(rope, l)
        rope.rotate(-l-skipsize)
        rot_count += -l-skipsize
        skipsize += 1

    # Recover the original list order
    current = rot_count % length
    rope.rotate(-current)

    return rope, current, skipsize


def knothash(input):
    # Prepare the input: ASCII decoding and add suffix
    lengths = [ord(c) for c in input]
    lengths.extend(SUFFIX)

    # Do the hashing
    rope = deque(range(256))
    rot_count = 0
    skipsize = 0
    for _ in range(64):
        # rope, current, skipsize = knottying(lengths, current=current, skipsize=skipsize, rope=rope)

        for l in lengths:
            # Reverse the first l elements of the rope
            reverse_left(rope, l)
            rope.rotate(-l-skipsize)
            rot_count += -l-skipsize
            skipsize += 1

        # Recover the original list order
        rot_count = rot_count % 256
        
    rope.rotate(-rot_count)

    # Compute dense hash
    denses = []
    for i in range(16):
        chunk = islice(rope, i*16, (i+1)*16)
        denses.append(reduce(lambda a,b:a^b, chunk))

    chunks_hex = [f'{n:02x}' for n in denses]

    return ''.join(chunks_hex)


def part1(input, length=256):
    input = integers(input)

    rope, current, skipsize = knottying(input, length)

    # Put the rope into the current order
    # rope.rotate(current)
    # print(rope)
    # rope.rotate(-current)
    
    return rope[0]*rope[1]


def part2(input):
    return knothash(input)


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, lambda i: part1(i, 5), [12],
                      part2, [None, 
                    '33efeb34ea91902bb2f59c9920caa6cd',
                    '3efbe78a8d82f29979031a4aa0b16a9d',
                    '63960835bcdc130f0b66d7ff4f6a5a8e'])
    main()
    