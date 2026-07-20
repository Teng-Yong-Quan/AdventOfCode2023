input_data = open('/home/advent-of-code-2023/Day02/advent_of_code_2.txt','r')
total = 0
for line in input_data:
	colour_limit_dict = {"red": 0,"green": 0,"blue": 0}
	line = line.strip()
	game_total = 1
	full_string_list = line.split(":")
	cubes_string_list = full_string_list[1].split(";")
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
						colour_limit_dict[colour] = int(cube_number)
	for colour, limit in colour_limit_dict.items():
		game_total *= limit
	total += game_total
print(total)
input_data.close()