cmds = open("input.txt").read()[:-1].split("\n")
hor = 0
depth = 0
for cmd in cmds:
    direction, units = cmd.split(" ")
    if direction == "forward":
        hor += int(units)
    elif direction == "down":
        depth += int(units)
    else:
        depth -= int(units)
print(hor * depth)
