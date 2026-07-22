input_data = open("/home/advent-of-code-2023/Day05/advent_of_code_5.txt", "r")
input_data_lst = [y for y in [x.replace("\n","") for x in input_data] if y]
seeds = [int(y) for x in [x for x in input_data_lst if "seeds: " in x] for y in x.replace("seeds: ", "").split()]
keywords_dict = {kw.replace(":",""): [] for kw in input_data_lst if "map" in kw}
kw_index = -1
keywords = list(keywords_dict.keys())
for line in input_data_lst[1:]:
	if "map" not in line:
		tup = tuple(int(z) for z in line.split())
		keywords_dict[keywords[kw_index]].append(tup)
	else:
		kw_index += 1
lowest_loc = -1
for seed in seeds:
	current_seed = seed
	for k,v in keywords_dict.items():
		for dest, source, length in v:
			if source <= current_seed <= source + length:
				current_seed = dest + (current_seed - source)
				break
	if lowest_loc == -1:
		lowest_loc = current_seed
	else:
		if current_seed < lowest_loc:
			lowest_loc = current_seed
print(lowest_loc)
input_data.close()
