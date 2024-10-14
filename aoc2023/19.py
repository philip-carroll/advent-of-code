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


def get_workflows(data):
    workflows = {}

    for wf in data:
        k, vs = wf.split('{')
        workflows[k] = []
        for v in vs.split(',')[:-1]:
            a = v[0]
            b, c = v[1:].split(':')
            workflows[k].append((a, b, c))

        workflows[k].append(vs.split(',')[-1][:-1])

    return workflows


def trim_ranges(part, operator, operand, ranges):
    good = ranges.copy()
    bad = ranges.copy()

    if part == 'x':
        if operator == '<':
            good[0] = range(good[0][0], min(int(operand), good[0][-1] + 1))
            bad[0] = range(max(bad[0][0], int(operand)), bad[0][-1] + 1)
        elif operator == '>':
            good[0] = range(max(good[0][0], int(operand) + 1), good[0][-1] + 1)
            bad[0] = range(bad[0][0], min(int(operand) + 1, bad[0][-1]))
    elif part == 'm':
        if operator == '<':
            good[1] = range(good[1][0], min(int(operand), good[1][-1] + 1))
            bad[1] = range(max(bad[1][0], int(operand)), bad[1][-1] + 1)
        elif operator == '>':
            good[1] = range(max(good[1][0], int(operand) + 1), good[1][-1] + 1)
            bad[1] = range(bad[1][0], min(int(operand) + 1, bad[1][-1]))
    elif part == 'a':
        if operator == '<':
            good[2] = range(good[2][0], min(int(operand), good[2][-1] + 1))
            bad[2] = range(max(bad[2][0], int(operand)), bad[2][-1] + 1)
        elif operator == '>':
            good[2] = range(max(good[2][0], int(operand) + 1), good[2][-1] + 1)
            bad[2] = range(bad[2][0], min(int(operand) + 1, bad[2][-1]))
    elif part == 's':
        if operator == '<':
            good[3] = range(good[3][0], min(int(operand), good[3][-1] + 1))
            bad[3] = range(max(bad[3][0], int(operand)), bad[3][-1] + 1)
        elif operator == '>':
            good[3] = range(max(good[3][0], int(operand) + 1), good[3][-1] + 1)
            bad[3] = range(bad[3][0], min(int(operand) + 1, bad[3][-1]))

    return good, bad


def evaluate(rating, workflow, workflows):
    for rule in workflows[workflow]:
        if type(rule) is str:
            return rule

        part = rule[0]
        operator = rule[1][0]
        operand = rule[1][1:]
        path = rule[2]

        for r in rating.split(','):
            k, v = r.split('=')
            if k == part:
                if (operator == '<' and int(v) < int(operand)) or (operator == '>' and int(v) > int(operand)):
                    return path


def evaluate_range(accepted, ranges, path, workflow, workflows):
    path += '->' + workflow

    if workflow == 'A':
        accepted.append(ranges)
        print('%s : %s' % (path, ranges))
        return accepted
    elif workflow != 'R':
        bad = ranges
        for rule in workflows[workflow]:
            if type(rule) is str:
                workflow = rule
                evaluate_range(accepted, bad, path, workflow, workflows)
            else:
                part = rule[0]
                operator = rule[1][0]
                operand = rule[1][1:]
                workflow = rule[2]
                good, bad = trim_ranges(part, operator, operand, bad)

                evaluate_range(accepted, good, path, workflow, workflows)

    return accepted


def one(data):
    i = data.index('')
    workflows = get_workflows(data[:i])
    parts = data[i + 1:]

    accepted = []

    for p in parts:
        l = p + ': in'
        p = p.removeprefix('{').removesuffix('}')
        res = 'in'
        while res not in ('A', 'R'):
            res = evaluate(p, res, workflows)
            l += ' -> ' + res

        if res == 'A':
            accepted.append(p)

        print(l)

    total = 0
    for parts in accepted:
        for p in parts.split(','):
            k, v = p.split('=')
            total += int(v)

    return total


def two(data):
    i = data.index('')
    workflows = get_workflows(data[:i])

    accepted = evaluate_range(
        [],
        [range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001)],
        '',
        'in',
        workflows)

    return sum([len(i[0]) * len(i[1]) * len(i[2]) * len(i[3]) for i in accepted])


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
