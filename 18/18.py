from math import floor, ceil

BRACKET_LEFT = -1
BRACKET_RIGHT = -2
COMMA = -3


def explode(number, idx):
    digit_left = number[idx]
    digit_right = number[idx + 2]

    for idx_left in range(idx - 1, -1, -1):
        if number[idx_left] >= 0:
            number[idx_left] += digit_left
            break
    for idx_right in range(idx + 3, len(number)):
        if number[idx_right] >= 0:
            number[idx_right] += digit_right
            break

    number = number[: idx - 1] + [0] + number[idx + 4 :]

    return number


def split(number, idx):
    digit_left = floor(number[idx] / 2)
    digit_right = ceil(number[idx] / 2)

    number = (
        number[:idx]
        + [BRACKET_LEFT, digit_left, COMMA, digit_right, BRACKET_RIGHT]
        + number[idx + 1 :]
    )
    return number


def reduce(number):
    brackets = 0
    for idx, char in enumerate(number):
        if char == BRACKET_LEFT:
            brackets += 1
        elif char == BRACKET_RIGHT:
            brackets -= 1

        if char >= 0 and brackets > 4:
            return explode(number, idx), False

    for idx, char in enumerate(number):
        if char > 9:
            return split(number, idx), False

    return number, True


def reduce_to_final_number(number):
    while True:
        number, final = reduce(number)
        if final:
            return number


def process(number):
    result = []
    for char in number:
        if char == "[":
            result.append(BRACKET_LEFT)
        elif char == "]":
            result.append(BRACKET_RIGHT)
        elif char == ",":
            result.append(COMMA)
        else:
            result.append(int(char))

    return result


def add(number_1, number_2):
    return [BRACKET_LEFT, *number_1, COMMA, *number_2, BRACKET_RIGHT]


def magnitude(number):
    while True:
        if len(number) == 1:
            return number[0]

        for idx in range(len(number)):
            if number[idx] >= 0 and number[idx + 1] == COMMA and number[idx + 2] >= 0:
                result = 3 * number[idx] + 2 * number[idx + 2]
                number = number[: idx - 1] + [result] + number[idx + 4 :]
                break


numbers = open("input.txt").read().splitlines()
final_sum = process(numbers[0])
for number_2 in numbers[1:]:
    final_sum = reduce_to_final_number(add(final_sum, process(number_2)))

print(magnitude(final_sum))

largest_magnitude = 0
for number_1 in numbers:
    for number_2 in numbers:
        largest_magnitude = max(
            largest_magnitude,
            magnitude(
                reduce_to_final_number(add(process(number_1), process(number_2)))
            ),
        )

print(largest_magnitude)
