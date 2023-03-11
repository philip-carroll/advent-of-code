priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}


def one():
    score = 0

    with open('rucksack.txt') as f:
        for line in f.readlines():
            line = line.rstrip()
            if len(line) % 2 != 0:
                print(line)

            half = int(len(line) / 2)
            r1 = line[0:half]
            r2 = line[half:len(line)]

            print('%s : %s' % (r1, r2))
            for c in r1:
                if c in r2:
                    p = priorities[c]
                    score += p
                    print('%s : %s' % (c, p))
                    break

        print(score)


def two():
    score = 0
    idx = 0
    lines = []
    with open('rucksack.txt') as f:
        for line in f.readlines():
            line = line.rstrip()
            print(line)
            idx += 1
            lines.append(line)

            if idx == 3:
                for c in lines[0]:
                    if c in lines[1] and c in lines[2]:
                        p = priorities[c]
                        score += p
                        print('%s : %s' % (c, p))
                        break

                idx = 0
                lines = []

        print(score)


if __name__ == '__main__':
    # one()
    two()
