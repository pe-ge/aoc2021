bin_nums = open("input.txt").read().split()

gamma_rate = ""
oxygen_generator_rating = bin_nums[:]
for col in range(len(oxygen_generator_rating[0])):
    if len(oxygen_generator_rating) == 1:
        break
    ones = 0
    zeros = 0
    for row in range(len(oxygen_generator_rating)):
        ones += 1 if oxygen_generator_rating[row][col] == "1" else 0
        zeros += 1 if oxygen_generator_rating[row][col] == "0" else 0


    bit_criteria = "1" if ones >= zeros else "0"

    new_oxygen_generator_rating = []
    for num in oxygen_generator_rating:
        if num[col] == bit_criteria:
           new_oxygen_generator_rating.append(num)

    oxygen_generator_rating = new_oxygen_generator_rating

CO2_scrubber_rating = bin_nums[:]
for col in range(len(CO2_scrubber_rating[0])):
    if len(CO2_scrubber_rating) == 1:
        break
    ones = 0
    zeros = 0
    for row in range(len(CO2_scrubber_rating)):
        ones += 1 if CO2_scrubber_rating[row][col] == "1" else 0
        zeros += 1 if CO2_scrubber_rating[row][col] == "0" else 0


    bit_criteria = "0" if zeros <= ones else "1"

    new_CO2_scrubber_rating = []
    for num in CO2_scrubber_rating:
        if num[col] == bit_criteria:
            new_CO2_scrubber_rating.append(num)

    CO2_scrubber_rating = new_CO2_scrubber_rating

print(int(oxygen_generator_rating[0], 2) * int(CO2_scrubber_rating[0], 2))
