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
    nums = []
    for l in data:
        n = [c for c in l if c.isnumeric()]
        nums.append(int(n[0] + n[-1]))

    return sum(nums)


def two(data):
    words = {
        'one': 'o1e',
        'two': 't2o',
        'three': 'th3ee',
        'four': 'fo4r',
        'five': 'fi5e',
        'six': 's6x',
        'seven': 'se7en',
        'eight': 'ei8ht',
        'nine': 'ni9e',
    }

    nums = []
    for l in data:
        if not (l[0].isnumeric() and l[-1].isnumeric()):
            for k, v in words.items():
                l = l.replace(k, v)

        n = [c for c in l if c.isnumeric()]
        n = int(n[0] + n[-1])
        nums.append(n)

    return sum(nums)


if __name__ == '__main__':
    data = get_data(True)

    # print(one(data))
    print(two(data))
