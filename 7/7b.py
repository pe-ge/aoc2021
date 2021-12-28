import numpy as np

positions = np.array(list(map(int, open("input.txt").read().split("\n")[0].split(","))))
median = int(np.median(positions))


def calc_alignment(positions, align_pos):
    return sum([sum(range(abs(pos - align_pos) + 1)) for pos in positions])


best = calc_alignment(positions, median)
while True:
    median += 1
    result = calc_alignment(positions, median)
    if result > best:
        break
    best = result

print(best)
