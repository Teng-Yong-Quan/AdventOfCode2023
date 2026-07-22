input_data = open("/home/advent-of-code-2023/Day05/advent_of_code_5.txt", "r")
input_data_lst = [y for y in [x.replace("\n","") for x in input_data] if y]
seed_ranges = [int(y) for x in [x for x in input_data_lst if "seeds: " in x] for y in x.replace("seeds: ", "").split()]
seeds = seed_ranges[::2]
ranges = seed_ranges[1::2]
keywords_dict = {kw.replace(":",""): [] for kw in input_data_lst if "map" in kw}
kw_index = -1
keywords = list(keywords_dict.keys())
for line in input_data_lst[1:]:
	if "map" not in line:
		tup = tuple(int(z) for z in line.split())
		keywords_dict[keywords[kw_index]].append(tup)
	else:
		kw_index += 1

queue = [[x,y] for x, y in zip(seeds, [x+y-1 for x,y in zip(seeds,ranges)])]
for k,v in keywords_dict.items():
	finished = []
	unfinished = []
	while queue:
		unfinished.append(queue.pop(0))
		while unfinished:
			current_ele = unfinished.pop(0)
			lower_seed, upper_seed = current_ele[0], current_ele[1]
			isFound = False
			for dest, source, length in v:
				if upper_seed < source or lower_seed >= source + length:
					continue
				lower_bound = max(lower_seed, source)
				upper_bound = min(upper_seed, source + length - 1)
				if lower_seed < source:
					unfinished.append([lower_seed, source - 1])
				if upper_seed > source + length - 1:
					unfinished.append([source + length, upper_seed])
				if lower_bound <= upper_bound:
					finished.append([dest + (lower_bound - source), dest + (upper_bound - source)])
					isFound = True
				if isFound:
					break
			if not isFound:
				finished.append(current_ele)
	queue = finished
ans = min([x[0] for x in queue])
print(ans)
input_data.close()