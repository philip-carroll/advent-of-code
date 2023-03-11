import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from itertools import product


def plot(cubes, size):
    # prepare some coordinates
    x, y, z = np.indices((size, size, size))
    voxelarray = None

    # and plot everything
    ax = plt.figure().add_subplot(projection='3d')

    # combine the objects into a single boolean array
    for a, b, c in cubes:
        cube = (x == a) & (y == b) & (z == c)
        if voxelarray is None:
            voxelarray = cube
        else:
            voxelarray = voxelarray | cube

    ax.voxels(voxelarray, edgecolor='k')

    plt.show()


def get_cubes():
    cubes = []
    size = 0

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()
            coords = tuple(int(c) for c in line.split(','))
            cubes.append(coords)
            if max(coords) > size:
                size = max(coords)

    return set(cubes), size + 1


def flood(box, x, y, z, old, new):
    def is_valid(point):
        x, y, z = point[0], point[1], point[2]
        # Base cases
        if x < minx or x >= maxx or y < miny or y >= maxy or z < minz or z >= maxz:
            return False

        if box[(x, y, z)] != old or box[(x, y, z)] == new:
            return False

        return True

    # Append the starting position
    queue = [(x, y, z)]

    # Replace the color at (x, y, z)
    box[(x, y, z)] = new

    # While the queue is not empty i.e. the area having old value is not replaced  with new value
    while queue:
        # Dequeue the front node
        x, y, z = queue.pop()

        # Each direction
        above = (x, y + 1, z)
        if is_valid(above):
            box[above] = new
            queue.append(above)

        below = (x, y - 1, z)
        if is_valid(below):
            box[below] = new
            queue.append(below)

        left = (x - 1, y, z)
        if is_valid(left):
            box[left] = new
            queue.append(left)

        right = (x + 1, y, z)
        if is_valid(right):
            box[right] = new
            queue.append(right)

        front = (x, y, z - 1)
        if is_valid(front):
            box[front] = new
            queue.append(front)

        back = (x, y, z + 1)
        if is_valid(back):
            box[back] = new
            queue.append(back)


def flood_recursive(box, x, y, z, old, new):
    # Base cases
    if (x < minx or x >= maxx or y < miny or y >= maxy or z < minz or z >= maxz):
        return

    if (box[(x, y, z)] != old or box[(x, y, z)] == new):
        return

    # Replace the color at (x, y, z)
    box[(x, y, z)] = new

    # Recur for each direction
    above = (x, y + 1, z)
    below = (x, y - 1, z)
    left = (x - 1, y, z)
    right = (x + 1, y, z)
    front = (x, y, z - 1)
    back = (x, y, z + 1)
    for dx, dy, dz in [above, below, left, right, front, back]:
        flood_recursive(box, dx, dy, dz, old, new)


def get_area(cubes):
    area = 0

    for x, y, z in cubes:
        above = (x, y + 1, z)
        below = (x, y - 1, z)
        left = (x - 1, y, z)
        right = (x + 1, y, z)
        front = (x, y, z - 1)
        back = (x, y, z + 1)
        # remove sides with neighbouring cubes from surface area
        area += 6 - len({above, below, left, right, front, back}.intersection(cubes))

    return area


if __name__ == '__main__':
    cubes, size = get_cubes()
    box = defaultdict(int)
    air = []
    area = 0

    minx, maxx = min([x for x, y, z in cubes]), max([x for x, y, z in cubes]) + 1
    miny, maxy = min([y for x, y, z in cubes]), max([y for x, y, z in cubes]) + 1
    minz, maxz = min([z for x, y, z in cubes]), max([z for x, y, z in cubes]) + 1

    lava_area = get_area(cubes)

    xs = [x for x in range(minx, maxx)]
    ys = [y for y in range(miny, maxy)]
    zs = [z for z in range(minz, maxz)]

    for p in product(xs, ys, zs):
        if p in cubes:
            box[p] = 1
        else:
            box[p] = 0

    flood(box, minx, miny, minz, 0, 1)

    for b, v in box.items():
        if v == 0:
            air.append(b)

    air_area = get_area(air)

    print(lava_area)
    print(air_area)
    print(lava_area - air_area)  # remove surface area of air from total surface area

    plot(cubes, size)
    plot(air, size)
