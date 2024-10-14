from collections import Counter


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


values = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def one(data):
    res = 0
    hands = []
    for line in data:
        hands.append([[values[v] for v in line.split(' ')[0]], int(line.split(' ')[1]), 0])

    for hand in hands:
        for card in hand[0]:
            hand[2] += hand[0].count(card)

    for i in range(len(hands)):  # bubble sort
        for j in range(i + 1, len(hands)):
            if hands[i][2] > hands[j][2]:
                hands[i], hands[j] = hands[j], hands[i]
            elif hands[i][2] == hands[j][2]:
                done = False
                for k in range(len(hands[i][0])):
                    if not done:
                        if hands[i][0][k] > hands[j][0][k]:
                            hands[i], hands[j] = hands[j], hands[i]
                            done = True
                        elif hands[i][0][k] < hands[j][0][k]:
                            done = True

    for i in range(len(hands)):
        res += (i + 1) * hands[i][1]

    return res


def two(data):
    res = 0
    hands = []
    hands2 = []  # just used to track J's before we swap them out
    for line in data:
        hands.append([[values[v] for v in line.split(' ')[0]], int(line.split(' ')[1]), 0])
        hands2.append([[values[v] for v in line.split(' ')[0]], int(line.split(' ')[1]), 0])
    print(hands)

    for hand in hands:
        if hand[0] != [0, 0, 0, 0, 0]:
            max_count = max(hand[0].count(c) for c in hand[0] if c != 0)
            max_dupe = max(c for c in hand[0] if hand[0].count(c) == max_count and c != 0)
            for i in range(len(hand[0])):
                if hand[0][i] == 0:
                    hand[0][i] = max_dupe
        else:
            hand[0] = [14, 14, 14, 14, 14]
    for hand in hands:
        for card in hand[0]:
            hand[2] += hand[0].count(card)
    print(hands)

    for i in range(len(hands)):  # bubble sort
        for j in range(i + 1, len(hands)):
            swap = False
            if hands[i][2] > hands[j][2]:
                swap = True
            elif hands[i][2] == hands[j][2]:
                done = False
                for k in range(len(hands[i][0])):
                    if not done:
                        if hands2[i][0][k] > hands2[j][0][k]:
                            swap = True
                            done = True
                        elif hands2[i][0][k] < hands2[j][0][k]:
                            done = True
            if swap:
                hands[i], hands[j] = hands[j], hands[i]
                hands2[i], hands2[j] = hands2[j], hands2[i]
    print(hands)

    for i in range(len(hands)):
        res += (i + 1) * hands[i][1]

    return res


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data))
    print(two(data))  # 249526184 too low
