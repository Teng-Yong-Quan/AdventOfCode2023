input_data = open('/home/advent-of-code-2023/Day02/advent_of_code_2.txt','r')
total = 0
colour_limit_dict = {"red": 12,"green": 13,"blue": 14}
for line in input_data:
	line = line.strip()
	is_exceed_limit = False
	full_string_list = line.split(":")
	game_number = full_string_list[0]
	cubes_string_list = full_string_list[1].split(";")
	valid_game_number = ""
	for current_set_string in cubes_string_list:
		current_set_string_list = current_set_string.split(",")
		for current_cube_string in current_set_string_list:
			cube_number = ""
			for colour, limit in colour_limit_dict.items():
				if colour in current_cube_string:
					for alphanumeric in current_cube_string:
						if alphanumeric.isdigit():
							cube_number += alphanumeric
					if int(cube_number) > limit:
						is_exceed_limit = True
						break
			if is_exceed_limit:
				break
		if is_exceed_limit:
			break
	if not is_exceed_limit:
		for alphanumeric in game_number:
			if alphanumeric.isdigit():
				valid_game_number += alphanumeric
		total += int(valid_game_number)
print(total)
input_data.close()