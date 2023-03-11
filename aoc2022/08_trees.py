def one():
    trees = []
    visible = 0

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()

            row = [int(n) for n in line]
            trees.append(row)

    visible += len(trees[0]) * 2
    visible += (len(trees) - 2) * 2

    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees[0]) - 1):
            tree = trees[x][y]
            print(tree)
            up = [r[y] for r in trees[0:x]]
            # print('Up: %s' % up)
            print('Up: %s' % len(up))
            down = [r[y] for r in trees[x + 1:len(trees)]]
            # print('Down: %s' % down)
            print('Down: %s' % len(down))
            left = trees[x][0:y]
            # print('Left: %s' % left)
            print('Left: %s' % len(left))
            right = trees[x][y + 1:]
            # print('Right: %s' % right)
            print('Right: %s' % len(right))

            if tree > max(up) or tree > max(down) or tree > max(left) or tree > max(right):
                visible += 1
        print('----------------------------')
    return visible


def two():
    trees = []
    max = 0

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()

            row = [int(n) for n in line]
            trees.append(row)

    for x in range(1, len(trees) - 1):
        for y in range(1, len(trees[0]) - 1):
            tree = trees[x][y]
            scenic = 0

            up = [r[y] for r in trees[0:x]]
            up = calc(tree, reversed(up))

            down = [r[y] for r in trees[x + 1:len(trees)]]
            down = calc(tree, down)

            left = trees[x][0:y]
            left = calc(tree, reversed(left))

            right = trees[x][y + 1:]
            right = calc(tree, right)

            scenic = up * down * left * right

            if scenic > max:
                max = scenic

    return max


def calc(tree, line):
    s = 0
    for h in line:
        if h < tree:
            s += 1
        else:
            s += 1
            break

    return s


if __name__ == '__main__':
    # print(one())
    print(two())
