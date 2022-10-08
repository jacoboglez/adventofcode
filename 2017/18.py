'''
https://adventofcode.com/2017/day/18
'''
DAY = 18


from re import RegexFlag
from utils import *
from collections import defaultdict, deque


def parser(test=False):
    return Input(DAY, 2017, test=test)


def value(REGISTERS, Y):
    if Y.strip('-').isnumeric():
        return int(Y)
    return REGISTERS[Y]


def cpu1(input):
    REGISTERS = defaultdict(int)
    current = 0
    play = None
    while True:
        instruction = input[current]
        match instruction.split(' '):
            # snd X plays a sound with a frequency equal to the value of X.
            case 'snd', X:
                play = value(REGISTERS, X)
            # set X Y sets register X to the value of Y.
            case 'set', X, Y:
                REGISTERS[X] = value(REGISTERS, Y)
            # add X Y increases register X by the value of Y.
            case 'add', X, Y:
                REGISTERS[X] += value(REGISTERS, Y)
            # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
            case 'mul', X, Y:
                REGISTERS[X] *= value(REGISTERS, Y)
            # mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
            case 'mod', X, Y:
                REGISTERS[X] = REGISTERS[X]%value(REGISTERS, Y)
            # rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
            case 'rcv', X:
                if REGISTERS[X]: 
                    return play
            # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero.
            case 'jgz', X, Y:
                if REGISTERS[X]:
                    current += value(REGISTERS, Y) - 1 # -1 to correct for the increase out the match
        
        current += 1


def exec_instruction(instruction, REGISTERS):
    delta_current = 1
    send = None
    match instruction.split(' '):
            # snd X sends the value of X to the other program
            case 'snd', X:
                send = value(REGISTERS, X)
            
            # set X Y sets register X to the value of Y.
            case 'set', X, Y:
                REGISTERS[X] = value(REGISTERS, Y)
            
            # add X Y increases register X by the value of Y.
            case 'add', X, Y:
                REGISTERS[X] += value(REGISTERS, Y)
            
            # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
            case 'mul', X, Y:
                REGISTERS[X] *= value(REGISTERS, Y)
            
            # mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
            case 'mod', X, Y:
                REGISTERS[X] = REGISTERS[X]%value(REGISTERS, Y)

            # rcv X receives the next value and stores it in register X.
            case 'rcv', X:
                if REGISTERS['QUEUE']:
                    REGISTERS[X] = REGISTERS['QUEUE'].popleft()
                else:
                    # Dont go to the next instruction until it reads a value
                    delta_current = 0
                
            # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero.
            case 'jgz', X, Y:
                if value(REGISTERS, X) > 0:
                    delta_current = value(REGISTERS, Y) 
    
    return REGISTERS, send, delta_current
        

def cpu2(input):
    REGISTERS_0 = defaultdict(int)
    REGISTERS_1 = defaultdict(int)

    REGISTERS_0['p'] = 0
    REGISTERS_1['p'] = 1

    REGISTERS_1['QUEUE'] = deque([])
    REGISTERS_0['QUEUE'] = deque([])

    current_0 = 0
    current_1 = 0

    counter = 0
    while True:
        # Execute an instruction in both programs
        REGISTERS_0, sent_to_1, delta_current_0 = exec_instruction(input[current_0], REGISTERS_0)
        REGISTERS_1, sent_to_0, delta_current_1 = exec_instruction(input[current_1], REGISTERS_1)

        # Recieve the sent messages
        if sent_to_0 != None: REGISTERS_0['QUEUE'].append(sent_to_0)
        if sent_to_1 != None: REGISTERS_1['QUEUE'].append(sent_to_1)

        # Count porgam 1 sent messages
        if sent_to_0 != None:
            counter += 1

        # Update the current instruction in both
        current_0 += delta_current_0
        current_1 += delta_current_1

        # Check for locks:
        # if both deltas are 0, they are both trying to receive without input
        if not delta_current_0 and not delta_current_1:
            return counter


def part1(input):
    return cpu1(input)


def part2(input):
    return cpu2(input)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [4], part2, [None, 3])
    main()