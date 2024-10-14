from pprint import pprint
from collections import OrderedDict


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
    res = OrderedDict()

    for line in data:
        if line.startswith('seeds:'):
            section = 0
            res[section] = [int(s) for s in line.split(' ') if s.isnumeric()]
        elif line.startswith('seed-to-soil map:'):
            section = 1
            res[section] = []
        elif line.startswith('soil-to-fertilizer map:'):
            section = 2
            res[section] = []
        elif line.startswith('fertilizer-to-water map:'):
            section = 3
            res[section] = []
        elif line.startswith('water-to-light map:'):
            section = 4
            res[section] = []
        elif line.startswith('light-to-temperature map:'):
            section = 5
            res[section] = []
        elif line.startswith('temperature-to-humidity map:'):
            section = 6
            res[section] = []
        elif line.startswith('humidity-to-location map:'):
            section = 7
            res[section] = []
        elif line == '':
            pass
        else:
            res[section].append(line)
    print(res)

    res2 = OrderedDict()
    for k, v in res.items():
        if k == 0:
            res2[k] = v
        else:
            res2[k] = []
            for vs in v:
                res2[k].append([int(i) for i in vs.split(' ')])
    print(res2)

    res3 = OrderedDict()
    for k, v in res2.items():
        if k == 0:
            res3[k] = v
        else:
            print(k)
            if k == 1:
                res3[k] = {v1: v1 for v1 in res3[k - 1]}
            else:
                res3[k] = {v1: v1 for v1 in res3[k - 1].values()}

            for m in v:
                s = m[1]  # source
                d = m[0]  # destination
                l = m[2]  # length

                if k == 1:
                    last_vals = res3[k - 1]
                else:
                    last_vals = res3[k - 1].values()
                for des in last_vals:
                    if s <= des < (s + l):
                        res3[k][des] = d + (des - s)
    print(res3)

    return min([v for v in res3[7].values()])


def two(data):
    res = OrderedDict()

    for line in data:
        if line.startswith('seeds:'):
            section = 0
            res[section] = []
            seeds = [int(s) for s in line.split(' ') if s.isnumeric()]
            for i in range(len(seeds)):
                if i % 2 == 0:  # even
                    # if i % 2 == 0 and i < 2:  # even
                    res[section].append(range(seeds[i], seeds[i] + seeds[i + 1]))
        elif line.startswith('seed-to-soil map:'):
            section = 1
            res[section] = []
        elif line.startswith('soil-to-fertilizer map:'):
            section = 2
            res[section] = []
        elif line.startswith('fertilizer-to-water map:'):
            section = 3
            res[section] = []
        elif line.startswith('water-to-light map:'):
            section = 4
            res[section] = []
        elif line.startswith('light-to-temperature map:'):
            section = 5
            res[section] = []
        elif line.startswith('temperature-to-humidity map:'):
            section = 6
            res[section] = []
        elif line.startswith('humidity-to-location map:'):
            section = 7
            res[section] = []
        elif line == '':
            pass
        else:
            res[section].append(line)
    print(res)

    res2 = OrderedDict()
    for k, v in res.items():
        if k == 0:
            res2[k] = v
        else:
            res2[k] = []
            for vs in v:
                res2[k].append([int(i) for i in vs.split(' ')])
    print(res2)

    res3 = OrderedDict()
    for k, v in res2.items():
        done = []
        if k == 0:
            res3[k] = v
        else:
            if k == 1:
                res3[k] = {v1: v1 for v1 in res3[k - 1]}
                last_vals = res3[k - 1]
            else:
                res3[k] = {}
                last_vals = res3[k - 1].values()

            for des in last_vals:
                for m in v:
                    s = m[1]  # source
                    d = m[0]  # destination
                    l = m[2]  # length

                    r = range(m[1], m[1] + l)

                    intersection = range(max(des.start, r.start), min(des.stop, r.stop))
                    if intersection.start < intersection.stop:
                        res3[k][intersection] = range(intersection.start + (d - s), intersection.stop + (d - s))

                        if des != intersection:
                            if des.start < intersection.start:  # before intersection
                                difference = range(des.start, intersection.start)
                            if des.stop > intersection.stop:  # after intersection
                                difference = range(intersection.stop, des.stop)
                            if difference not in res3[k]:
                                res3[k][difference] = difference
                        done.append(des)

                if des not in done:
                    res3[k][des] = des

    pprint(res3)

    return min([v.start for v in res3[7].values()])


if __name__ == '__main__':
    data = get_data(False)

    # pprint(one(data))  # 12208442 too low
    print(two(data))
