'''
https://adventofcode.com/2020/day/8
'''
DAY = 8

from utils import *


def parser(test=False):
    raw_input = Input(DAY, 2020, test=test)
    return [ ( i.split(' ')[0], int(i.split(' ')[1]) ) for i in raw_input]


def run(program):
    accumulator = 0
    instruction = 0
    executed_instructions = set([])

    while True:
        if instruction in executed_instructions:
            # Terminated because loop
            return accumulator, 1
        if instruction >= len(program):
            # Terminated correctly
            return accumulator, 0

        operation, argument = program[instruction]
        executed_instructions.add(instruction)

        if operation == 'acc':
            accumulator += argument
            instruction += 1
        elif operation == 'jmp':
            instruction += argument
        elif operation == 'nop':
            instruction += 1
        else:
            raise ValueError(f'Unexpected operation: {operation}')
            
            
def part1(input):
    return run(input)[0]


def part2(input):
    for i, (op, ar) in enumerate(input):
        mod_program = list(input) # Copy the original program

        if op == 'jmp':
            mod_program[i] = ('nop', ar)
        elif op == 'nop':
            mod_program[i] = ('jmp', ar)
        else:
            continue

        accumulator, exit_code = run(mod_program)

        if not exit_code:
            return accumulator
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [5], part2, [8])
    main()