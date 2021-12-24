from collections import defaultdict
from pprint import pprint


def get_diff(a1, a2):
    if a1 < a2:
        diff = 1
    elif a1 > a2:
        diff = -1
    else:
        diff = 0
    return diff


data = open("input.txt").read().split("\n")[:-1]
points = defaultdict(int)
for line in data:
    x1, y1, x2, y2 = map(int, line.replace(" -> ", ",").split(","))

    dx = get_diff(x1, x2)
    dy = get_diff(y1, y2)

    x = x1
    y = y1
    while True:
        points[(x, y)] += 1
        x += dx
        y += dy
        if x == x2 and y == y2:
            points[(x, y)] += 1
            break

pprint(sum(map(lambda x: x > 1, points.values())))
