width, height = 0, 0
points = set()
folds = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if line == "\n":
            break

        x, y = map(int, line.replace("\n", "").split(","))
        points.add((x, y))
        width = max(x, width)
        height = max(y, height)

    while True:
        line = f.readline()
        if line == "":
            break

        axis, distance = line[len("fold along ") :].replace("\n", "").split("=")
        folds.append((axis, int(distance)))


def do_fold(points, axis, distance):
    global width, height
    folded_points = set()
    for x, y in points:
        if axis == "y":
            folded_points.add((x, 2 * distance - y) if y > distance else (x, y))
        else:
            folded_points.add((2 * distance - x, y) if x > distance else (x, y))

    if axis == "y":
        height = height // 2
    else:
        width = width // 2

    return folded_points


def print_points(points):
    for y in range(height + 1):
        for x in range(width + 1):
            print("#" if (x, y) in points else ".", end="")
        print()
    print()


points = do_fold(points, folds[0][0], folds[0][1])
print(len(points))

for fold in folds[1:]:
    points = do_fold(points, fold[0], fold[1])
print_points(points)
