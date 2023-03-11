def one():
    score = 0

    with open('cleanup.txt') as f:
        for line in f.readlines():
            line = line.rstrip()

            e1, e2 = line.split(',')
            e10, e11 = e1.split('-')
            e20, e21 = e2.split('-')
            e1r = set(range(int(e10), int(e11) + 1))
            e2r = set(range(int(e20), int(e21) + 1))

            if e1r.issubset(e2r) or e2r.issubset(e1r):
                score += 1
                print(e1r)
                print(e2r)

    return score


def two():
    score = 0

    with open('cleanup.txt') as f:
        for line in f.readlines():
            line = line.rstrip()

            e1, e2 = line.split(',')
            e10, e11 = e1.split('-')
            e20, e21 = e2.split('-')
            e1r = set(range(int(e10), int(e11) + 1))
            e2r = set(range(int(e20), int(e21) + 1))

            if e1r.intersection(e2r):
                score += 1
                print(e1r)
                print(e2r)
                print(e1r.intersection(e2r))

    return score


if __name__ == '__main__':
    # print(one())
    print(two())
