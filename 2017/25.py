'''
https://adventofcode.com/2017/day/25
'''
DAY = 25

from cmath import nan
from curses import raw
import sys
sys.path.insert(0, '.')
from utils import *
from collections import namedtuple, defaultdict
import re


def parser(test=False):
    raw_input = '\n'.join(Input(DAY, 2017, test=test))

    initial_state = re.search(r'Begin in state (\w).', raw_input).group(1)
    N_steps = int(re.search(r'checksum after (\d+) steps.', raw_input).group(1))

    re_PA = r'In state (\w):\n' + \
            r'.+value is (\d):\n' + \
            r'.+the value (\d).\n' + \
            r'.+to the (\w+).\n' + \
            r'.+with state (\w).\n' + \
            r'.+value is (\d):\n' + \
            r'.+the value (\d).\n' + \
            r'.+to the (\w+).\n' + \
            r'.+with state (\w).'

    instructions_parameters = re.findall(re_PA, raw_input)

    # Build the instructions dictionary
    instructions = dict()
    blueprint = namedtuple('blueprint', 'to_write to_move next_state')

    for state_instructions in instructions_parameters:
        current_state = state_instructions[0]

        instructions[current_state] = dict()
        for v in range(2):
            current_value = int(state_instructions[1+4*v])
            to_write = int(state_instructions[2+4*v])
            to_move = 1 if state_instructions[3+4*v] == 'right' else -1
            next_state = state_instructions[4+4*v]

            instructions[current_state][current_value] = blueprint(to_write, to_move, next_state)

    return instructions, initial_state, N_steps


def turingMachine(instructions, initial_state, N_steps):
    state = initial_state
    tape = defaultdict(int)
    cursor = 0
    for _ in range(N_steps):
        current_value = tape[cursor]
        to_write, to_move, next_state = instructions[state][current_value]
        tape[cursor] = to_write
        cursor += to_move
        state = next_state

    return tape


def part1(input):
    instructions, initial_state, N_steps = input
    tape = turingMachine(instructions, initial_state, N_steps)

    # Do the checksum
    checksum = 0
    for v in tape.values():
        checksum += v

    return checksum


def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')


if __name__ == "__main__":
    test(DAY, parser, part1, [3], part2, [])
    main()
    