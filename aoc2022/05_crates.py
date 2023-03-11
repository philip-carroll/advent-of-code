import textwrap


def setup_crates():
    l1, l2, l3, l4, l5, l6, l7, l8, l9 = [], [], [], [], [], [], [], [], []
    l = [l1, l2, l3, l4, l5, l6, l7, l8, l9]
    # l1, l2, l3 = [], [], []
    # l = [l1, l2, l3]

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()
            if line == ' 1   2   3   4   5   6   7   8   9':
            # if line == ' 1   2   3':
                break
            else:
                i = 0
                for c in textwrap.wrap(line, 4, drop_whitespace=False):
                    if '[' in c:
                        l[i].insert(0, c.replace('[', '').replace(']', '').replace(' ', ''))
                    i += 1

    return l


def one():
    l = setup_crates()

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            if line.startswith('move'):
                parsed = line.split(' ')
                moves = int(parsed[1])
                froms = int(parsed[3]) - 1
                tos = int(parsed[5]) - 1

                for i in range(moves):
                    l[tos].append(l[froms].pop())
                    print(l)

                print('\n')

    s = ''
    for i in range(len(l)):
        s = s + str(l[i].pop())

    return s


def two():
    l = setup_crates()

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            if line.startswith('move'):
                parsed = line.split(' ')
                moves = int(parsed[1])
                froms = int(parsed[3]) - 1
                tos = int(parsed[5]) - 1

                l[tos] = l[tos] + l[froms][-moves:]
                del l[froms][-moves:]
                print(l)

    s = ''
    for i in range(len(l)):
        s = s + str(l[i].pop())

    return s


if __name__ == '__main__':
    # print(setup_crates())
    # print(one())
    print(two())
