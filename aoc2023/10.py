import numpy as np
import matplotlib.pyplot as plt

pipes = {
    '.': [],
    '|': ['N', 'S'],  # is a vertical pipe connecting north and south.
    '-': ['E', 'W'],  # is a horizontal pipe connecting east and west.
    'L': ['N', 'E'],  # is a 90-degree bend connecting north and east.
    'J': ['N', 'W'],  # is a 90-degree bend connecting north and west.
    '7': ['S', 'W'],  # is a 90-degree bend connecting south and west.
    'F': ['S', 'E']  # is a 90-degree bend connecting south and east.
}


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


def plt_loop(loop, gaps):
    plot = plt.subplot()
    plot.invert_yaxis()

    lx = [l[1] for l in loop]
    ly = [l[0] for l in loop]
    plot.plot(lx, ly)

    gx = [g[0] for g in gaps]
    gy = [g[1] for g in gaps]
    plot.plot(gx, gy, 'ro')

    plt.grid()
    plt.xticks(np.arange(min(lx), max(lx) + 1, 1.0))
    plt.yticks(np.arange(min(ly), max(ly) + 1, 1.0))
    plt.show()


def one(data):
    loop = []

    for i in range(len(data)):
        data[i] = list(data[i])
        if 'S' in data[i]:
            s = [i, data[i].index('S')]

    d = s
    dir = None
    start = True
    while d != s or start:
        north = [d[0] - 1, d[1]]
        east = [d[0], d[1] + 1]
        south = [d[0] + 1, d[1]]
        west = [d[0], d[1] - 1]

        if start:
            start = False

            if 'S' in pipes[data[north[0]][north[1]]]:
                d = north
                dir = 'N'
            elif 'W' in pipes[data[east[0]][east[1]]]:
                d = east
                dir = 'E'
            elif 'N' in pipes[data[south[0]][south[1]]]:
                d = south
                dir = 'S'
            elif 'E' in pipes[data[west[0]][west[1]]]:
                d = west
                dir = 'W'
        else:
            pipea = pipes[data[d[0]][d[1]]]
            pipe = pipea.copy()
            if dir == 'N':
                pipe.remove('S')
            elif dir == 'E':
                pipe.remove('W')
            elif dir == 'S':
                pipe.remove('N')
            elif dir == 'W':
                pipe.remove('E')
            dir = pipe[0]
            if dir == 'N':
                d = north
            if dir == 'E':
                d = east
            if dir == 'S':
                d = south
            if dir == 'W':
                d = west

        loop.append(d)

    plt_loop(loop)
    return len(loop) / 2


def two(data):
    loop = []

    for i in range(len(data)):
        data[i] = list(data[i])
        if 'S' in data[i]:
            s = [i, data[i].index('S')]

    d = s
    dir = None
    start = True
    while d != s or start:
        north = [d[0] - 1, d[1]]
        east = [d[0], d[1] + 1]
        south = [d[0] + 1, d[1]]
        west = [d[0], d[1] - 1]

        if start:
            start = False

            if 'S' in pipes[data[north[0]][north[1]]]:
                d = north
                dir = 'N'
            elif 'W' in pipes[data[east[0]][east[1]]]:
                d = east
                dir = 'E'
            elif 'N' in pipes[data[south[0]][south[1]]]:
                d = south
                dir = 'S'
            elif 'E' in pipes[data[west[0]][west[1]]]:
                d = west
                dir = 'W'
        else:
            pipea = pipes[data[d[0]][d[1]]]
            pipe = pipea.copy()
            if dir == 'N':
                pipe.remove('S')
            elif dir == 'E':
                pipe.remove('W')
            elif dir == 'S':
                pipe.remove('N')
            elif dir == 'W':
                pipe.remove('E')
            dir = pipe[0]
            if dir == 'N':
                d = north
            if dir == 'E':
                d = east
            if dir == 'S':
                d = south
            if dir == 'W':
                d = west

        loop.append(d)

    from shapely import Polygon, Point
    poly = Polygon(loop)

    gaps = []
    xs = [l[1] for l in loop]
    ys = [l[0] for l in loop]
    for x in range(max(xs) + 1):
        for y in range(max(ys) + 1):
            p = Point(y, x)
            print(p)
            if p.within(poly):
                gaps.append([x, y])

    # plt_loop(loop, gaps)
    return len(gaps)


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))
