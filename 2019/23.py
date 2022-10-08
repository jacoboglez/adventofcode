'''
https://adventofcode.com/2019/day/23
'''
DAY = 23

from utils import *
from icc import intCodeComputer
from collections import deque


NETWORK_SIZE = 50


def part1(program):
    network = [ intCodeComputer(program, id=i, verbose=False) for i in range(NETWORK_SIZE) ]
    queues = [ deque([]) for _ in range(NETWORK_SIZE) ]

    # Initialize network
    for i, computer in enumerate(network):
        computer.inputArray.append(i)
        computer.compute()

    # Make one turn in the network
    while True:
        # print('(-----------------------------------------------------------)')
        for i, (computer, Q) in enumerate( zip(network, queues) ):
            if not Q:
                computer.inputArray.append(-1)
            else:
                computer.inputArray.append(Q.popleft())
                computer.inputArray.append(Q.popleft())

            # print(f'in[{i}]: {computer.inputArray}')
            computer.compute()
            # print(f'out[{i}]: {computer.outputArray}')

            # Process output array
            while computer.outputArray:
                addr = computer.outputArray.pop(0)
                X = computer.outputArray.pop(0)
                Y = computer.outputArray.pop(0)

                if addr == 255:
                    return Y

                queues[addr].extend([X, Y])


def part2(program):
    network = [ intCodeComputer(program, id=i, verbose=False) for i in range(NETWORK_SIZE) ]
    queues = [ deque([]) for _ in range(NETWORK_SIZE) ]
    NAT = []
    previous_Y = None

    # Initialize network
    for i, computer in enumerate(network):
        computer.inputArray.append(i)
        computer.compute()

    # Make one turn in the network
    while True:
        idle = True
        # print('(-----------------------------------------------------------)')
        for i, (computer, Q) in enumerate( zip(network, queues) ):
            if not Q:
                computer.inputArray.append(-1)
            else:
                idle = False
                computer.inputArray.append(Q.popleft())
                computer.inputArray.append(Q.popleft())

            # print(f'in[{i}]: {computer.inputArray}')
            computer.compute()
            # print(f'out[{i}]: {computer.outputArray}')

            # Process output array
            while computer.outputArray:
                idle = False
                addr = computer.outputArray.pop(0)
                X = computer.outputArray.pop(0)
                Y = computer.outputArray.pop(0)

                if addr == 255:
                    NAT = [X, Y]
                else:
                    queues[addr].extend([X, Y])
        
        # End of the cycle
        # NAT checks idle: empty queues & not sending
        if idle:
            queues[0].extend([X, Y])

            if Y == previous_Y:
                return Y
            else:
                previous_Y = Y
    


def main():
    input = Input(DAY, 2019, line_parser = integers)
    program = list(input[0])
    
    result_1 = part1(program)
    print(f'Part 1: {result_1}')

    print('')
    result_1 = part1(program)
    result_2 = part2(program)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    main()