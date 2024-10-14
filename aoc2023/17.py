from pprint import pprint
from collections import defaultdict
from utils.search_utils import dijkstra


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
    graph = defaultdict(dict)
    x, y = len(data), len(data[0])
    # x, y = 4, 4

    for i in range(x):
        for j in range(y):
            if i > 0:
                node = (i - 1, j)
                # graph[(i, j)][node] = int(data[i - 1][j])  # up
                graph[(i, j)][node] = ('U', int(data[i - 1][j]))  # up
            if i < x - 1:
                node = (i + 1, j)
                # graph[(i, j)][node] = int(data[i + 1][j])  # down
                graph[(i, j)][node] = ('D', int(data[i + 1][j]))  # down
            if j > 0:
                node = (i, j - 1)
                # graph[(i, j)][node] = int(data[i][j - 1])  # left
                graph[(i, j)][node] = ('L', int(data[i][j - 1]))  # left
            if j < y - 1:
                node = (i, j + 1)
                # graph[(i, j)][node] = int(data[i][j + 1])  # right
                graph[(i, j)][node] = ('R', int(data[i][j + 1]))  # right

    # return dijkstra_pure(graph, (0, 0))
    # return dijkstra(graph, (0, 0), max_steps=3)
    res = dijkstra(graph, (0, 0), 10, 4)
    return {k: v for k, v in res.items() if k[0] == (x - 1, y - 1) and k[2] >= 4}


def two(data):
    return data


if __name__ == '__main__':
    data = get_data(False)

    pprint(one(data))
    # print(two(data))
