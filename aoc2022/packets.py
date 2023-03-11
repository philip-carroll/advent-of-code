import ast


def prepare():
    res = []

    with open('packets.txt') as f:
        i = 0
        left = None
        right = None
        for line in f.readlines():
            line = line.rstrip()
            i += 1
            if i % 3 == 1:
                left = ast.literal_eval(line)
            elif i % 3 == 2:
                right = ast.literal_eval(line)
                res.append((left, right))

    return res


def prepare2():
    res = [[[2]], [[6]]]

    with open('packets.txt') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line != '':
                res.append(ast.literal_eval(line))

    return res


def recur(left, right, level):
    res = None

    i = 0
    while res is None and i < min(len(left), len(right)):
        l, r = left[i], right[i]
        print('\t' * level + 'Compare %s vs %s' % (l, r))

        # both values are integers
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
        # both values are lists
        elif type(l) == list and type(r) == list:
            res = recur(l, r, level + 1)
        # exactly one value is an integer
        elif type(l) == list:
            res = recur(l, [r], level + 1)
        elif type(r) == list:
            res = recur([l], r, level + 1)

        i += 1

    # iteration has not separated packets
    if res is None:
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False

    return res


if __name__ == '__main__':
    total = 0
    ps = []
    packets = prepare2()

    # for packet in packets:
    #     print('Compare %s vs %s' % (packet[0], packet[1]))
    #     ps.append(recur(packet[0], packet[1], level=1))
    # print(ps)
    #
    # for i in range(len(ps)):
    #     if ps[i]:
    #         total += i + 1
    # print(total)

    for i in range(len(packets)):
        # initially swapped is false
        swapped = False
        i = 0
        while i < len(packets) - 1:
            # comparing the adjacent elements
            if not recur(packets[i], packets[i + 1], level=1):
                # swapping
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                # Changing the value of swapped
                swapped = True
            i = i + 1
        # if swapped is false then the list is sorted
        # we can stop the loop
        if swapped == False:
            break

    a = packets.index([[2]]) + 1
    b = packets.index([[6]]) + 1
    print(a * b)
