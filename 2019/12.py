'''
https://adventofcode.com/2019/day/12
'''

from utils import *
import numpy as np
import math

def energy(moons, velocities):
    potential_energy = 0
    kinetic_energy = 0
    total_energy = 0

    for moon, velocity in zip(moons, velocities):
        potential_energy = sum(abs(moon))
        kinetic_energy = sum(abs(velocity))
        total_energy += potential_energy * kinetic_energy

    return total_energy


def part1(input):
    # Update velocity with gravity
    #   To apply gravity consider each pair of moons
    #   Pull moons together by 1 velocity in each axis
    #   Unless they have the same position in that axis

    moons = [np.array(t) for t in input]
    velocities = [np.array([0, 0, 0]) for _ in moons]
    print(f'moons (0): {moons}')
    # print(f'velocities: {velocities}')

    t_end = 1000
    for t in range(t_end):
        for m_i, moon in enumerate(moons):
            for o_i, other in enumerate(moons[m_i+1:], m_i+1):
                v_inc = np.array([0, 0, 0])
                v_inc += (moon < other) 
                v_inc -= (other < moon)

                velocities[m_i] += v_inc
                velocities[o_i] -= v_inc

        print(f'velocities ({t+1}): {velocities}')

        # Update position with velolcity
        for i, velocity in enumerate(velocities):
            moons[i] += velocity

        print(f'moons ({t+1}): {moons}')
        

        # Total energy
        total_energy = energy(moons, velocities)
        print(f'energy ({t+1}): {total_energy}')


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def part2(input):

    partial_peridos = []
    for coor in range(3):
        moons = [np.array(t) for t in input]
        velocities = np.array([np.array([0, 0, 0]) for _ in moons])

        moons_0 = [np.array(t) for t in input]
        velocities_0 = [np.array([0, 0, 0]) for _ in moons]
        
        
    
        t =1
        while True:
            for m_i, moon in enumerate(moons):
                for o_i, other in enumerate(moons[m_i+1:], m_i+1):
                    v_inc = np.array([0, 0, 0])
                    v_inc += (moon < other) 
                    v_inc -= (other < moon)

                    velocities[m_i] += v_inc
                    velocities[o_i] -= v_inc

            # Update position with velolcity
            for i, velocity in enumerate(velocities):
                moons[i] += velocity


            # Check if previous
            for i, (moon, vel) in enumerate(zip(moons, velocities)):
                if not ((moons_0[i][coor] == moon[coor]) and (velocities_0[i][coor] == vel[coor])):
                    break
            else: # didnt break because wrong
                break

            # Update step
            t += 1

        partial_peridos.append(t)
        print(t)

    result = lcm(partial_peridos[0], lcm(partial_peridos[1], partial_peridos[2]))
    print(result)

    return result



def main():
    input = Input(12, 2019, integers, test=1)
    # part1(input)
    part2(input)


if __name__ == "__main__":
    main()