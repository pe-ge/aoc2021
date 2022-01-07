data = list(map(lambda x: list(map(int, x)), open("input.txt").read().splitlines()))


for row in data:
    row_extension = []
    for n in range(1, 5):
        for risk_level in row:
            row_extension.append((risk_level + n - 1) % 9 + 1)

    row.extend(row_extension)

data_extension = []
for n in range(1, 5):
    for row in data:
        row_extension = []
        for risk_level in row:
            row_extension.append((risk_level + n - 1) % 9 + 1)

        data_extension.append(row_extension)

data.extend(data_extension)

prev_nodes = {}
visited = set()
to_visit = [(0, 0, data[0][0])]
while to_visit:
    r, c, total_risk = to_visit.pop(0)
    visited.add((r, c))

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r = r + dr
        new_c = c + dc
        if not (0 <= new_r < len(data) and 0 <= new_c < len(data[new_r])):
            continue
        if (new_r, new_c) not in visited:
            if (new_r, new_c) == (len(data) - 1, len(data[-1]) - 1):
                print(total_risk + data[new_r][new_c] - data[0][0])
            for rr, cc, _ in to_visit:
                if (new_r, new_c) == (rr, cc):
                    break
            else:
                to_visit.append((new_r, new_c, total_risk + data[new_r][new_c]))
            prev_nodes[(new_r, new_c)] = r, c

    to_visit.sort(key=lambda x: x[2])
