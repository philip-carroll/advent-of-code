import math


def tpos(hx, hy, tx, ty):
    if (hx - tx) == 2 and hy == ty:
        tx += 1
    elif (tx - hx) == 2 and hy == ty:
        tx -= 1
    elif (hy - ty) == 2 and hx == tx:
        ty += 1
    elif (ty - hy) == 2 and hx == tx:
        ty -= 1
    elif math.dist((hx, hy), (tx, ty)) > 2:
        if hx > tx:
            tx += 1
        else:
            tx -= 1
        if hy > ty:
            ty += 1
        else:
            ty -= 1

    return tx, ty


def one():
    rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    positions = []

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()

            direction = line.split(' ')[0]
            steps = int(line.split(' ')[1])

            # track the head
            for i in range(steps):
                hx, hy = rope[0]
                if direction == 'U':
                    hy += 1
                elif direction == 'D':
                    hy -= 1
                elif direction == 'L':
                    hx -= 1
                elif direction == 'R':
                    hx += 1
                rope[0] = (hx, hy)

                # print('h: (%s,%s)' % (hx, hy))
                # print(math.dist((hx, hy), (tx, ty)))
                # print('t: (%s,%s)' % (tx, ty))

                for i in range(1, len(rope)):
                    rope[i] = tpos(rope[i - 1][0], rope[i - 1][1], rope[i][0], rope[i][1])
                    print(rope)
                print('----------')

                positions.append(rope[len(rope) - 1])

    return len(set(positions))


def two():
    pass


if __name__ == '__main__':
    print(one())
    # print(two())
