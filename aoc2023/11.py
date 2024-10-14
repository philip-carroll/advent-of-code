import itertools


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


def expand(data):
    data2 = []
    for line in data:
        data2.append(line.copy())
    inserts = 0
    for i in range(len(data)):
        if all([x == '.' for x in data[i]]):
            data2.insert(i + inserts + 1, ['|' for _ in data[i]])
            inserts += 1

    data3 = []
    for line in data2:
        data3.append(line.copy())
    inserts = 0
    for i in range(len(data2[0])):
        if all([y[i] == '.' or y[i] == '|' for y in data2]):
            for j in range(len(data2)):
                data3[j].insert(i + inserts + 1, '|')
            inserts += 1

    return data3


def one(data):
    for i in range(len(data)):
        data[i] = list(data[i])

    data = expand(data)

    nums = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '.':
                nums.append((i, j))

    # import networkx as nx
    # G = nx.grid_2d_graph(len(data), len(data[0]))
    combinations = itertools.combinations(nums, 2)
    total = 0
    for c in combinations:
        source = c[0]
        target = c[1]
        # total += nx.shortest_path_length(G, source, target)
        diff = abs(target[0] - source[0]) + abs(target[1] - source[1])
        total += diff
        print('%s: %s' % (c, diff))

    return total


def two(data):
    expansion = 1000000

    for i in range(len(data)):
        data[i] = list(data[i])

    data = expand(data)

    nums = []
    i2 = 0
    for i in range(len(data)):
        j2 = 0
        row_counted = False
        for j in range(len(data[i])):
            if data[i][j] == '#':
                nums.append((i2, j2))
            elif data[i][j] == '|':
                if all([x == '|' for x in data[i]]) and not row_counted:  # row expanded
                    i2 += expansion - 2
                    row_counted = True
                elif all([y[j] == '|' for y in data]):  # column expanded
                    j2 += expansion - 2

            j2 += 1
        i2 += 1

    combinations = itertools.combinations(nums, 2)
    total = 0
    for c in combinations:
        source = c[0]
        target = c[1]
        diff = abs(target[0] - source[0]) + abs(target[1] - source[1])
        total += diff
        print('%s: %s' % (c, diff))

    return total


if __name__ == '__main__':
    data = get_data(False)

    print(one(data))
    # print(two(data))
