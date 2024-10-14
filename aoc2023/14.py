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


def move_north(data):
    moving = True
    moves = 0
    while moving:
        moving = False
        for i in range(1, len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 'O' and data[i - 1][j] == '.':
                    data[i][j] = '.'
                    data[i - 1][j] = 'O'
                    moving = True
                    moves += 1

    return data, moves


def move_south(data):
    moving = True
    moves = 0
    while moving:
        moving = False
        for i in range(len(data) - 1):
            for j in range(len(data[0])):
                if data[i][j] == 'O' and data[i + 1][j] == '.':
                    data[i][j] = '.'
                    data[i + 1][j] = 'O'
                    moving = True
                    moves += 1

    return data, moves


def move_east(data):
    moving = True
    moves = 0
    while moving:
        moving = False
        for i in range(len(data)):
            for j in range(len(data[0]) - 1):
                if data[i][j] == 'O' and data[i][j + 1] == '.':
                    data[i][j] = '.'
                    data[i][j + 1] = 'O'
                    moving = True
                    moves += 1

    return data, moves


def move_west(data):
    moving = True
    moves = 0
    while moving:
        moving = False
        for i in range(len(data)):
            for j in range(1, len(data[0])):
                if data[i][j] == 'O' and data[i][j - 1] == '.':
                    data[i][j] = '.'
                    data[i][j - 1] = 'O'
                    moving = True
                    moves += 1

    return data, moves


def one(data):
    total = 0

    for i in range(len(data)):
        data[i] = list(data[i])

    data = move_north(data)

    for i in range(0, len(data)):
        total += sum(1 if x == 'O' else 0 for x in data[i]) * (len(data) - i)

    return total


def two(data):
    total = 0

    for i in range(len(data)):
        data[i] = list(data[i])

    i = 1
    history = []
    done = False
    while not done:
        data, mn = move_north(data)
        data, mw = move_west(data)
        data, ms = move_south(data)
        data, me = move_east(data)
        shift = 'N%s W%s S%s E%s' % (mn, mw, ms, me)
        # print(shift)
        if shift not in history:
            history.append(shift)
        else:
            start = history.index(shift) + 1
            end = i
            print('Cycle Start: %s Cycle End: %s' % (start, end - 1))
            done = True
        i += 1

    remainder = (1000000000 - end) % (end - start)
    for i in range(remainder):
        data, mn = move_north(data)
        data, mw = move_west(data)
        data, ms = move_south(data)
        data, me = move_east(data)

    for i in range(0, len(data)):
        total += sum(1 if x == 'O' else 0 for x in data[i]) * (len(data) - i)

    return total


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
