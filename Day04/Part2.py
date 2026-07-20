input_data = open("/home/advent-of-code-2023/Day04/advent_of_code_4.txt", "r")

card_winning_numbers_dict = {}
card_count_dict = {}

total = 0
total_card_index = 0
current_card_index = 1

for line in input_data:
	line = line.strip()

	full_list = line.split(":")
	main_list = full_list[1].split("|")

	winning_numbers_list = main_list[0].split()
	own_numbers_list = main_list[1].split()

	number_of_winning_numbers = 0

	for own_number in own_numbers_list:
		if own_number in winning_numbers_list:
			number_of_winning_numbers += 1

	total_card_index += 1
	card_winning_numbers_dict[total_card_index] = number_of_winning_numbers
	card_count_dict[total_card_index] = 1

while current_card_index < total_card_index:
	current_range = card_winning_numbers_dict[current_card_index]
	end = current_card_index + current_range
	current_card_count = card_count_dict[current_card_index]

	for _ in range(current_card_count):
		for start in range(current_card_index + 1, end + 1):
			if start <= total_card_index:
				card_count_dict[start] += 1

	current_card_index += 1

for count in card_count_dict.values():
	total += count

print(total)
input_data.close()