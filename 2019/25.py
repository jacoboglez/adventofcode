'''
https://adventofcode.com/2019/day/25
'''
DAY = 25

from utils import *
from icc import intCodeComputer


def parser(test=False):
    return Input(DAY, 2021, test=test)


def part1(program, verbose=True):
    software = intCodeComputer(program, id=1, verbose=False)

    # Uncomment next line to play the game interactively
    # software.interactiveRun()
    
    # Read the comments from the instruction .txt file and play them automatically
    raw_instructions = mapt(str.strip, open(f'2019/25_instructions.txt'))
    # Remove the comments (preceded by "#")
    instructions = [inst.split('#')[0].strip() for inst in raw_instructions]

    # Start the program
    software.compute()

    for inst in instructions:
        if verbose:
            software.outputASCII()

        software.inputArray = [ord(a) for a in inst+'\n']
        software.compute()
    

def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])

    part1(program)


if __name__ == "__main__":
    main()
