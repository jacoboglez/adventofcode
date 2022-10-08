from collections import defaultdict

infty = 999999999999

ANALYSIS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parseAunts(inputlst):
    aunts = defaultdict(dict)

    for i, sue in enumerate(inputlst):
        s = sue.split()
        # Could not bother to generalize it
        aunts[int(s[1].strip(':'))][s[2].strip(':')] = int(s[3].strip(','))
        aunts[int(s[1].strip(':'))][s[4].strip(':')] = int(s[5].strip(','))
        aunts[int(s[1].strip(':'))][s[6].strip(':')] = int(s[7].strip(','))
 
    return aunts


def part1(my_aunts):
    for aunt, prop in my_aunts.items():
        for p_name, p_value in prop.items():
            if ANALYSIS[p_name] != p_value:
                break
        else: #nobreak
            return aunt


def part2(my_aunts):
    # New corrected analysis
    an = {k: [v] for k,v in ANALYSIS.items()}
    an['cats'] = range(an['cats'][0]+1, infty)
    an['trees'] = range(an['trees'][0]+1, infty)
    an['pomeranians'] = range(0, an['pomeranians'][0])
    an['goldfish'] = range(0, an['goldfish'][0])
    
    for aunt, prop in my_aunts.items():
        for p_name, p_value in prop.items():
            if p_value not in an[p_name]:
                break
        else: #nobreak
            return aunt


if __name__ == "__main__":
    inputlst = open('2015/inputs/2015_16.txt', 'r').read().strip().split('\n')
    myAunts = parseAunts(inputlst)
    print(f'Part 1: {part1(myAunts)}')
    print(f'Part 1: {part2(myAunts)}')
