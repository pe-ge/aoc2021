from collections import defaultdict
from math import inf


def solve(num_steps):
    rules = {}
    pair_counts = defaultdict(int)
    with open("input.txt") as f:
        template = f.readline()[:-1]
        prev_char = template[0]
        for char in template[1:]:
            pair_counts[prev_char + char] += 1
            prev_char = char
        f.readline()
        while True:
            line = f.readline()
            if line == "":
                break

            pair, insert = line[:-1].split(" -> ")
            rules[pair] = pair[0] + insert, insert + pair[1]

    def apply_rules(rules, pair_counts):
        new_pair_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            new_pair_counts[rules[pair][0]] += count
            new_pair_counts[rules[pair][1]] += count

        return new_pair_counts

    for _ in range(num_steps):
        pair_counts = apply_rules(rules, pair_counts)

    all_chars = set()
    for pair in rules.keys():
        all_chars.add(pair[0])
        all_chars.add(pair[1])

    char_counts = defaultdict(int)
    for char in all_chars:
        for pair, count in pair_counts.items():
            if char in pair:
                char_counts[char] += count

                if char + char == pair:
                    char_counts[char] += count

        if template[0] == char or template[-1] == char:
            char_counts[char] -= 1

        char_counts[char] = char_counts[char] // 2
        if template[0] == char or template[-1] == char:
            char_counts[char] += 1

    min_count = inf
    max_count = 0
    for count in char_counts.values():
        min_count = min(min_count, count)
        max_count = max(max_count, count)
    print(max_count - min_count)


solve(10)
solve(40)
