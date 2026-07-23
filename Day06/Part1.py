input_data = open("/home/advent-of-code-2023/Day06/advent_of_code_6.txt", "r")
input_data_lst = [x for x in input_data]
times = [int(x) for x in input_data_lst[0].replace("Time:", "").split() if x]
distances = [int(x) for x in input_data_lst[1].replace("Distance:", "").split() if x]
ans = 1
for i in range(len(times)):
	current_dist = distances[i]
	current_time = times[i]
	solution = 0
	for j in range(1, current_time):
		leftover_time = current_time - j
		if leftover_time * j > current_dist:
			solution += 1
	ans *= solution
print(ans)
input_data.close()