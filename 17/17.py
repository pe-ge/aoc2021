inp = "target area: x=195..238, y=-93..-67"

min_x, max_x, min_y, max_y = map(
    int,
    inp[inp.find("x") :]
    .replace("x=", "")
    .replace(", y=", ",")
    .replace("..", ",")
    .split(","),
)


def one_step(pos_x, pos_y, vel_x, vel_y):
    pos_x += vel_x
    pos_y += vel_y

    if vel_x > 0:
        vel_x -= 1
    elif vel_x < 0:
        vel_x += 1

    vel_y -= 1

    return pos_x, pos_y, vel_x, vel_y


def get_highest_y(vel_x, vel_y):
    pos_x, pos_y = 0, 0
    highest_y = 0
    while True:
        if pos_y < min_y:
            return 0, 0

        if pos_x > max_x:
            return 0, 0

        if min_x <= pos_x <= max_x and min_y <= pos_y <= max_y:
            return highest_y, 1

        pos_x, pos_y, vel_x, vel_y = one_step(pos_x, pos_y, vel_x, vel_y)
        highest_y = max(highest_y, pos_y)


count = 0
highest_y = 0
for vel_x in range(1, 300):
    for vel_y in range(-100, 1000):
        y, c = get_highest_y(vel_x, vel_y)
        highest_y = max(highest_y, y)
        count += c

print(highest_y, count)
