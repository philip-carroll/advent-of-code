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
    res = []

    for line in data:
        line = [int(v) for v in line.split(' ')]
        diffs = [line]
        i = 0
        while not all(v == 0 for v in diffs[i]):
            diffs.append([diffs[i][j + 1] - diffs[i][j] for j in range(len(diffs[i]) - 1)])
            i += 1
        # print(diffs)

        nxt = 0
        diffs.reverse()
        for diff in diffs:
            diff.append(diff[-1] + nxt)
            nxt = diff[-1]
            # print(diff)

        res.append(nxt)

    return sum(res)


def two(data):
    res = []

    for line in data:
        line = [int(v) for v in line.split(' ')]
        diffs = [line]
        i = 0
        while not all(v == 0 for v in diffs[i]):
            diffs.append([diffs[i][j + 1] - diffs[i][j] for j in range(len(diffs[i]) - 1)])
            i += 1
        print(diffs)

        nxt = 0
        diffs.reverse()
        for diff in diffs:
            diff.reverse()
            diff.append(diff[-1] - nxt)
            nxt = diff[-1]
            diff.reverse()
            print(diff)

        res.append(nxt)

    return sum(res)


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
