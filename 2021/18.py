'''
https://adventofcode.com/2021/day/18
'''
DAY = 18


from utils import *
from math import ceil, floor


def parser(test=False):
    return Input(DAY, 2021, test=test)


def rreplace(s, old, new):
    return new.join(s.rsplit(old, 1))


def snail_test():
    # snail_sum
    # assert snail_sum('[1,2]','[[3,4],5]') == '[[1,2],[[3,4],5]]'
    # assert snail_reduce('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
    # assert snail_reduce('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'

    # # snail_explode
    # assert snail_explode('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
    # assert snail_explode('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
    # assert snail_explode('[[6,[5,[4,[3,2]]]],1]') == '[[6,[5,[7,0]]],3]'
    # assert snail_explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    # assert snail_explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]') == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'


    # # snail_split
    # assert snail_split('[10,5]') == '[[5,5],5]'
    # assert snail_split('[0,11]') == '[0,[5,6]]'
    # assert snail_split('[[[[0,7],4],[15,[0,13]]],[1,1]]') == '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
    # assert snail_split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]') == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'

    # # snail_reduce
    assert snail_reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]') == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    # assert snail_reduce('a') == 'b'


def snail_reduce(sn):
    '''To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:
    - If any pair is nested inside four pairs, the leftmost such pair explodes.
    - If any regular number is 10 or greater, the leftmost such regular number splits.'''
    # print(sn)

    depth = 0
    while True:
        # print(f'{sn=}')
        depth = 0
        for i, c in enumerate(sn):
            if c == '[': 
                depth += 1
            elif c == ']': 
                depth -= 1

            if depth == 5:
                # block = sn[i:i+5]
                new_snail = snail_explode(sn, i)
                break

            if (i < len(sn)-1) and sn[i:i+2].isnumeric():
                # Split
                n = sn[i:i+2]
                new_snail = sn.replace(n, f'[{floor(int(n)/2)},{ceil(int(n)/2)}]')
                break
        else: # nobreak
            break
        sn = new_snail
    return new_snail


def snail_explode(sn, i):
    '''To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair 
    (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). 
    Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.'''
    while not ( (sn[i] == '[') and (sn[i+1].isnumeric()) and (sn[i+3].isnumeric() or sn[i+4].isnumeric())):
        i+=1

    # check for double digits
    if sn[i+2].isnumeric():
        aa = int(sn[i+1:i+3])
        if sn[i+5].isnumeric():
            bb = int(sn[i+4:i+6])
            jump = 7
        else:
            bb = int(sn[i+4:i+5])
            jump = 6
    else:
        aa = int(sn[i+1:i+2])
        if sn[i+4].isnumeric():
            bb = int(sn[i+3:i+5])
            jump = 6
        else:
            bb = int(sn[i+3:i+4])
            jump = 5

    # previous number
    for j, a in enumerate(sn[i:0:-1]):
        if a.isnumeric():
            ai = j
            an = int(a)
            break
    else: # nobreak
        ai = -1

    for j, b in enumerate(sn[i+jump:]):
        if b.isnumeric():
            bi = j
            bn = int(b)
            break
    else: # nobreak
        bi = -1

    news = ''
    if ai > 0:
        news += sn[:i-ai] + str(an+aa) + sn[i-ai+1:i]
    else:
        news += sn[:i]

    news += '0'

    if bi > 0:
        news += sn[i+jump:i+jump+bi] + str(bn+bb) + sn[i+jump+1+bi:]
    else:
        news += sn[i+jump:]

    return news



def snail_sum(a,b):
    '''To add two snailfish numbers, form a pair from the left and right parameters of the addition operator. 
    For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].'''
    return '[' + a + ',' + b + ']'


def part1(input):
    prev = input[0]
    for b in input[1:]:
        # print(f'{prev=}')
        # print(f'   {b=}')
        prev = snail_sum(prev, b)
        prev = snail_reduce(prev)
        # print(f'{prev=}')
        # print()
    


def part2(input):
    pass
    

def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    snail_test()
    test(DAY, parser, part1, [1], part2, [])
    # main()