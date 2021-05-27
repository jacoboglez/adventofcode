from string import ascii_lowercase

TESTS1 = [
('abcdfezx', 'abcdffaa'),
('abcdefgh', 'abcdffaa'),
('ghijklmn', 'ghjaabcc')
]


FORBIDDEN = "i o l".split()


def incrementLetter(s):
    l = list(s)
    for i, c in reversed(list(enumerate(l))):
        next_i = ascii_lowercase.index(c) + 1
        if next_i > len(ascii_lowercase)-1:
            next_i = 0
            l[i] = ascii_lowercase[next_i]
        else:
            l[i] = ascii_lowercase[next_i]
            break

    return "".join(l)


def requirement1(s):
    for i in range(len(ascii_lowercase[:-2])):
        consecutive = ascii_lowercase[i:i+3]
        if consecutive in s:
            return True

    return False


def requirement2(s):
    for f in FORBIDDEN:
        if f in s:
            return False

    return True


def requirement3(s):
    count = 0
    for l in ascii_lowercase:
        if s.count(l*2):
            count +=1
        if count >= 2:
            return True
    
    return False


def part1(inputlst):
    password = inputlst

    while not (requirement1(password) and 
               requirement2(password) and 
               requirement3(password) ):
        password = incrementLetter(password)

    return password


def test():
    # Increment letter
    assert incrementLetter('xx') == 'xy'
    assert incrementLetter('xy') == 'xz'
    assert incrementLetter('xz') == 'ya'
    assert incrementLetter('ya') == 'yb'

    # Requirement 1
    assert requirement1('hijklmmn') == True
    assert requirement1('abbceffg') == False

    # Requirement 2
    assert requirement2('hijklmmn') == False
    assert requirement2('abbcegjk') == True
    assert requirement2('abboegjk') == False
    assert requirement2('abblegjk') == False

    # Requirement 3
    assert requirement3('hijklmmn') == False
    assert requirement3('abbceffg') == True
    assert requirement3('abbcegjk') == False

    for inp, res in TESTS1:
        if part1(inp) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    # test() # Too slow
    inputlst = open('2015/inputs/11.txt', 'r').read().strip()
    pass1 = part1(inputlst)
    print(f'Part 1: {pass1}')
    print(f'Part 2: {part1(incrementLetter(pass1))}')
