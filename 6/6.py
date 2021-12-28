data = list(map(int, open("input.txt").read().replace("\n", "").split(",")))


def grow(current_day, lanternfish_state, table, num_days):
    if (current_day, lanternfish_state) in table:
        return table[(current_day, lanternfish_state)]

    if current_day == num_days:
        return 1

    new_lanternfish_state = lanternfish_state - 1
    if new_lanternfish_state >= 0:
        result = grow(current_day + 1, new_lanternfish_state, table, num_days)
        table[(current_day, lanternfish_state)] = result
        return result
    else:
        result = grow(current_day + 1, 6, table, num_days) + grow(current_day + 1, 8, table, num_days)
        table[(current_day, lanternfish_state)] = result
        return result


def part1():
    return sum([grow(0, d, {}, 80) for d in data])

def part2():
    return sum([grow(0, d, {}, 256) for d in data])


print(part1())
print(part2())
