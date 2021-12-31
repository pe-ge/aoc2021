lines = open("input.txt").read().split("\n")[:-1]

pairs = {">": "<", ")": "(", "}": "{", "]": "["}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def check_line(line):
    stack = list()
    for char in line:
        if char in ")]}>":
            left_bracket = stack.pop()
            if left_bracket != pairs[char]:
                return points[char]
        else:
            stack.append(char)
    return 0


result = 0
for line in lines:
    result += check_line(line)

print(result)
