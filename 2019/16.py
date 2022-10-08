'''
https://adventofcode.com/2019/day/16
'''

from utils import *
import numpy as np


BASE_PATTERN = [0, 1, 0, -1]
REPEAT_INPUT = 10000


def Input16(test=False):
    return Input(16, 2019, line_parser=lambda x: [int(n) for n in list(x)], test=test)[0]


def n_pattern(n):
    pattern = []
    for p in BASE_PATTERN:
        pattern.extend([p]*n)

    # Rotate
    pattern.append(pattern[0])
    del pattern[0]

    return pattern


def n_factors(n):
    t = 1
    position = 0
    base_length = len(BASE_PATTERN)

    while True:
        for p in range(t, n):
            yield BASE_PATTERN[position]
        position += 1
        position = position % base_length
        t = 0


def compute_phase(sequence):
    sequence_out = []
    a = np.array(sequence)
    for i, _ in enumerate(sequence, 1):
        factors = n_factors(i)
        v = np.array( [next(factors) for _ in range(len(sequence))] )
        r = np.dot(a, v)
        sequence_out.append(abs(r)%10)

    return sequence_out


def decode_message(sequence, n_phases = 100):
    backward_sequence = sequence[::-1]

    for p in range(n_phases):
        # Using the trick of partial sums
        backward_out_sequence = []
        total = 0
        for s in backward_sequence:
            total += s
            backward_out_sequence.append(total%10)
        backward_sequence = [ *backward_out_sequence ]

    return backward_out_sequence[::-1]


def part1(sequence, n_phases=100):
    for p in range(1, n_phases+1):
        # print(f'Phase {p}')
        sequence = compute_phase(sequence)
        # print(sequence)  

    return ''.join( [ str(n) for n in sequence] )


def part2(input):
    sequence = input*REPEAT_INPUT
    # print('Sequence in memory.')

    # Compute messae offset
    message_offset = int( ''.join( [ str(d) for d in input[:7] ] ) )
    # print(message_offset)

    if message_offset < (len(input)*REPEAT_INPUT) // 2:
        # The message is not in the patern section
        raise

    message_to_end = sequence[message_offset:]
    decoded_message_to_end = decode_message(message_to_end)

    # print(decoded_message_to_end[:8])
    return ''.join( [ str(n) for n in decoded_message_to_end[:8] ] )
    

def main():
    # Part 1
    assert part1(Input16(test=1), n_phases = 4) == '01029498'
    print('Test 1: OK')
    assert part1(Input16(test=2))[:8] == '24176176' # Test 2
    print('Test 2: OK')
    assert part1(Input16(test=3))[:8] == '73745418' # Test 3
    print('Test 3: OK')
    assert part1(Input16(test=4))[:8] == '52432133' # Test 4
    print('Test 4: OK')

    result_1 = part1(Input16())
    print(f'Part 1: {result_1[:8]}')
    print()

    # Part 2
    assert part2(Input16(test=5)) == '84462026' # Test 5
    print('Test 5: OK')
    assert part2(Input16(test=6)) == '78725270' # Test 6
    print('Test 6: OK')
    assert part2(Input16(test=7)) == '53553731' # Test 7
    print('Test 7: OK')

    result_2 = part2(Input16())
    print(f'Part 2: {result_2}')
    print()


if __name__ == "__main__":
    main()