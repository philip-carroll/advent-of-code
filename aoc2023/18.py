import numpy as np
import matplotlib.pyplot as plt
from shapely import Polygon, Point

directions = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}


def plt_grid(grid):
    plot = plt.subplot()
    plot.invert_yaxis()

    x = [g[0] for g in grid]
    y = [g[1] for g in grid]
    plot.plot(x, y)

    plt.grid()
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    plt.yticks(np.arange(min(y), max(y) + 1, 1.0))
    plt.show()


def shoelace(grid):
    grid.reverse()
    sum1 = 0
    sum2 = 0

    for i in range(len(grid)):
        try:
            sum1 += grid[i][0] * grid[i + 1][1]
        except IndexError:
            sum1 += grid[i][0] * grid[0][1]
        try:
            sum2 += grid[i][1] * grid[i + 1][0]
        except IndexError:
            sum2 += grid[i][1] * grid[0][0]

    res = abs(sum1 - sum2)

    return res / 2


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
    x, y = (0, 0)
    grid = []

    for line in data:
        direction, steps, colour = line.split(' ')
        steps = int(steps)

        if direction == 'U':
            y = y - steps
        elif direction == 'D':
            y = y + steps
        elif direction == 'L':
            x = x - steps
        elif direction == 'R':
            x = x + steps

        grid.append((x, y))

    poly = Polygon(grid)
    area = 0
    minx, maxx = min([x for x, y in grid]), max([x for x, y in grid]) + 1
    miny, maxy = min([y for x, y in grid]), max([y for x, y in grid]) + 1
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            p = Point(x, y)
            if p.within(poly):
                area += 1

    # print(area)
    # print(poly.exterior.length)
    return area + poly.exterior.length


def two(data):
    x, y = (0, 0)
    grid = []

    for line in data:
        direction, steps, colour = line.split(' ')
        direction = directions[colour[-2]]
        steps = int(''.join([n for n in colour[2:7]]), 16)
        if direction == 'U':
            y = y - steps
        elif direction == 'D':
            y = y + steps
        elif direction == 'L':
            x = x - steps
        elif direction == 'R':
            x = x + steps

        grid.append((x, y))

    poly = Polygon(grid)
    border = (poly.exterior.length / 2) + 1  # account for the border around grid
    return shoelace(grid) + border


if __name__ == '__main__':
    data = get_data(False)

    print(one(data))
    print(two(data))
    # plt_grid(grid)
