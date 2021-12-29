result = 0
for line in open("input.txt").read().split("\n")[:-1]:
    _, numbers = line.split(" | ")
    for number in numbers.split(" "):
        if len(number) in [2, 3, 4, 7]:
            result += 1

print(result)
