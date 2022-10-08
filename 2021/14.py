'''
https://adventofcode.com/2021/day/14
'''
DAY = 14


from utils import *
from collections import defaultdict, Counter
from functools import lru_cache


def parser(test=False):
    input = Input(DAY, 2021, test=test)
    polymer_template = input[0]

    insertion_rules = defaultdict(str)
    for line in input[2:]:
        pair, insertion = line.split(' -> ')
        insertion_rules[pair] = insertion
    
    return polymer_template, insertion_rules


def part1(input):
    polymer_template, insertion_rules = input

    polymer = polymer_template
    for _ in range(10):
        new_polymer = []
        for a,b in zip(polymer[:-1], polymer[1:]):
            new_polymer.append(a)
            new_polymer.append(insertion_rules[a+b])

        new_polymer.append(b)
        polymer = new_polymer

    element_counts = Counter(new_polymer)

    return max(element_counts.values()) - min(element_counts.values())


def part2(input, n=40):
    polymer_template, insertion_rules = input

    @lru_cache(maxsize=None)
    def rec(a,b, nn):
        if (a+b in insertion_rules) and nn:
            a_down = rec(a, insertion_rules[a+b], nn-1)
            b_down = rec(insertion_rules[a+b], b, nn-1)
            return a_down + b_down
        else:
            return Counter([a])

    total_counter = Counter()
    for a,b in zip(polymer_template[:-1], polymer_template[1:]):
        total_counter += rec(a,b,n)

    # Add the last element
    total_counter += Counter(polymer_template[-1])

    return max(total_counter.values()) - min(total_counter.values())
    

def part2_count(input, n=40):
    polymer_template, insertion_rules = input

    couples = defaultdict(int)
    elements = defaultdict(int)

    # Initalization
    for a,b in zip(polymer_template[:-1], polymer_template[1:]):
        elements[a] += 1

        if a+b in insertion_rules:
            couples[a+b] += 1
    elements[b] += 1

    for _ in range(n):
        new_couples = defaultdict(int)
        for c, v in couples.items():
            inser = insertion_rules[c]
            elements[inser] += v
            
            if c[0]+inser in insertion_rules:
                new_couples[c[0]+inser] += v
            if inser+c[1] in insertion_rules:
                new_couples[inser+c[1]] += v
    
        couples = new_couples.copy()

    return max(elements.values()) - min(elements.values())
            
            
def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [1588], part2, [2188189693529])
    main()