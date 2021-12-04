bin_nums = open("input.txt").read().split()

gamma_rate = ""
for col in range(len(bin_nums[0])):
    ones = 0
    zeros = 0
    for row in range(len(bin_nums)):
        ones += 1 if bin_nums[row][col] == "1" else 0
        zeros += 1 if bin_nums[row][col] == "0" else 0


    gamma_rate += "1" if ones > zeros else "0"

epsilon_rate = "".join(list(map(lambda x: str(1 - int(x)), gamma_rate)))
print(int(epsilon_rate, 2) * int(gamma_rate, 2))




