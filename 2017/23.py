'''
https://adventofcode.com/2017/day/23
'''
DAY = 23

from curses.ascii import isalpha
import sys
from time import time
sys.path.insert(0, '.')

from utils import *
from sympy import isprime


def parser(test=False):
    return [i.split(' ') for i in Input(DAY, 2017, test=test)]


def value(x, registers):
    if x.isalpha():
        return registers[x]
    else:
        return int(x)


def runProgram(program, registers=defaultdict(int)):
    i = 0

    times_mul = 0
    while i < len(program):
        instruction, x, y = program[i]
        
        if instruction == 'set':
            registers[x] = value(y, registers)
        elif instruction == 'sub':
            registers[x] -= value(y, registers)
        elif instruction == 'mul':
            registers[x] *= value(y, registers)
            times_mul += 1
        elif instruction == 'jnz':
            if value(x, registers) != 0:
                i += value(y, registers)
                i -=1 # Correct for the next line

        i += 1
        
    return registers['h'], times_mul


def part1(input):
    _, times_mul = runProgram(input)
    return times_mul


def program2_naive(b=107_900, c=124_900, jump=17):
    h = 0
    while b != c:
        f = 1
        d = 2
        while d != b:
            e = 2
            while e != b:
                if (d*e) == b:
                    f = 0
                e = e + 1
            d = d + 1
        if f == 0:
            h = h + 1
        b = b + jump

    return h


def program_2(b=107_900, c=124_900, jump=17):
    '''It counts the numbers that are not prime between b and c with step 17.'''
    not_primes = 0
    for n in range(b, c+1, jump):
        if not isprime(n):
            not_primes += 1

    return not_primes


def part2(input):
    # Remains to read the parameters form the input
    return program_2()
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [], part2, [])
    main()