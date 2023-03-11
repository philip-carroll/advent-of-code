from pprint import pprint


def one():
    sizes = {}
    res = 0
    location = '.'

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()

            if line.startswith('$ cd /'):
                location = '.'
                print(location)
            elif line.startswith('$ cd ..'):
                location = location.split('/')
                location.pop()
                location = '/'.join(location)
                print(location)
            elif line.startswith('$ cd '):
                location += '/' + line.removeprefix('$ cd ')
                print(location)
            elif line.startswith('dir '):
                folder = location + '/' + line.removeprefix('dir ')
                if folder not in sizes.keys():
                    sizes[folder] = 0
            elif line.split(' ')[0].isnumeric():
                if location in sizes.keys():
                    sizes[location] += int(line.split(' ')[0])
                else:
                    sizes[location] = int(line.split(' ')[0])

    pprint(sizes)

    sizes2 = sizes.copy()

    for k, v in sizes.items():
        for k2, v2 in sizes.items():
            if k != k2 and k.startswith(k2 + '/'):  # it's a subfolder
                sizes2[k2] += sizes[k]

    pprint(sizes2)

    for k, v in sizes2.items():
        if v <= 100000:
            res += v

    return res


def two():
    sizes = {}
    res = 0
    location = '.'

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()

            if line.startswith('$ cd /'):
                location = '.'
                print(location)
            elif line.startswith('$ cd ..'):
                location = location.split('/')
                location.pop()
                location = '/'.join(location)
                print(location)
            elif line.startswith('$ cd '):
                location += '/' + line.removeprefix('$ cd ')
                print(location)
            elif line.startswith('dir '):
                folder = location + '/' + line.removeprefix('dir ')
                if folder not in sizes.keys():
                    sizes[folder] = 0
            elif line.split(' ')[0].isnumeric():
                if location in sizes.keys():
                    sizes[location] += int(line.split(' ')[0])
                else:
                    sizes[location] = int(line.split(' ')[0])

    pprint(sizes)

    sizes2 = sizes.copy()

    for k, v in sizes.items():
        for k2, v2 in sizes.items():
            if k != k2 and k.startswith(k2 + '/'):  # it's a subfolder
                sizes2[k2] += sizes[k]

    total = sizes2['.']
    needed = (total + 30000000) - 70000000

    min = 30000000
    for k, v in sizes2.items():
        if v >= needed and v < min:
            min = v

    return min


if __name__ == '__main__':
    # print(one())
    print(two())
