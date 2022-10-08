'''
https://adventofcode.com/2020/day/4
'''
DAY = 4

from utils import *
import re


FIELDS = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])


def parser(test=False):
    raw_in = Input(DAY, 2020, test=test)

    all_passports = []
    passport = {}
    for line in raw_in:
        if not line: # Blank line: passport finished, start a new one
            all_passports.append(passport)
            passport = {}
            continue
        
        fields = line.split(' ')
        passport.update( {f.split(':')[0]: f.split(':')[1] for f in fields} )

    all_passports.append(passport) # Add the last one
    return all_passports


def part1(input):
    valid = 0

    for passport in input:
        passport_fields = set(passport.keys())
        passport_fields.add('cid')

        if passport_fields == FIELDS:
            valid += 1

    return valid


def validate(passport):
    ''' Returns 1 if valid and 0 if invalid.
    RULES:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.'''

    # byr
    byr = int(passport['byr'])
    if not (1920 <= byr <= 2002):
        return 0

    # iyr
    iyr = int(passport['iyr'])
    if not (2010 <= iyr <= 2020):
        return 0

    # eyr
    eyr = int(passport['eyr'])
    if not (2020 <= eyr <= 2030):
        return 0

    # hgt
    hgt =passport['hgt']
    match = re.search(r"(\d+)(in|cm)", hgt)
    if not match:
        return 0
    elif match.group(2) == "cm":
        if not (150 <= int(match.group(1)) <= 193):
            return 0
    elif match.group(2) == "in":
        if not (59 <= int(match.group(1)) <= 76):
            return 0

    # hcl
    hcl = passport['hcl']
    match = re.match(r"#[0-9 a-f]{6}", hcl)
    if not bool(match):
        return 0

    # ecl
    ecl = passport['ecl']
    if not (ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
        return 0

   # pid
    pid = passport['pid']
    match = re.match(r"^[0-9]{9}$", pid)
    if not bool(match):
        return 0

    return 1


def part2(input):
    valid = 0

    for passport in input:
        passport_fields = set(passport.keys())
        passport_fields.add('cid')

        if passport_fields == FIELDS:
            valid += validate(passport)

    return valid


def main():
    input = parser()
    print('RESULTS')

    result_1 = part1(input)
    print(f'Part 1: {result_1}')

    result_2 = part2(input)
    print(f'Part 2: {result_2}')


if __name__ == "__main__":
    test(DAY, parser, part1, [2], part2, [2, 4])
    main()