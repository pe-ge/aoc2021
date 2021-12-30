heightmap = open("input.txt").read().split("\n")[:-1]


def get_point(heightmap, r, c):
    if 0 <= r < len(heightmap) and 0 <= c < len(heightmap[r]):
        return int(heightmap[r][c])
    else:
        return 9


def is_low_point(heightmap, r, c):
    point = get_point(heightmap, r, c)
    return (
        point < get_point(heightmap, r + 1, c)
        and point < get_point(heightmap, r - 1, c)
        and point < get_point(heightmap, r, c + 1)
        and point < get_point(heightmap, r, c - 1)
    )


risk_level = 0
for r in range(len(heightmap)):
    for c in range(len(heightmap[r])):
        if is_low_point(heightmap, r, c):
            risk_level += get_point(heightmap, r, c) + 1
print(risk_level)
