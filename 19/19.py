beacons = []
scanners = {0: (0, 0, 0)}
with open("input.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        if line.startswith("--- scanner"):
            beacons.append(set())
        elif line != "":
            beacons[-1].add(tuple(map(int, line.split(","))))


def rotate_one_axis(x, y, z):
    return [(x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y)]


def rotate_all_axes(x, y, z):
    return (
        rotate_one_axis(x, y, z)
        + rotate_one_axis(-z, y, x)
        + rotate_one_axis(-x, y, -z)
        + rotate_one_axis(z, y, -x)
        + rotate_one_axis(y, -x, z)
        + rotate_one_axis(-y, x, z)
    )


def get_all_rotations(beacons):
    all_rotations = []
    for beacon in beacons:
        for rotation_idx, rotation in enumerate(rotate_all_axes(*beacon)):
            if rotation_idx == len(all_rotations):
                all_rotations.append([])
            all_rotations[rotation_idx].append(rotation)

    return all_rotations


def find_overlap_and_merge(beacons_2, scanner_idx):
    beacons_1 = beacons[0]
    beacons_2_rotations = get_all_rotations(beacons_2)
    max_count = 0
    for rotation_idx, beacons_2_rotation in enumerate(beacons_2_rotations):
        for fixed_beacon_2 in beacons_2_rotation:
            for fixed_beacon_1 in beacons_1:
                diff_x = fixed_beacon_1[0] - fixed_beacon_2[0]
                diff_y = fixed_beacon_1[1] - fixed_beacon_2[1]
                diff_z = fixed_beacon_1[2] - fixed_beacon_2[2]

                count = 0
                for beacon_2 in beacons_2_rotation:
                    beacon_2_translated = (
                        beacon_2[0] + diff_x,
                        beacon_2[1] + diff_y,
                        beacon_2[2] + diff_z,
                    )
                    if beacon_2_translated in beacons_1:
                        count += 1

                max_count = max(count, max_count)
                if count >= 12:
                    print("Overlap found. Merging beacons with scanner 0")
                    for beacon_2 in beacons_2_rotation:
                        beacon_2_translated = (
                            beacon_2[0] + diff_x,
                            beacon_2[1] + diff_y,
                            beacon_2[2] + diff_z,
                        )
                        beacons_1.add(beacon_2_translated)

                    scanners[scanner_idx] = (diff_x, diff_y, diff_z)
                    return True

    return False


visited = set()
while True:
    if len(visited) != len(beacons) - 1:
        for i in range(1, len(beacons)):
            if i not in visited:
                print(f"Finding overlap between scanner 0 and {i}")
                if find_overlap_and_merge(beacons[i], i):
                    visited.add(i)
    else:
        break

max_distance = 0
for _, beacon_1 in scanners.items():
    for _, beacon_2 in scanners.items():
        distance = (
            abs(beacon_1[0] - beacon_2[0])
            + abs(beacon_1[1] - beacon_2[1])
            + abs(beacon_1[2] - beacon_2[2])
        )
        max_distance = max(max_distance, distance)

print(f"Total number of all beacons: {len(beacons[0])}")
print(f"Distance between most distant scanners: {max_distance}")
