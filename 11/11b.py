from copy import copy

data = list(map(lambda x: list(map(int, x)), open("input.txt").read().split("\n")[:-1]))


def one_step(data):
    new_data = copy(data)
    for row_idx, row in enumerate(data):
        for col_idx, energy in enumerate(row):
            new_data[row_idx][col_idx] = energy + 1

    already_flashed = set()
    num_flashes = 0
    while True:
        flashed, new_flashes = flash(new_data, already_flashed)
        num_flashes += new_flashes
        if not flashed:
            break

    for row_idx, row in enumerate(data):
        for col_idx, energy in enumerate(row):
            if new_data[row_idx][col_idx] > 9:
                new_data[row_idx][col_idx] = 0

    return new_data, num_flashes


def inc_energy(data, row_idx, col_idx):
    if 0 <= row_idx < len(data) and 0 <= col_idx < len(data[row_idx]):
        data[row_idx][col_idx] = data[row_idx][col_idx] + 1
        return True
    return False


def flash(data, flashed):
    changed = False
    num_flashes = 0
    for row_idx, row in enumerate(data):
        for col_idx, energy in enumerate(row):
            if energy > 9 and (row_idx, col_idx) not in flashed:
                num_flashes += 1
                flashed.add((row_idx, col_idx))
                for dr, dc in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]:
                    if inc_energy(data, row_idx + dr, col_idx + dc):
                        changed = True

    return changed, num_flashes


def synchronized(data):
    for row_idx, row in enumerate(data):
        for col_idx, energy in enumerate(row):
            if energy != 0:
                return False
    return True


num_flashes = 0
step = 0
while not synchronized(data):
    step += 1
    data, new_flashes = one_step(data)
    num_flashes += new_flashes


print(step)
