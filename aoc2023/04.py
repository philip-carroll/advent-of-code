import re
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


def get_nums(data):
    nums = []

    for i in range(len(data)):
        nums.append(re.findall(r'\d+', data[i]))

    return nums


def one(data):
    res = []

    for card in data:
        nums = card.split(':')
        win, you = nums[1].split('|')
        win = [int(w) for w in win.split(' ') if w.isnumeric()]
        you = [int(y) for y in you.split(' ') if y.isnumeric()]

        hits = 0
        for y in you:
            if y in win:
                if hits == 0:
                    hits = 1
                else:
                    hits = hits * 2

        res.append(hits)

    return sum(res)


def two(data):
    res = OrderedDict()
    i = 1

    for card in data:
        res[i] = 0
        nums = card.split(':')
        win, you = nums[1].split('|')
        win = [int(w) for w in win.split(' ') if w.isnumeric()]
        you = [int(y) for y in you.split(' ') if y.isnumeric()]

        for y in you:
            if y in win:
                res[i] += 1

        i += 1

    res2 = [k for k, v in res.items()]
    print(res)
    for k, v in res.items():
        if v > 0:
            res2.extend(res2.count(k) * [k + 1 for k in range(k, k + v)])
        # print(res2)

    return len(res2)


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
