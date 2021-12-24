from collections import defaultdict
from pprint import pprint

data = open("input.txt").read().split("\n")[:-1]
points = defaultdict(int)
for line in data:
    x1, y1, x2, y2 = map(int, line.replace(" -> ", ",").split(","))
    if not ((x1 == x2) or (y1 == y2)):
        continue
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            points[(x, y)] += 1


pprint(sum(map(lambda x: x > 1, points.values())))
