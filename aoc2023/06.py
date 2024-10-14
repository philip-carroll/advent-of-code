import numpy


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
    times = []
    distances = []

    for line in data:
        if line.startswith('Time:'):
            times.extend([int(t) for t in line.split(':')[1].split(' ') if t.isnumeric()])
        elif line.startswith('Distance:'):
            distances.extend([int(d) for d in line.split(':')[1].split(' ') if d.isnumeric()])

    res = [0 for t in range(len(times))]
    for i in range(len(times)):
        for j in range(times[i]):
            speed = j
            dist = speed * (times[i] - j)
            if dist > distances[i]:
                res[i] += 1

    return numpy.prod(res)


def two(data):
    for line in data:
        if line.startswith('Time:'):
            times = int(''.join([t for t in line.split(':')[1] if t.isnumeric()]))
        elif line.startswith('Distance:'):
            distances = int(''.join([d for d in line.split(':')[1] if d.isnumeric()]))

    res = 0
    for j in range(times):
        if j % 1000 == 0:
            print(j)
        speed = j
        dist = speed * (times - j)
        if dist > distances:
            res += 1

    return res


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))  # 71503 too low
