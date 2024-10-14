from math import lcm


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


def prep_data(data):
    thelads = {}

    # set up objects
    for line in data:
        src, dest = line.split(' -> ')
        if src.startswith('%'):
            thelads[src.replace('%', '')] = FlipFlop(name=src.replace('%', ''))
        elif src.startswith('&'):
            thelads[src.replace('&', '')] = Conjunction(name=src.replace('&', ''))
        else:
            thelads[src] = Module(name=src)

    # set up destinations
    for line in data:
        src, dest = line.split(' -> ')
        src = src.replace('%', '').replace('&', '')
        for d in dest.split(','):
            d = d.strip()
            if d not in thelads:
                thelads[d] = Module(name=d)
            thelads[src].destinations.append(thelads[d])

    # set up inputs
    for line in data:
        src, dest = line.split(' -> ')
        src = src.replace('%', '').replace('&', '')
        for d in dest.split(','):
            d = d.strip()
            if type(thelads[d]) is Conjunction:
                thelads[d].last_pulses[thelads[src]] = False

    return thelads


messages = []


class Module:

    def __init__(self, name=None):
        self.name = name
        self.destinations = []

    def send(self, source, pulse: bool):
        for d in self.destinations:
            messages.append((self, d, pulse))


class FlipFlop(Module):
    def __init__(self, name=None):
        self.name = name
        self.destinations = []
        self.state = False  # initialise state to off

    def send(self, source, pulse: bool):
        if not pulse:  # low pulse
            self.state = not self.state  # flip state

            for d in self.destinations:
                if self.state:
                    messages.append((self, d, True))  # if now on send high pulse
                else:
                    messages.append((self, d, False))  # if now off send low pulse


class Conjunction(Module):
    def __init__(self, name=None):
        self.name = name
        self.destinations = []
        self.last_pulses = {}

    def send(self, source, pulse: bool):
        self.last_pulses[source] = pulse  # update memory

        # if all high send low pulse, otherwise send high pulse
        for d in self.destinations:
            messages.append((self, d, not all(self.last_pulses.values())))


def one(data, pushes):
    thelads = prep_data(data)

    button = Module('button')
    broadcaster = thelads['broadcaster']
    button.destinations.append(broadcaster)

    i = 1
    low = 0
    high = 0
    while i <= pushes:
        messages.append((button, broadcaster, False))
        while len(messages) > 0:
            src, dest, pulse = messages.pop(0)
            if pulse:
                high += 1
            else:
                low += 1
            dest.send(src, pulse)
        i += 1

    return low * high


def two(data, pushes):
    thelads = prep_data(data)
    cycles = []

    button = Module('button')
    broadcaster = thelads['broadcaster']
    button.destinations.append(broadcaster)

    i = 1
    while i <= pushes:
        messages.append((button, broadcaster, False))
        while len(messages) > 0:
            src, dest, pulse = messages.pop(0)
            dest.send(src, pulse)

            if any(thelads['th'] == d for d in dest.destinations) and not pulse:
                if len(cycles) == 0 or not any(i % c == 0 for c in cycles):
                    cycles.append(i)

        i += 1

    return lcm(*cycles)


if __name__ == '__main__':
    data = get_data(True)

    print(one(data, 1000))
    print(two(data, 10000))
