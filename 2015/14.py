import re 

TESTS1 = [
('''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
'''.strip().split('\n'), 1120),
]

TESTS2 = [
('''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
'''.strip().split('\n'), 689),
]


def distance(vel, vel_t, rest_t, total_time):
    entero = vel*vel_t * ( total_time // (vel_t+rest_t) )
    resto = vel * min(vel_t, total_time % (vel_t+rest_t) )
    return entero + resto


def part1(inputlst, total_time=1000):
    max_dist = 0
    for inputstr in inputlst:
        [vel, vel_t, rest_t] = re.findall(r"-?[0-9]+", inputstr)
        dist = distance(int(vel), int(vel_t), int(rest_t), total_time)
        if dist > max_dist: max_dist = dist

    return max_dist


def part2(inputlst, total_time=1000):
    reindeers = []
    for inputstr in inputlst:
        [vel, vel_t, rest_t] = re.findall(r"-?[0-9]+", inputstr)
        reindeers.append( (int(vel), int(vel_t), int(rest_t)) )

    points = [0 for r in reindeers]
    distances = [0 for r in reindeers]
    for t in range(1, total_time+1):
        for i, r in enumerate(reindeers):
            distances[i] = distance(*r, t)

        for i in range(len(reindeers)):
            if distances[i] == max(distances):
                points[i] += 1

    return max(points)


def test():
    for inp, res in TESTS1:
        if part1(inp) != res:
            raise AssertionError

    for inp, res in TESTS2:
        if part2(inp) != res:
            print(part2(inp))
            raise AssertionError

    print('Tests SUCCESSFUL')


if __name__ == "__main__":
    test()
    inputlst = open('2015/inputs/2015_14.txt', 'r').read().strip().split('\n')
    print(f'Part 1: {part1(inputlst, total_time=2503)}')
    print(f'Part 1: {part2(inputlst, total_time=2503)}')
