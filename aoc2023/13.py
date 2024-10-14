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


def original_lines(data):
    lines = {}
    patterns = []
    pattern = []

    for line in data:
        if line == '':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(list(line))
    patterns.append(pattern)

    p = 0
    for pattern in patterns:
        p += 1
        done = False
        for i in range(len(pattern) - 1):
            if not done and pattern[i] == pattern[i + 1]:  # row match
                print('%s Row: %s %s' % (p, i, i + 1))
                j = i - 1
                k = i + 2
                while not done and j >= 0 and k < len(pattern):
                    if not [x for x in pattern[j]] == [x for x in pattern[k]]:
                        print('%s Missed: %s %s' % (p, j, k))
                        break
                    else:
                        j -= 1
                        k += 1
                else:
                    lines[p] = ('row', i)
                    done = True
                    print('%s Final row!' % p)

        for i in range(len(pattern[0]) - 1):
            if not done and all(pat[i] == pat[i + 1] for pat in pattern):  # column match
                print('%s Column: %s %s' % (p, i, i + 1))
                j = i - 1
                k = i + 2
                while not done and j >= 0 and k < len(pattern[0]):
                    if not all(pat[j] == pat[k] for pat in pattern):
                        print('%s Missed: %s %s' % (p, j, k))
                        break
                    else:
                        j -= 1
                        k += 1
                else:
                    lines[p] = ('col', i)
                    done = True
                    print('%s Final column!' % p)

    return lines


def one(data):
    lines = original_lines(data)
    total = 0

    for k, v in lines.items():
        if v[0] == 'row':
            total += (v[1] + 1) * 100
        else:
            total += (v[1] + 1)

    return total


def two(data):
    lines = original_lines(data)
    total = 0
    patterns = []
    pattern = []

    for line in data:
        if line == '':
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(list(line))
    patterns.append(pattern)

    p = 0
    for pattern in patterns:
        p += 1
        done = False

        for i in range(len(pattern) - 1):
            used = False
            if not done and not (lines[p][0] == 'row' and lines[p][1] == i):
                if pattern[i] == pattern[i + 1] or sum(
                        0 if x0 == x1 else 1 for x0, x1 in zip(pattern[i], pattern[i + 1])) == 1:  # row nearly match
                    print('%s Row: %s %s' % (p, i, i + 1))
                    j = i - 1
                    k = i + 2
                    if sum(0 if x0 == x1 else 1 for x0, x1 in zip(pattern[i], pattern[i + 1])) == 1:
                        used = True
                        print('%s Used: %s %s' % (p, i, i + 1))
                    while not done and j >= 0 and k < len(pattern):
                        if [x for x in pattern[j]] != [x for x in pattern[k]]:
                            if not used and sum(
                                    0 if x0 == x1 else 1 for x0, x1 in zip(pattern[j], pattern[k])) == 1:
                                used = True
                                print('%s Used: %s %s' % (p, j, k))
                                j -= 1
                                k += 1
                            else:
                                print('%s Missed: %s %s' % (p, j, k))
                                break
                        else:
                            j -= 1
                            k += 1
                    else:
                        total += (i + 1) * 100
                        done = True
                        print('%s Final row!' % p)

        for i in range(len(pattern[0]) - 1):
            used = False
            if not done and not (lines[p][0] == 'col' and lines[p][1] == i):
                if all(pat[i] == pat[i + 1] for pat in pattern) or sum(
                        0 if pat[i] == pat[i + 1] else 1 for pat in pattern) == 1:  # column nearly match
                    print('%s Column: %s %s' % (p, i, i + 1))
                    j = i - 1
                    k = i + 2
                    if sum(0 if pat[i] == pat[i + 1] else 1 for pat in pattern) == 1:
                        used = True
                        print('%s Used: %s %s' % (p, i, i + 1))
                    while not done and j >= 0 and k < len(pattern[0]):
                        if not all(pat[j] == pat[k] for pat in pattern):
                            if not used and sum(0 if pat[j] == pat[k] else 1 for pat in pattern) == 1:
                                used = True
                                print('%s Used: %s %s' % (p, j, k))
                                j -= 1
                                k += 1
                            else:
                                print('%s Missed: %s %s' % (p, j, k))
                                break
                        else:
                            j -= 1
                            k += 1
                    else:
                        total += i + 1
                        done = True
                        print('%s Final column!' % p)

    return total


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))  # 34864 too high
