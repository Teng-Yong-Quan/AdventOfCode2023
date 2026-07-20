def is_gear(ch):
	return ch == "*"

input_data = open('/home/advent-of-code-2023/Day03/advent_of_code_3.txt','r')
full_nested_lists = [line.strip() for line in input_data]
gear_coord_num_dict = {}
total = 0
current_list_index = 0
while current_list_index < len(full_nested_lists):
	current_list = full_nested_lists[current_list_index]
	current_index = 0
	while current_index < len(current_list):
		if not current_list[current_index].isdigit():
			current_index += 1
		else:
			is_gear_check = False
			current_number_string = ""
			start_index = current_index
			end_index = start_index
			while end_index < len(current_list):
				if current_list[end_index].isdigit():
					current_number_string += current_list[end_index]
					end_index += 1
				else:
					break
			current_index = end_index
			lower_row = current_list_index - 1
			upper_row = current_list_index + 1
			lower_bound = start_index - 1
			gear_coord = None
			for current_col in range(lower_bound, end_index + 1):
				if (
					0 <= current_col < len(current_list)
					and 0 <= lower_row < len(full_nested_lists)
				):
					if is_gear(full_nested_lists[lower_row][current_col]):
						is_gear_check = True
						gear_coord = (lower_row, current_col)
						break
				if (
					0 <= current_col < len(current_list)
					and 0 <= upper_row < len(full_nested_lists)
				):
					if is_gear(full_nested_lists[upper_row][current_col]):
						is_gear_check = True
						gear_coord = (upper_row, current_col)
						break
			if not is_gear_check:
				if 0 <= lower_bound < len(current_list):
					is_gear_check = is_gear(current_list[lower_bound])
					if is_gear_check:
						gear_coord = (current_list_index, lower_bound)
			if not is_gear_check:
				if 0 <= end_index < len(current_list):
					is_gear_check = is_gear(current_list[end_index])
					if is_gear_check:
						gear_coord = (current_list_index, end_index)
			if is_gear_check:
				if gear_coord not in gear_coord_num_dict:
					gear_coord_num_dict[gear_coord] = []
				gear_coord_num_dict[gear_coord].append(
					int(current_number_string))
	current_list_index += 1
for gear_coord, numbers in gear_coord_num_dict.items():
	if len(numbers) == 2:
		gear_total = 1
		for number in numbers:
			gear_total *= number
		total += gear_total
print(total)
input_data.close()