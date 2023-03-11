from collections import defaultdict


def one():
    measure = [20, 60, 100, 140, 180, 220]
    total = 0

    with open(__file__.replace('.py', '.txt')) as f:
        instructions = defaultdict(list)
        cycle = 1
        x = 1

        for line in f.readlines():
            line = line.rstrip()

            if line.startswith('addx'):
                v = line.split(' ')[1]
                instructions[cycle + 1].append(int(v))
                cycle += 2
            else:
                cycle += 1

        for i in range(1, max(instructions.keys()) + 1):
            x += sum(instructions[i])
            if (i + 1) in measure:
                total += (i + 1) * x

        return total


def two():
    s = ''

    with open(__file__.replace('.py', '.txt')) as f:
        instructions = defaultdict(list)
        cycle = 1
        x = 1

        for line in f.readlines():
            line = line.rstrip()

            if line.startswith('addx'):
                v = line.split(' ')[1]
                instructions[cycle + 1].append(int(v))
                cycle += 2
            else:
                cycle += 1

        # for i in range(1, max(instructions.keys()) + 1):
        #     x += sum(instructions[i])

        cycle = 0
        for i in range(0, 6):
            c = 0
            for j in range(0, 40):
                x += sum(instructions[cycle])
                if c - 1 == x or c == x or c + 1 == x:
                    s += '#'
                else:
                    s += '.'

                cycle += 1
                c += 1
            s += '\n'

        return s


if __name__ == '__main__':
    # print(one())
    print(two())
