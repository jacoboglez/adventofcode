'''
https://adventofcode.com/2017/day/20
'''
DAY = 20
INF = float('inf')
N = 500 # Number of iterations
# Ideally the program should stop with some criteria, 
# not after max. number of iterations

from operator import add
from os import close
from utils import *
from collections import namedtuple, defaultdict


Particle = namedtuple('Particle', ['i', 'p', 'v', 'a'])


def parser(test=False):
    input = Input(DAY, 2017, test=test, line_parser=integers)
    particles = []
    for i, p in enumerate(input):
        particles.append( Particle(i, tuple(p[:3]), tuple(p[3:6]), tuple(p[6:])) )
        
    return particles


def manhattan(a):
    return sum(abs(c) for c in a)


def part1(particles):
    for _ in range(N):
        new_particles = []
        closest = Particle(-1, (INF, INF, INF), (INF, INF, INF), (INF, INF, INF))
        for p in particles:
            new_v = addc(p.v, p.a)
            new_p = Particle(p.i, addc(p.p, new_v), new_v, p.a)
            new_particles.append(new_p)
            if manhattan(new_p.p) < manhattan(closest.p):
                closest = new_p
        particles = new_particles
        
    return closest.i
        

def part2(particles):
    for _ in range(N):
        collisions = defaultdict(list)
        for p in particles:
            new_v = addc(p.v, p.a)
            new_p = Particle(p.i, addc(p.p, new_v), new_v, p.a)
            collisions[new_p.p].append(new_p)

        # Remove collisions
        particles = [ps[0] for ps in collisions.values() if (len(ps) == 1)]
        
        
    return len(particles)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [1], part2, [None, 1])
    main()