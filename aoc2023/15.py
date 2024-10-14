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


def hash(text):
    res = 0
    for c in text:
        code = ord(c)
        res += code
        res = res * 17
        res = res % 256

    return res


def one(data):
    res = 0
    for step in data[0].split(','):
        res += hash(step)

    return res


def two(data):
    res = 0

    boxes = {i: OrderedDict() for i in range(256)}
    for step in data[0].split(','):
        if '=' in step:
            op = '='
            label = step.split('=')[0]
            focal = step.split('=')[1]
        else:
            op = '-'
            label = step.split('-')[0]

        box = hash(label)
        if op == '-':
            if label in boxes[box]:
                del boxes[box][label]
        else:
            boxes[box][label] = focal

    for k, v in boxes.items():
        slot = 1
        for k2, v2 in v.items():
            res += (k + 1) * slot * int(v2)
            slot += 1

    return res


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
