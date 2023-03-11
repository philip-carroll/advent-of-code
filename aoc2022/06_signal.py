def one():
    with open('signal.txt') as f:
        for line in f.readlines():
            for i in range(3, len(line)):
                if line[i] not in line[i - 3:i] and \
                        line[i - 1] not in line[i - 3:i - 1] and \
                        line[i - 2] not in line[i - 3:i - 2]:
                    return i + 1


def two():
    with open('signal.txt') as f:
        for line in f.readlines():
            for i in range(13, len(line)):
                if line[i] not in line[i - 13:i] and \
                        line[i - 1] not in line[i - 13:i - 1] and \
                        line[i - 2] not in line[i - 13:i - 2] and \
                        line[i - 3] not in line[i - 13:i - 3] and \
                        line[i - 4] not in line[i - 13:i - 4] and \
                        line[i - 5] not in line[i - 13:i - 5] and \
                        line[i - 6] not in line[i - 13:i - 6] and \
                        line[i - 7] not in line[i - 13:i - 7] and \
                        line[i - 8] not in line[i - 13:i - 8] and \
                        line[i - 9] not in line[i - 13:i - 9] and \
                        line[i - 10] not in line[i - 13:i - 10] and \
                        line[i - 11] not in line[i - 13:i - 11]:
                    return i + 1


if __name__ == '__main__':
    # print(one())
    print(two())
