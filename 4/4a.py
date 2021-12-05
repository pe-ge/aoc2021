with open("input.txt") as f:
    numbers = f.readline().split(",")

    boards = []
    drawn = []
    board_idx = 0
    while True:
        boards.append({})
        drawn.append(set())
        f.readline()

        no_more_input = False
        for row in range(5):
            nums = f.readline().strip().replace("  ", " ").split(" ")
            if nums == [""]:
                no_more_input = True
                break
            for col, num in enumerate(nums):
                boards[board_idx][num] = (row, col)

        if no_more_input:
            boards = boards[:-1]
            break

        board_idx += 1

def find_winning_board_idx(drawn):
    for board_idx in range(len(drawn)):
        for row in range(5):
            for col in range(5):
                if (row, col) not in drawn[board_idx]:
                    break
            else:
                return board_idx

        for col in range(5):
            for row in range(5):
                if (row, col) not in drawn[board_idx]:
                    break
            else:
                return board_idx

    return None

for num in numbers:
    for board_idx in range(len(boards)):
        if num in boards[board_idx]:
            drawn[board_idx].add(boards[board_idx][num])
    winning_board_idx = find_winning_board_idx(drawn)
    if winning_board_idx is not None:
        break

sum_unmarked_nums = 0
for key, (row, col) in boards[winning_board_idx].items():
    if (row, col) not in drawn[winning_board_idx]:
        sum_unmarked_nums += int(key)

print(sum_unmarked_nums * int(num))


