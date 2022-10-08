'''
https://adventofcode.com/2019/day/21
'''
DAY = 21

from utils import *
from icc import intCodeComputer
# from itertools import count

# Part 1:
# Jump if there is a space in the next three tiles but the
# fourth tile (where it lands) has floor.
SCRIPT1 = '\n'.join([
'NOT A T',
'NOT B J',
'OR T J',
'NOT C T',
'OR T J',
'AND D J',
'WALK',
''])

# Part 2:
# Jump if there is a space in the next three tiles but the
# fourth tile (where it lands) has floor.
# Also we can jump if H has floor (two consecutive jumps)
# or if either E & I have floor (jump to D, move to E and jump to I)
# or if E & F have floor (move from D to F)
# H or ( (I or F) and E ) == H or ( (E and I) or (E and F) )
SCRIPT2 = '\n'.join([
'NOT A T', 
'NOT B J',
'OR T J',
'NOT C T',
'OR T J', 
'AND D J', 
'OR J T', # Second part
'OR I T',
'OR F T',
'AND E T',
'OR H T',
'AND T J',
'RUN',
''])


def to_ascii(ints):
    return ''.join( [chr(i) if i < 1114112 else str(i) for i in ints] )


def to_ints(ascii):
    return [ord(a) for a in ascii]


def springdroid(program, springscript, verbose=False):
    software = intCodeComputer(program, id=1, verbose=False)

    springscript = to_ints(springscript)

    software.compute()
    software.inputArray.extend( springscript )
    software.compute()

    if verbose: print( to_ascii(software.outputArray) )
    return software.outputArray[-1]
     

def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])
    
    result_1 = springdroid(program, SCRIPT1)
    print(f'Part 1: {result_1}')

    print('')
    result_2 = springdroid(program, SCRIPT2)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()