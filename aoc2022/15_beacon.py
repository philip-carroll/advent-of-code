import ast
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import geopandas as gpd
from matplotlib.collections import PatchCollection
from shapely.geometry import Polygon as SPolygon


def prepare():
    sensors, beacons, links = [], [], []

    with open(__file__.replace('.py', '.txt')) as f:
        for line in f.readlines():
            line = line.rstrip()
            line = line.replace('Sensor at ', '').replace(' closest beacon is at ', '')
            line = line.replace('x=', '').replace('y=', '')
            line = line.split(':')
            line = [l.split(',') for l in line]

            sensor = ast.literal_eval(line[0][0]), ast.literal_eval(line[0][1])
            beacon = ast.literal_eval(line[1][0]), ast.literal_eval(line[1][1])

            sensors.append(sensor)
            beacons.append(beacon)
            links.append((sensor, beacon))

    return sensors, beacons, links


def mdist(s, b):
    return abs((s[0] - b[0])) + abs((s[1] - b[1]))


def polys(links):
    res = []

    for s, b in links:
        dist = mdist(s, b)
        print('%s : %s -> %s' % (s, b, dist))
        ply = [(s[0], s[1] - dist),  # top
               (s[0] + dist, s[1]),  # right
               (s[0], s[1] + dist),  # bottom
               (s[0] - dist, s[1])]  # left

        res.append(ply)

    return res


if __name__ == '__main__':
    s, b, l = prepare()
    polys = polys(l)
    row = 4000000

    leftest, rightest = 0, 0
    patches, spatches = [], []
    for pl in polys:
        if pl[0][1] <= row <= pl[2][1]:
            if pl[1][0] > rightest:
                rightest = pl[1][0]
            if pl[3][0] < leftest:
                leftest = pl[3][0]
        spatches.append(SPolygon(pl))
        patches.append(Polygon(pl, closed=True))
    # p = PatchCollection(patches, alpha=0.4)
    # ax.add_collection(p)

    grid = SPolygon([(0, 0), (row, 0), (row, row), (0, row)])
    for sp in spatches:
        grid = grid.difference(sp)
        myPoly = gpd.GeoSeries(grid)
    myPoly.plot()
    # plt.plot([x[0] for x in s], [x[1] for x in s], 'bo')
    # plt.plot([x[0] for x in b], [x[1] for x in b], 'r+')
    # plt.plot([leftest, rightest], [row, row], 'g.')
    ax = plt.gca()
    ax.invert_yaxis()
    ax.ticklabel_format(style='plain')
    plt.show()

    # s = set(s)
    # b = set(b)
    # res = 0
    # for i in range(leftest, rightest):
    #     point = (i, row)
    #     print(point)
    #     for pt in patches:
    #         if pt.contains_point(point) and point not in s and point not in b:
    #             res += 1
    #             break
    # print(res)
