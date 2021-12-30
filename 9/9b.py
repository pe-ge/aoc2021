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


def find_basin(heightmap, low_point_r, low_point_c):
    basin = set()
    to_pop = [(low_point_r, low_point_c)]
    while to_pop:
        r, c = to_pop.pop(0)
        basin.add((r, c))
        for next_r, next_c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                not (next_r, next_c) in basin
                and get_point(heightmap, next_r, next_c) != 9
            ):
                to_pop.append((next_r, next_c))

    return len(basin)


basins = []
for r in range(len(heightmap)):
    for c in range(len(heightmap[r])):
        if is_low_point(heightmap, r, c):
            basins.append(find_basin(heightmap, r, c))

basins = list(sorted(basins, reverse=True))
print(basins[0] * basins[1] * basins[2])
