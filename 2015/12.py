import re
import json


TESTS1 = [
('[1,2,3,-5,5]', 6),
('{"a":2,"b":4}', 6),
('[[[3]]] ', 3),
('{"a":{"b":4},"c":-1}', 3),
('{"a":[-1,1]} ', 0),
('[-1,{"a":1}]', 0),
('[] ', 0),
('{}', 0),
]

TESTS2 = [
([1,2,3,-5,5], 6),
([1,{"c":"red","b":2},3], 4),
({"d":"red","e":[1,2,3,4],"f":5}, 0),
([1,"red",5], 6),
]


def part1(inputstr):
    g = re.findall(r"-?[0-9]+", inputstr)
    return sum( int(n) for n in g )


def part2(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)

    return crawler(data)


def crawler(data):
    acum = 0
    if type(data) is dict:
        if "red" in data.values():
                return 0
        data = data.values()

    for el in data:
        if type(el) is int:
            acum += el
        elif type(el) is list:
            acum += crawler(el)
        elif type(el) is dict:
            acum += crawler(el)
    
    return acum


def test():
    for inp, res in TESTS1:
        if part1(inp) != res:
            raise AssertionError

    for inp, res in TESTS2:
        if crawler(inp) != res:
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test() 
    inputlst = open('2015/inputs/2015_12.txt', 'r').read().strip()
    print(f'Part 1: {part1(inputlst)}')
    print(f'Part 2: {part2("2015/inputs/2015_12.txt")}')
