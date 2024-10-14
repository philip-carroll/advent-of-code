import re


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
    nums = get_nums(data)

    for i in range(len(nums)):
        covered = ''
        for j in range(len(nums[i])):
            num = nums[i][j]
            done = False
            dupes = covered.count(num)
            if dupes > 0:
                loc = [m.start() for m in re.finditer(nums[i][j], data[i])][dupes]
            else:
                loc = [m.start() for m in re.finditer(nums[i][j], data[i])][0]
            rows = [i - 1, i, i + 1]
            cols = list(range(loc - 1, loc + len(num) + 1))

            if not done:
                for x in rows:
                    for y in cols:
                        try:
                            cell = data[x][y]
                            if not cell.isnumeric() and not cell == '.':
                                res.append(int(num))
                                done = True
                        except IndexError:
                            pass
            covered = covered + ' ' + num
            print('%s: %s: %s: %s: %s' % (loc, nums[i][j], rows, cols, done))

    return sum(res)


def two(data):
    res = []
    nums = get_nums(data)

    for i in range(len(nums)):
        covered = ''
        for j in range(len(nums[i])):
            num = nums[i][j]
            done = False
            dupes = covered.count(num)
            if dupes > 0:
                loc = [m.start() for m in re.finditer(nums[i][j], data[i])][dupes]
            else:
                loc = [m.start() for m in re.finditer(nums[i][j], data[i])][0]
            rows = [i - 1, i, i + 1]
            cols = list(range(loc - 1, loc + len(num) + 1))

            if not done:
                for x in rows:
                    for y in cols:
                        try:
                            cell = data[x][y]
                            if cell == '*':
                                res.append((int(num), (x, y)))
                                done = True
                        except IndexError:
                            pass
            covered = covered + ' ' + num
            print('%s: %s: %s: %s: %s' % (loc, nums[i][j], rows, cols, done))

    res2 = []
    for i in res:
        for j in res:
            if i > j and i[1] == j[1]:
                res2.append(i[0] * j[0])

    return sum(res2)


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
