'''
https://adventofcode.com/2019/day/14
'''

from utils import *
import re
import pprint
from collections import defaultdict
from math import ceil


def reactions(input): 
    comp_dict = {}
    for reaction in input:
        components = re.findall(r'(\d+) ([A-Z]+)', reaction)
        components = [ (int(comp[0]), comp[1]) for comp in components[::-1] ]
        # components_dict = {comp[0][1]: comp for comp in components}
        comp_dict[components[0][1]] = components
    
    # pprint.pprint(comp_dict)

    return comp_dict 


def part1(input, FUEL = 1):
    reactions_dict = reactions(input)
    
    predecesors_required = defaultdict(int)
    reactives_left = defaultdict(int)
    predecesors_required['FUEL'] += FUEL

    while True:
        reactives_required = [ *predecesors_required.keys() ]
        for reactive in reactives_required:
            if reactive == 'ORE':
                continue
            
            # print(f'Obtaining {reactive}')

            reactive_needed = predecesors_required[reactive] - reactives_left[reactive]

            if reactive_needed < 0:
                reactives_left[reactive] = -1*reactive_needed
                reactive_needed = 0

            reactive_produced_by_reaction = reactions_dict[reactive][0][0]

            reactions_required = ceil( reactive_needed/reactive_produced_by_reaction )

            reactives_left[reactive] = reactive_produced_by_reaction*reactions_required - reactive_needed

            # print(f'We need {reactive_needed}, {reactions_required} reactions ({reactives_left[reactive]} left).')

            # print('It adds:')
            predecesors = reactions_dict[reactive][1:] # [(1,A), (2,B)]
            for pred_reaction_quant, predecesor in predecesors:
                predecesors_required[predecesor] += reactions_required*pred_reaction_quant
                # print(f'{predecesor}: {reactions_required*pred_reaction_quant} (total: {predecesors_required[predecesor]})')

            # Clean that entry bc their predecessors were included
            del predecesors_required[reactive]

        # print(predecesors_required)
        # print(reactives_left)
        if len(predecesors_required.keys()) == 1 and list(predecesors_required.keys())[0] =='ORE':
            break

    return predecesors_required['ORE']



def part2(input):
    ORE = 1000000000000

    MAX_FUEL = 82892753 * 3
    MIN_FUEL = 0

    MAX_ORE_required = part1(input, MAX_FUEL)

    if MAX_ORE_required < ORE:
        print('We can produce more fuel. Increase maximum.')
        raise

    FUEL = MAX_FUEL // 2
    while True:
        FUEL_ANT = FUEL
        ORE_required = part1(input, FUEL)

        if ORE_required < ORE:
            # we can produce more fuel
            MIN_FUEL = FUEL
        else:
            # we can not produce that much fuel with our ORE
            MAX_FUEL = FUEL
        
        FUEL = (MAX_FUEL + MIN_FUEL) // 2

        if FUEL == FUEL_ANT:
            break
        
    #     print(f'MAX: {MAX_FUEL}')
    #     print(f'MIN: {MIN_FUEL}')
    #     print(f'FUEL: {FUEL}')
    #     print(f' ')

    # print(FUEL)
    return FUEL


def test():
    # Test number:       1    2      3       4        5
    tests_ORE_result = [31, 165, 13312, 180697, 2210736]

    print('Part 1:')
    for test_i, ORE_result in enumerate(tests_ORE_result, 1):
        input = Input(14, 2019, test=test_i)
        ORE = part1(input)
        assert ORE_result == ORE
        print(f'Test {test_i} CORRECT')
    
    print('-----------------------------------------')
    print(' ')
    print('Part 2:')

    # Test number:              3        4       5
    tests_FUEL_result = [82892753, 5586022, 460664]

    for test_i, FUEL_result in enumerate(tests_FUEL_result, 3):
        input = Input(14, 2019, test=test_i)
        FUEL = part2(input)
        assert FUEL_result == FUEL
        print(f'Test {test_i} CORRECT')
    

def main():
    input = Input(14, 2019)
    ORE = part1(input)
    print(ORE)
    print(' ')

    input = Input(14, 2019)
    FUEL = part2(input)
    print(FUEL)


if __name__ == "__main__":
    main()