cmds = open("input.txt").read()[:-1].split("\n")
hor = 0
depth = 0
aim = 0
for cmd in cmds:
    direction, units = cmd.split(" ")
    if direction == "forward":
        hor += int(units)
        depth += aim * int(units)
    elif direction == "down":
        aim += int(units)
    else:
        aim -= int(units)
print(hor * depth)
