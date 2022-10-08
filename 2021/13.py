'''
https://adventofcode.com/2021/day/13
'''
DAY = 13


from utils import *


def parser(test=False):
    input = Input(DAY, 2021, test=test)
    dots = set()
    # Dots
    for i, line in enumerate(input):
        if not line: # Empty line: separator
            break
        dots.add(tuple(int(i) for i in line.split(',')))

    # Folds
    folds = []
    for line in input[i+1:]:
        dir, val = line.split('=')
        folds.append((0 if dir[-1]=='x' else 1, int(val)))

    return dots, folds
    
       
def fold_paper(dots, folds, part=2):
    ''' Folding works like this:    
        If the fold is at y=n (same for x=n), coordinates change like this:
        y=n+1 -> y=n-1
        y=n+2 -> y=n-2
        ...
        So the change in coordinate is:
        final_coor = initial_coor - 2·(initial_coor - n). '''

    for x, val in folds:
        if x == 0: # Fold x
            delta = lambda x: (-2*(x[0]-val), 0)
        else: # Fold y
            delta = lambda x: (0, -2*(x[1]-val))

        new_dots = set()
        for dot in dots:
            if dot[x] > val:
                new_dot = addc(dot, delta(dot))
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)

        dots = new_dots.copy()

        if part == 1:
            return dots

    return dots


def dots2str(dots):
    # Find paper size
    x_max, y_max = 0, 0
    for x, y in dots:
        if x > x_max: x_max = x
        if y > y_max: y_max = y
    
    paper = ''
    for y in range(y_max+1):
        line = ''
        for x in range(x_max+1):
            line += '█' if (x,y) in dots else ' '
        paper += '\n'
        paper += line
    
    return paper


def part1(input):
    folded = fold_paper(*input, part=1)
    return len(folded)


def part2(input):
    folded = fold_paper(*input)
    return dots2str(folded)
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [17], part2, [])
    main()