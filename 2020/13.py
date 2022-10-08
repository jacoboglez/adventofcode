'''
https://adventofcode.com/2020/day/13
'''
DAY = 13

from utils import *


def parser(test=False):
    earliest, buses = Input(DAY, 2020, test=test)
    return (int(earliest), ['' if b=='x' else int(b) for b in buses.split(',')])


def part1(input):
    my_time, buses = input

    earliest_bus = float('inf')
    min_wait = float('inf')
    for bus in buses:
        if not bus:
            continue

        wait_time = bus - (my_time % bus)
        if wait_time < min_wait:
            min_wait = wait_time
            earliest_bus = bus

    # print(f'{earliest_bus=}')
    # print(f'{wait_time=}')
    return earliest_bus * min_wait

    
def part2(input):
    '''Find the time that takes from the first n buses matching to the next time they match,
    use this time as a sort of lcd to iterate over time and match the next bus on the list until done. '''
    _, buses = input
    nonzero_buses = [(i, bus) for i, bus in enumerate(buses) if bus]

    t_bus0 = 0
    increment = buses[0] # Each buses[0] steps, bus 0 appears
    cycle_found = False
    max_bus_found = 1 # We have the cycle time for the first bus
    while max_bus_found < len(nonzero_buses):
        # Find the cycle time for the first max_bus_found buses
        delay, bus = nonzero_buses[max_bus_found]
        # From the base time (when bus 0 arrives) add the position of current bus
        t = t_bus0 + delay 

        if not t % bus: # The bus matches the slot
            if max_bus_found == len(nonzero_buses)-1:
                    # The last bus was reached
                    return t_bus0

            if cycle_found: # It is the second time it matches
                # The cycle lenght (from the previous match until now)
                increment = t_bus0 - t0 
                max_bus_found += 1

            # Restart the next cycle variables
            t0 = t_bus0 
            cycle_found = not cycle_found

        # Move forward in time a cycle
        t_bus0 += increment          


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [295], part2, [1068781, 3417, 754018, 779210, 1261476, 1202161486])
    main()