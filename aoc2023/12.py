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


def one(data):
    res = 0
    possible = ['.', '#']

    for line in data:
        springs, size = line.split(' ')
        size = [int(s) for s in size.split(',')]
        missing = [i for i, c in enumerate(springs) if c == '?']

        # get all permutations of possible values for missing elements
        permutations = list(itertools.product(possible, repeat=len(missing)))
        for p in permutations:
            l = springs
            # substitute in each permutation
            for m in range(len(missing)):
                l = l[:missing[m]] + p[m] + l[missing[m] + 1:]

            # check if this pattern works
            if [len(c) for c in l.split('.') if c != ''] == size:
                print(l + ' : Yes')
                res += 1
            else:
                print(l + ' : No')

    return res


def two(data):
    res = 0
    possible = ['.', '#']

    for line in data:
        springs, size = line.split(' ')
        size = [int(s) for s in size.split(',')]

        sp = list(springs)
        sz = list(size)
        for _ in range(4):
            sp.extend('?')
            sp.extend(springs)
            sz.extend(size)
        springs = ''.join([s for s in sp])
        size = sz
        missing = [i for i, c in enumerate(springs) if c == '?']

        # TODO Implement a dynamic programming solution
        permutations = list(itertools.product(possible, repeat=len(missing)))
        for p in permutations:
            l = springs
            for m in range(len(missing)):
                l = l[:missing[m]] + p[m] + l[missing[m] + 1:]

            if [len(c) for c in l.split('.') if c != ''] == size:
                print(l)
                res += 1

    return res


if __name__ == '__main__':
    data = get_data(True)

    # print(one(data))
    print(two(data))
