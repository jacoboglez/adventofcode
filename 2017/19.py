'''
https://adventofcode.com/2017/day/19
'''
DAY = 19

'''
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 

'''


from os import walk
from utils import *


def parser(test=False):
    return Input(DAY, 2017, test=test, line_parser=lambda i:i)


def walk_tubes(input):
    # Find the start
    prev = '|'
    h = input[0].find('|')
    v = 0
    dh = 0
    dv = 1

    # Start walking
    found = []
    steps = 0
    while True:
        current = input[v][h]
        if (current == '+') and (prev == '|'):
            # Find horizontal
            if (h+1 < len(input[v])) and (input[v][h+1] != ' '):
                dh = 1
            elif (h-1 >= 0) and (input[v][h-1] != ' '):
                dh = -1
            dv = 0
            prev = '-'

        elif (current == '+') and (prev == '-'):
            # Find vertical
            if (v+1 < len(input)) and (input[v+1][h] != ' '):
                dv = 1
            elif (v-1 >=0) and (input[v-1][h] != ' '):
                dv = -1
            dh = 0
            prev = '|'

        elif current.isalpha():
            found.append(current)

        elif current == ' ':
            return ''.join(found), steps
        
        h += dh
        v += dv
        steps += 1


def part1(input):
    return walk_tubes(input)[0]


def part2(input):
    return walk_tubes(input)[1]
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, ['ABCDEF'], part2, [38])
    main()