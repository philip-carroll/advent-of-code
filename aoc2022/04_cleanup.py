def get_assignments():
    assignments = []

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()

            range1, range2 = line.split(',')
            range1start, range1end = range1.split('-')
            range2start, range2end = range2.split('-')
            range1 = set(range(int(range1start), int(range1end) + 1))
            range2 = set(range(int(range2start), int(range2end) + 1))
            assignments.append((range1, range2))

    return assignments


def one(assignments):
    score = 0

    for range1, range2 in assignments:
        if range1.issubset(range2) or range2.issubset(range1):
            score += 1

    return score


def two(assignments):
    score = 0

    for range1, range2 in assignments:
        if range1.intersection(range2):
            score += 1

    return score


if __name__ == '__main__':
    assignments = get_assignments()

    print(one(assignments))
    print(two(assignments))
