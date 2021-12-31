lines = open("input.txt").read().split("\n")[:-1]

pairs = {">": "<", ")": "(", "}": "{", "]": "["}
rev_pairs = {"<": ">", "(": ")", "{": "}", "[": "]"}
points = {")": 1, "]": 2, "}": 3, ">": 4}


def is_corrupted(line):
    stack = list()
    for char in line:
        if char in ")]}>":
            left_bracket = stack.pop()
            if left_bracket != pairs[char]:
                return True
        else:
            stack.append(char)
    return False


def complete_line(line):
    stack = list()
    for char in line:
        if char in ")]}>":
            stack.pop()
        else:
            stack.append(char)

    return "".join((map(lambda x: rev_pairs[x], reversed(stack))))


def score_completion(completion):
    score = 0
    for char in completion:
        score = score * 5 + points[char]

    return score


scores = []
for line in lines:
    if not is_corrupted(line):
        comletion = complete_line(line)
        scores.append(score_completion(comletion))

print(list(sorted(scores))[len(scores) // 2])
