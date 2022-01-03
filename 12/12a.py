from collections import defaultdict


edges = defaultdict(list)
for line in open("input.txt").read().split("\n")[:-1]:
    a, b = line.split("-")
    edges[a].append(b)
    edges[b].append(a)


def backtrack(edges, node, visited):
    if node == "end":
        return 1

    num_paths = 0
    for neighbour in edges[node]:
        if neighbour == "start" or neighbour in visited:
            continue

        if neighbour.islower():
            visited.add(neighbour)
        num_paths += backtrack(edges, neighbour, visited)
        if neighbour.islower():
            visited.remove(neighbour)

    return num_paths


print(backtrack(edges, "start", set()))
