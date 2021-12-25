from copy import deepcopy

ocean = list(map(list, open("input.txt").read().split("\n")[:-1]))
num_rows = len(ocean)
num_cols = len(ocean[0])


def move_east_facing(ocean):
    new_ocean = deepcopy(ocean)
    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if (
                ocean[row_idx][col_idx] == ">"
                and ocean[row_idx][(col_idx + 1) % num_cols] == "."
            ):
                new_ocean[row_idx][col_idx] = "."
                new_ocean[row_idx][(col_idx + 1) % num_cols] = ">"
    return new_ocean


def move_south_facing(ocean):
    new_ocean = deepcopy(ocean)
    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if (
                ocean[row_idx][col_idx] == "v"
                and ocean[(row_idx + 1) % num_rows][col_idx] == "."
            ):
                new_ocean[row_idx][col_idx] = "."
                new_ocean[(row_idx + 1) % num_rows][col_idx] = "v"
    return new_ocean


step = 1
while True:
    new_ocean = move_south_facing(move_east_facing(ocean))
    if ocean == new_ocean:
        break
    step += 1
    ocean = new_ocean


print(step)
