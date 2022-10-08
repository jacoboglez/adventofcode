
def part1(inputlst):
    memory = 0
    for inputstr in inputlst:
        # print(inputstr[:-1], ' -> ', eval(inputstr))
        memory += len(inputstr[:-1])
        memory -= len(eval(inputstr))
    
    return memory


def part2(inputlst):    
    return sum( s.count('"')+s.count("\\")+2  for s in inputlst )


if __name__ == "__main__":
    print(f"Part 1: {part1( open('2015/inputs/2015_08.txt') )}")
    print(f"Part 2: {part2( open('2015/inputs/2015_08.txt') )}")
