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


def clean_data(data):
    games = {}
    round = 0
    for game in data:
        round += 1
        blue = []
        red = []
        green = []

        games[round] = {}

        start_index = 0
        for i in range(len(game)):
            j = game.find('blue', start_index)
            if (j != -1):
                blue.append(int(game[j - 3:j - 1]))
                start_index = j + 1
        games[round]['b'] = blue

        start_index = 0
        for i in range(len(game)):
            j = game.find('green', start_index)
            if (j != -1):
                green.append(int(game[j - 3:j - 1]))
                start_index = j + 1
        games[round]['g'] = green

        start_index = 0
        for i in range(len(game)):
            j = game.find('red', start_index)
            if (j != -1):
                red.append(int(game[j - 3:j - 1]))
                start_index = j + 1
        games[round]['r'] = red

    return games


def one(data):
    blue_limit = 14
    red_limit = 12
    green_limit = 13

    games = clean_data(data)

    res = []
    for g, v in games.items():
        if not any(i > blue_limit for i in v['b']) and not any(i > red_limit for i in v['r']) and not any(
                i > green_limit for i in v['g']):
            res.append(int(g))

    return sum(res)


def two(data):
    games = clean_data(data)

    res = []
    for g, v in games.items():
        max_b = max(v['b'])
        max_g = max(v['g'])
        max_r = max(v['r'])
        res.append(max_b * max_g * max_r)

    return sum(res)


if __name__ == '__main__':
    data = get_data(False)

    print(one(data))
    print(two(data))
