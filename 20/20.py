from math import inf

with open("input.txt") as f:
    data = f.read().splitlines()

    iea = data[0]
    print(iea)
    image = set()

    for row, line in enumerate(data[2:]):
        for col, char in enumerate(line):
            if char == "#":
                image.add((row, col))


def get_corners():
    topleft_row, topleft_col = inf, inf
    bottomright_row, bottomright_col = -inf, -inf

    for (row, col) in image:
        topleft_row = min(topleft_row, row)
        topleft_col = min(topleft_col, col)
        bottomright_row = max(bottomright_row, row)
        bottomright_col = max(bottomright_col, col)

    return topleft_row, topleft_col, bottomright_row, bottomright_col


def count_lit_pixels():
    topleft_row, topleft_col, bottomright_row, bottomright_col = get_corners()

    num_lit = 0
    for row in range(topleft_row, bottomright_row + 1):
        for col in range(topleft_col, bottomright_col + 1):
            num_lit += 1 if (row, col) in image else 0
    return num_lit


def calc_index(row, col):
    ord = 8
    binary_number = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            pixel = 1 if (row + dr, col + dc) in image else 0
            binary_number += 2 ** ord * pixel
            ord -= 1

    return binary_number


def apply_iea(margin):
    topleft_row, topleft_col, bottomright_row, bottomright_col = get_corners()
    new_image = set()
    for row in range(topleft_row - margin, bottomright_row + margin + 1):
        for col in range(topleft_col - margin, bottomright_col + margin + 1):
            index = calc_index(row, col)
            if iea[index] == "#":
                new_image.add((row, col))

    return new_image


def delete_unrelevant(margin):
    topleft_row, topleft_col, bottomright_row, bottomright_col = get_corners()

    for col in range(topleft_col, bottomright_col + 1):
        # remove top
        for row in range(topleft_row, topleft_row + margin + 1):
            image.discard((row, col))

        # remove bottom
        for row in range(bottomright_row - margin, bottomright_row + 1):
            image.discard((row, col))

    for row in range(topleft_row, bottomright_row + 1):
        # remove left
        for col in range(topleft_col, topleft_col + margin + 1):
            image.discard((row, col))

        # remove right
        for col in range(bottomright_col - margin, bottomright_col + 1):
            image.discard((row, col))


margin = 3
for num in range(50):
    image = apply_iea(margin)
    if num % 2 == 1:
        delete_unrelevant(margin)
    num_lit = count_lit_pixels()
    if num == 1:
        print(f"Answer to first part: {num_lit}")

print(f"Answer to second part: {num_lit}")
