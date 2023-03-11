import ast
import matplotlib.pyplot as plt


def prepare():
    res = []

    with open('sand.txt') as f:
        for line in f.readlines():
            line = line.rstrip()
            path = [ast.literal_eval(p) for p in line.split('->')]
            for i in range(len(path) - 1):
                sx, sy, ex, ey = path[i][0], path[i][1], path[i + 1][0], path[i + 1][1]
                res.append(path[i])
                if sx > ex:  # left
                    res.extend([(g, sy) for g in range(ex + 1, sx)])
                elif sx < ex:  # right
                    res.extend([(g, sy) for g in range(sx, ex + 1)])
                elif sy > ey:  # down
                    res.extend([(sx, g) for g in range(ey, sy + 1)])
                elif sy < ey:  # up
                    res.extend([(sx, g) for g in range(sy + 1, ey)])
                res.append(path[i + 1])

    return res


def sandfall(walls, balls, point, bottom):
    walls = walls.union(balls)

    if point[1] + 1 < bottom:
        if (point[0], point[1] + 1) not in walls:  # down
            pt = (point[0], point[1] + 1)
        elif (point[0] - 1, point[1] + 1) not in walls:  # down left
            pt = (point[0] - 1, point[1] + 1)
        elif (point[0] + 1, point[1] + 1) not in walls:  # down right
            pt = (point[0] + 1, point[1] + 1)
        else:
            pt = point
    else:
        pt = point

    # if pt[1] > bottom:
    if pt[1] <= 0:
        return False
    else:
        return pt


def one():
    walls = prepare()
    bottom = max([x[1] for x in walls])
    balls = []

    p = (500, 0)
    while p:
        p = (500, 0)
        q = None
        while q != p and p:
            q = p
            p = sandfall(walls, balls, p, bottom)
        if p:
            balls.append(p)

    print(len(balls))

    plt.plot([x[0] for x in walls], [x[1] for x in walls], 'bo')
    plt.plot([x[0] for x in balls], [x[1] for x in balls], 'r+')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()


def two():
    walls = set(prepare())
    bottom = max([x[1] for x in walls]) + 2
    balls = set()

    p = (500, 0)

    # i = 0
    # while p:
    for i in range(1000):
        p = (500, 0)
        q = None
        while q != p and p:
            q = p
            p = sandfall(walls, balls, p, bottom)
        if p:
            balls.add(p)
            print('%s: %s' % (i, p))
            # i += 1

    print(len(balls) + 1)

    plt.plot([x[0] for x in walls], [x[1] for x in walls], 'bo')
    plt.plot([x[0] for x in balls], [x[1] for x in balls], 'r+')
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()


if __name__ == '__main__':
    # one()
    two()
