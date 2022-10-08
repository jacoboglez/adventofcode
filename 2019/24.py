'''
https://adventofcode.com/2019/day/24
'''
DAY = 24

from utils import *
import numpy as np
from scipy import ndimage
from collections import deque
from time import time


KERNEL = np.array([[0,1,0],[1,0,1],[0,1,0]])
MINUTES = 200


def parse_input(input):
    state = []
    
    for line in input:
        row = []
        for c in line:
            if c == '.':
                row.append(0)
            elif c == '#':
                row.append(1)
            else:
                raise ValueError('Unexpected tile.')

        state.append(row)

    return np.array(state)


def print_state(state):
    bugs = ''
    for row in state:
        for c in row:
            bugs += '#' if c else '.'
        bugs += '\n'

    print(bugs)


def update(state):
    new_state = np.zeros([np.size(state, 0), np.size(state, 0)], dtype = int) 

    adjacents = ndimage.convolve(state, KERNEL, mode='constant', cval=0.0)

    # Bugs that stay alive
    new_state += state & (adjacents == 1)

    # Bugs that appear
    new_state += np.logical_not(state) & ( (adjacents == 1) | (adjacents == 2) )

    return new_state


def biodiverisy_rating(state):
    indices = np.nonzero(state.flatten())

    return sum([2**i for i in indices[0]])


def recursive_adjacents(recursive_states, level):
    rec_adjacents = np.zeros([np.size(recursive_states[0], 0), np.size(recursive_states[0], 0)], dtype = int)

    # Adjacents from the exterior grid (level - 1)
    if level - 1 >= 0:
        # Top row
        rec_adjacents[0,:] += recursive_states[level-1][1,2]
        # Right column
        rec_adjacents[:,-1] += recursive_states[level-1][2,3]
        # Bottom row
        rec_adjacents[-1,:] += recursive_states[level-1][3,2]
        # Left column
        rec_adjacents[:,0] += recursive_states[level-1][2,1]

    # Adjacents from the interior grid (level + 1)
    if level + 1 < len(recursive_states):
        # Top row
        rec_adjacents[1,2] += sum(recursive_states[level+1][0,:])
        # Right column
        rec_adjacents[2,3] += sum(recursive_states[level+1][:,-1])
        # Bottom row
        rec_adjacents[3,2] += sum(recursive_states[level+1][-1,:])
        # Left column
        rec_adjacents[2,1] += sum(recursive_states[level+1][:,0])

    return rec_adjacents


def update_recursively(recursive_states):

    new_state = np.zeros([np.size(recursive_states[0], 0), np.size(recursive_states[0], 0)], dtype = int) 

    # Add another recursive level on top and bottom if those levels are not empty
    if np.count_nonzero(recursive_states[0]): # Level 0 is nonzero
        recursive_states.appendleft( np.array(new_state, copy=True) )
    if np.count_nonzero(recursive_states[-1]): # Level -1 is nonzero
        recursive_states.append( np.array(new_state, copy=True) )

    # Clean list of states for the new step
    new_recursive_states = deque( [np.array(new_state, copy=True) for _ in recursive_states] )

    for level, (state, new_state) in enumerate(zip(recursive_states, new_recursive_states)):
        adjacents = ndimage.convolve(state, KERNEL, mode='constant', cval=0.0)
        # Add the adjacents from recursive levels
        adjacents += recursive_adjacents(recursive_states, level)

        # Bugs that stay alive
        new_state += state & (adjacents == 1)

        # Bugs that appear
        new_state += np.logical_not(state) & ( (adjacents == 1) | (adjacents == 2) )

        # Put to 0 the recursive cell
        new_state[2,2] = 0



    return new_recursive_states


def part1(input):
    seen = set([])

    state = parse_input(input)

    t = 0
    while True:
        # print(f'Step {t}:')
        # print_state(state)

        state_hash = hash(str(state))
        if state_hash in seen:
            # print_state(state)
            break
        else:
            seen.add(state_hash)

        state = update(state)
        t += 1

    # print(t)
    return biodiverisy_rating(state) 


def part2(input, verbose=False):
    state = parse_input(input)
    recursive_states = deque([state])
    if verbose: print('Initial state:')
    if verbose: print_state(state)

    for t in range(MINUTES):
        recursive_states = update_recursively(recursive_states)

        # # Print all states
        # print(f'Step {t+1}:')
        # for state in recursive_states:
        #     if np.count_nonzero(state):
        #         print_state(state)

    return sum( [np.count_nonzero(state) for state in recursive_states] )


def test():
    # Test number:
    tests_results = [2129920]

    print('Part 1:')
    for test_i, test_result in enumerate(tests_results, 1):
        input = Input(DAY, 2019, test=test_i)
        result = part1(input)
        assert result == test_result
        print(f'Test {test_i} CORRECT')
    
    # print('-----------------------------------------')
    # print(' ')
    # print('Part 2:')

    # # Test number:   
    # tests_results_2 = []

    # for test_i, test_result in enumerate(tests_results_2, 1):
    #     input = Input(DAY, 2019, test=test_i)
    #     result = part2(input)
    #     assert result == test_result
    #     print(f'Test {test_i} CORRECT')
    

def main():
    input = Input(DAY, 2019, test=False)

    tic = time()
    result_1 = part1(input)
    toc = time()
    print(f'Part 1: {result_1}')
    print(f'(t = {toc-tic:.4f} secods)')

    print()

    tic = time()
    result_2 = part2(input)
    toc = time()
    print(f'Part 2: {result_2}')
    print(f'(t = {toc-tic:.4f} secods)')
    

if __name__ == "__main__":
    main()