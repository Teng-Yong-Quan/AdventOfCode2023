input_data = open("/home/advent-of-code-2023/Day04/advent_of_code_4.txt", "r")

total = 0

for line in input_data:
	line = line.strip()

	full_list = line.split(":")
	main_list = full_list[1].split("|")

	winning_numbers_list = main_list[0].split()
	own_numbers_list = main_list[1].split()

	number_of_winning_numbers = -1

	for own_number in own_numbers_list:
		if own_number in winning_numbers_list:
			number_of_winning_numbers += 1

	if number_of_winning_numbers > -1:
		total += 2 ** number_of_winning_numbers

print(total)

input_data.close()