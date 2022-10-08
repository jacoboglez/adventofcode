'''
https://adventofcode.com/2017/day/13
'''
DAY = 13


from utils import *


def parser(test=False):
    input = Input(DAY, 2017, test=test)
    firewall = {}
    for line in input:
        layer, range = line.split(': ')
        firewall[int(layer)] = int(range) # 0 index for modular arithmetic
    return firewall


def mod1(i, m):
    ''' Compute modulo starting at one (1, 2, 3, ..., m):
        mod1(1,m) = 1
        mod1(m,m) = m
        mod1(m+2,m) = 2'''
    return (i-1) % m+1


def part1(firewall):
    counter = 0
    for p in firewall.keys():
        # Position of the S in layer p in picosecond p
        # To account for the return trip for the end I add the 
        # range again -1
        # Since the final step is the starting squeare I substract one again.
        S = mod1(p+1, firewall[p]*2-1-1)

        # Check if the S is in our position
        if S == 1:
            counter += p * firewall[p]

    return counter
    

def detected(firewall, t=0):
    for p in firewall.keys():

        # Position of the S in layer p in picosecond p
        # To account for the return trip for the end I add the 
        # range again -1
        # Since the final step is the starting squeare I substract one again.
        S = mod1(t+p+1, firewall[p]*2-1-1)

        # Check if the S is in our position
        if S == 1:
            return True
    return False
        

def part2(firewall):
    '''I think it could be optimized usign the Chinise Remainder Theorem.'''
    t = 0
    while detected(firewall, t):
        t += 1
    return t


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [24], part2, [10])
    main()