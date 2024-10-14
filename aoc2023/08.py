import math


def get_data(sample=False):
    file = __file__
    if sample:
        file = file.replace('.py', '.sample')
    else:
        file = file.replace('.py', '.txt')

    data = []

    with open(file) as f:
        for line in f.readlines():
            data.append(line.rstrip())

    return data


def one(data):
    loc = 'AAA'
    dest = 'ZZZ'
    steps = 0
    instructions = list(data[0])
    map = {}

    for line in data:
        if '=' in line:
            src = line.split(' = ')[0]
            left, right = line.split(' = ')[1].replace('(', '').replace(')', '').split(', ')
            map[src] = (left, right)

    while loc != dest:
        dir = instructions[steps % len(instructions)]
        if dir == 'L':
            loc = map[loc][0]
        else:
            loc = map[loc][1]
        steps += 1

    return steps


def two(data):
    steps = []
    instructions = list(data[0])
    map = {}

    for line in data:
        if '=' in line:
            src = line.split(' = ')[0]
            left, right = line.split(' = ')[1].replace('(', '').replace(')', '').split(', ')
            map[src] = (left, right)

    loc = [k for k in map.keys() if k[-1] == 'A']

    for l in loc:
        s = 0
        while not l[-1] == 'Z':
            dir = instructions[s % len(instructions)]
            if dir == 'L':
                l = map[l][0]
            else:
                l = map[l][1]
            s += 1
        steps.append(s)
        print('%s: %s' % (l, s))

    lcm = 1
    for s in steps:
        lcm = math.lcm(lcm, s)

    return lcm


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
