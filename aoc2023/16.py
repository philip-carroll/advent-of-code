import threading


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


def mirror(loc, dir, item):
    if dir == (0, 1):
        if item == '\\':
            dir = (1, 0)
        elif item == '/':
            dir = (-1, 0)

    elif dir == (0, -1):
        if item == '\\':
            dir = (-1, 0)
        elif item == '/':
            dir = (1, 0)

    elif dir == (1, 0):
        if item == '\\':
            dir = (0, 1)
        elif item == '/':
            dir = (0, -1)

    elif dir == (-1, 0):
        if item == '\\':
            dir = (0, -1)
        elif item == '/':
            dir = (0, 1)

    loc = loc[0] + dir[0], loc[1] + dir[1]

    return [loc, dir]


def splitter(loc, dir, item):
    sloc = (loc[0], loc[1])
    sdir = (dir[0], dir[1])

    if dir == (0, 1):
        if item == '|':
            dir = (1, 0)
            sdir = (-1, 0)

    elif dir == (0, -1):
        if item == '|':
            dir = (1, 0)
            sdir = (-1, 0)

    elif dir == (1, 0):
        if item == '-':
            dir = (0, 1)
            sdir = (0, -1)

    elif dir == (-1, 0):
        if item == '-':
            dir = (0, 1)
            sdir = (0, -1)

    loc = loc[0] + dir[0], loc[1] + dir[1]
    sloc = sloc[0] + sdir[0], sloc[1] + sdir[1]

    return [loc, dir], [sloc, sdir]


def get_combos(data):
    combos = []
    dcombos = list([(0, n), (1, 0)] for n in range(len(data[0])))
    lcombos = list([(n, 0), (0, 1)] for n in range(len(data)))
    rcombos = list([(n, len(data[0]) - 1), (0, -1)] for n in range(len(data)))
    ucombos = list([(len(data) - 1, n), (-1, 0)] for n in range(len(data[0])))
    combos.extend(dcombos)
    combos.extend(lcombos)
    combos.extend(rcombos)
    combos.extend(ucombos)

    return combos


def run(start):
    beams = {1: start}
    energized = [start]
    max_beam = 1

    while beams:
        for k, v in beams.copy().items():
            loc = v[0]
            dir = v[1]
            item = data[loc[0]][loc[1]]
            if item == '.':
                new = [(loc[0] + dir[0], loc[1] + dir[1]), dir]
            elif item in ['/', '\\']:
                new = mirror(loc, dir, item)
            elif item in ['-', '|']:
                new, split = splitter(loc, dir, item)
                if new[0] != split[0] and 0 <= split[0][0] < len(data) and 0 <= split[0][1] < len(data[0]):
                    max_beam += 1
                    beams[max_beam] = split
                    if split not in energized:
                        energized.append(split)
                    else:
                        del beams[max_beam]
                        # print('%s: %s' % (max_beam, split))

            if 0 <= new[0][0] < len(data) and 0 <= new[0][1] < len(data[0]):
                beams[k] = new
                if new not in energized:
                    energized.append(new)
                else:
                    del beams[k]
                    # print('%s: %s' % (k, new[0]))
            else:
                del beams[k]
                # print('%s: deleted' % k)

    print('%s: %s' % (start, len(set([e[0] for e in energized]))))


def one(data):
    for i in range(len(data)):
        data[i] = list(data[i])

    run([(0, 3), (1, 0)])


def two(data):
    for i in range(len(data)):
        data[i] = list(data[i])

    combos = get_combos(data)
    for c in combos:
        t = threading.Thread(target=run, args=(c,))
        t.start()


if __name__ == '__main__':
    data = get_data(False)

    # one(data)
    two(data)
