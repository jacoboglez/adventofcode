'''
https://adventofcode.com/2019/day/10
'''
DAY = 10

BIG = 9999999999
MAX_DESTROY = 200

from utils import *
from math import gcd, atan2, pi
from collections import deque

def detect_asteroids(asteroid, asteroid_coordinates):
    '''Returns the asteroids seen from a point with the coordinates relative to that point.'''
    asteroid = (0, 0)
    detected_ms = set([])
    detected_asteroids_dict = dict()

    for other in asteroid_coordinates:
        m_other = m(asteroid, other) 
        if m_other not in detected_ms:
            detected_ms.add( m_other )
            detected_asteroids_dict[m_other] = (other[0]-asteroid[0], other[1]-asteroid[1])
        else: # If that direction was detected
            prior_distance = abs(detected_asteroids_dict[m_other][0]) + \
                             abs(detected_asteroids_dict[m_other][1])

            if ( abs(other[0]-asteroid[0]) + abs(other[1]-asteroid[1]) ) < prior_distance:
                detected_asteroids_dict[m_other] = (other[0]-asteroid[0], other[1]-asteroid[1])

    detected_asteroids = list( detected_asteroids_dict.values() )
    # detected_asteroids.remove( (0.0, 0.0) )

    return detected_asteroids


def part1(input):
    asteroid_coordinates = asteroid_positions(input)

    record_detect = 0
    record_asteroid = (-1, -1)
    for asteroid in asteroid_coordinates:
        detected_ms = set([])
        for other in asteroid_coordinates:
            detected_ms.add( m(asteroid, other) )

        detected = len(detected_ms)
        if record_detect < detected:
            record_detect = detected
            record_asteroid = asteroid

    # We substract 1 to the record because it detects itself
    return record_detect-1, record_asteroid


def sort_angle(a):
    angle = atan2(a[1], a[0]) + pi/2
    return angle if angle >= 0 else angle+2*pi


def part2(input, my_ast):
    asteroid_coordinates = asteroid_positions(input)

    # Use coordinates relative to my_ast
    asteroid_relatives = [ (a[0]-my_ast[0], a[1]-my_ast[1]) for a in asteroid_coordinates ]
    asteroid_relatives.remove( (0, 0) )


    # seen_asteroids = list( detect_asteroids(my_ast, asteroid_relatives) )
    # seen_asteroids.sort( key = lambda a: atan2(a[1], a[0]) )
    # rotated_asteroids = deque(seen_asteroids)
    # while rotated_asteroids[0][0] != 0:
    #     rotated_asteroids.rotate(1)
    # print( rotated_asteroids )


    destroyed = 1
    while destroyed < MAX_DESTROY:
        seen_asteroids = list( detect_asteroids(my_ast, asteroid_relatives) )
        seen_asteroids.sort( key = sort_angle)

        for ast in seen_asteroids:
            asteroid_relatives.remove(ast)
        # seen_asteroids.sort( key = lambda a: atan2(a[1], a[0]) )

        # Rotamos hasta comenzar por el correcto
        rotated_asteroids = deque(seen_asteroids)
        # while rotated_asteroids[0][0] != 0:
        #     rotated_asteroids.rotate(1)

        # print(rotated_asteroids)
        # print(rotated_asteroids[0])
        while rotated_asteroids:
            last_destroyed = rotated_asteroids.popleft()
            # print(f'{destroyed}: {(last_destroyed[0]+my_ast[0], last_destroyed[1]+my_ast[1])}' )
            if destroyed == MAX_DESTROY:
                break
            destroyed += 1

    result_asteroid = (last_destroyed[0]+my_ast[0], last_destroyed[1]+my_ast[1])
    # print((last_destroyed[0]+my_ast[0], last_destroyed[1]+my_ast[1]))
    return result_asteroid[0]*100 + result_asteroid[1], result_asteroid


def test():
    # Test number:   1   2   3   4    5
    tests_results = [8, 33, 35, 41, 210]

    print('Part 1:')
    for test_i, test_result in enumerate(tests_results, 1):
        input = Input(DAY, 2019, test=test_i)
        result, asteroid = part1(input)
        assert result == test_result
        print(f'Test {test_i} CORRECT [asteroid {asteroid}].')
    

def m(a, b):
    ''' Return the slope of the line of sight between asteroids. 
        With some tricks to take into account the direction of sight.'''
    m_x = (b[0]-a[0])
    m_y = (b[1]-a[1])
    m_gcd = max(gcd(m_x, m_y), 1)
    # if m_x > 0:
    #     return m_y / m_x
    # elif m_x < 0:
    #     return BIG + (m_y / m_x)
    # elif m_y < 0:
    #     return BIG + 99999
    # else:
    #     return BIG

    return (m_x/m_gcd, m_y/m_gcd)


def asteroid_positions(input):
    asteroid_coordinates = []

    for r_i, row in enumerate(input):
        for c_i, spot in enumerate(row):
            if spot == '#':
                asteroid_coordinates.append((c_i, r_i))

    return asteroid_coordinates


def main():
    input = Input(DAY, 2019, test=False)
    detected_1, asteroid_1 = part1(input)
    print('Part 1: ')
    print(f'From asteroid {asteroid_1}, {detected_1} detected.')
    print( )

    # Part 2
    result, final_asteroid = part2(input, asteroid_1)
    print('Part 2: ')
    print(f'Last asteroid destroyed: {final_asteroid}. Result: {result}')
    print()


if __name__ == "__main__":
    main()