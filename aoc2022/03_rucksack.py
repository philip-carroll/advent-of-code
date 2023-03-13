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


def get_contents():
    contents = []

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            contents.append(line.rstrip())

    return contents


def one(contents):
    score = 0

    for c in contents:
        half = int(len(c) / 2)
        r1 = c[0:half]
        r2 = c[half:len(c)]

        for r in r1:
            if r in r2:
                p = priorities[r]
                score += p
                break

    return score


def two(contents):
    score = 0
    idx = 0
    lines = []

    for c in contents:
        idx += 1
        lines.append(c)

        if idx == 3:
            for r in lines[0]:
                if r in lines[1] and r in lines[2]:
                    score += priorities[r]
                    break

            idx = 0
            lines = []

    return score


if __name__ == '__main__':
    contents = get_contents()

    print(one(contents))
    print(two(contents))
