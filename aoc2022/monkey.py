from collections import defaultdict
import math


def one():
    monkeys = defaultdict(dict)

    with open('advent\monkey.txt') as f:
        monkey = None

        for line in f.readlines():
            line = line.rstrip()

            if line.startswith('Monkey '):
                monkey = int(line.split(' ')[1].rstrip(':'))
                monkeys[monkey]['insp'] = 0
            elif line.startswith('  Starting items: '):
                monkeys[monkey]['items'] = [
                    int(i) for i in line.lstrip('  Starting items: ').split(',')]
            elif line.startswith('  Operation: new = old '):
                monkeys[monkey]['op'] = line.lstrip('  Operation: new = old ')
            elif line.startswith('  Test: '):
                monkeys[monkey]['test'] = line.lstrip('  Test: ')
            elif line.startswith('    If true: throw to monkey '):
                monkeys[monkey]['t'] = int(
                    line.lstrip('    If true: throw to monkey '))
            elif line.startswith('    If false: throw to monkey '):
                monkeys[monkey]['f'] = int(line.lstrip(
                    '    If false: throw to monkey '))

        for i in range(0, 20):
            for m, v in monkeys.items():
                monkey = monkeys[m]
                for item in monkey['items']:
                    monkey['insp'] += 1
                    item = operate(item, monkey['op'])
                    item = item // 3
                    if evaluate(item, monkey['test']):
                        recipient = monkey['t']
                    else:
                        recipient = monkey['f']
                    monkeys[recipient]['items'].append(item)
                monkey['items'] = []

            insps = []
            for m, v in monkeys.items():
                insps.append(monkeys[m]['insp'])
            insps.sort(reverse=True)

    return insps[0] * insps[1]


def two():
    monkeys = defaultdict(dict)
    cd = 1

    with open('advent\monkey.txt') as f:
        monkey = None

        for line in f.readlines():
            line = line.rstrip()

            if line.startswith('Monkey '):
                monkey = int(line.split(' ')[1].rstrip(':'))
                monkeys[monkey]['insp'] = 0
            elif line.startswith('  Starting items: '):
                monkeys[monkey]['items'] = [int(i) for i in line.lstrip('  Starting items: ').split(',')]
            elif line.startswith('  Operation: new = old '):
                monkeys[monkey]['op'] = line.lstrip('  Operation: new = old ')
            elif line.startswith('  Test: '):
                monkeys[monkey]['test'] = line.lstrip('  Test: ')
            elif line.startswith('    If true: throw to monkey '):
                monkeys[monkey]['t'] = int(line.lstrip('    If true: throw to monkey '))
            elif line.startswith('    If false: throw to monkey '):
                monkeys[monkey]['f'] = int(line.lstrip('    If false: throw to monkey '))

        # Chinese Remainder Theorem
        for m, v in monkeys.items():
            monkey = monkeys[m]
            test = monkey['test']
            cd = cd * int(test.lstrip('divisible by '))

        for i in range(0, 10000):
            for m, v in monkeys.items():
                monkey = monkeys[m]
                for item in monkey['items']:
                    monkey['insp'] += 1
                    item = operate(item, monkey['op'])
                    item = math.floor(item % cd)
                    if evaluate(item, monkey['test']):
                        recipient = monkey['t']
                    else:
                        recipient = monkey['f']
                    monkeys[recipient]['items'].append(item)
                monkey['items'] = []

            insps = []
            for m, v in monkeys.items():
                insps.append(monkeys[m]['insp'])
            insps.sort(reverse=True)

    return insps[0] * insps[1]


def operate(item, op):
    if op == '* old':
        op = '* ' + str(item)

    s, o = op.split()

    if s == '+':
        r = item + int(o)
    elif s == '-':
        r = item - int(o)
    elif s == '*':
        r = item * int(o)
    if s == '/':
        r = item / int(o)

    return r


def evaluate(item, test):
    test = int(test.lstrip('divisible by '))
    return item % test == 0


if __name__ == '__main__':
    # print(one())
    print(two())
