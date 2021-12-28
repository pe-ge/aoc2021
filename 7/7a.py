import numpy as np

positions = np.array(list(map(int, open("input.txt").read().split("\n")[0].split(","))))
median = int(np.median(positions))


def calc_alignment(positions, align_pos):
    return sum([abs(pos - align_pos) for pos in positions])


print(calc_alignment(positions, median))
