'''
https://adventofcode.com/2021/day/17
'''
DAY = 17


from utils import *
from math import sqrt


def parser(test=False):
    return Input(DAY, 2021, test=test, line_parser=integers)[0]


def parts(input):
    xa, xb, ya, yb = input

    # Velocity ranges
    vx_max = xb
    vx_min = int(sqrt(2*xa)) # Minimum speed that makes x reach xa
    vy_min = ya
    total_max = -float('inf')

    counter = 0
    for vx0 in range(vx_min, vx_max+1):
        for vy0 in range(vy_min, vx_max+1):
            x = 0
            y = 0
            vx = vx0
            vy = vy0
            max_y = -float('inf')
            for _ in range(1000):
                # Update positions
                x += vx
                y += vy

                # Update velocities
                if vx > 0: vx -=1
                elif vx < 0: vx +=1
                vy -= 1

                # Update max_y
                if y > max_y: max_y = y

                # Check area
                if  (xa <= x <= xb) and (ya <= y <= yb):
                    counter += 1
                    # Update overall maximum
                    if max_y > total_max: total_max = max_y
                    break

                # If probe below yb or to the right of xb discard
                if (y < ya) or (x > xb):
                    break

    return total_max, counter


def main():
    input = parser()
    print('RESULTS')

    result_1, result_2 = parts(input)

    print(f'Part 1: {result_1}')
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, lambda i: parts(i)[0], [45], lambda i: parts(i)[1], [112])
    main()