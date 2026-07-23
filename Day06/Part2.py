input_data = open("/home/advent-of-code-2023/Day06/advent_of_code_6.txt", "r")
input_data_lst = [x for x in input_data]
time = int(input_data_lst[0].replace("Time:", "").replace(" ",""))
distance = int(input_data_lst[1].replace("Distance:", "").replace(" ",""))

solution = 0
for j in range(1, time):
	leftover_time = time - j
	if leftover_time * j > distance:
		solution += 1
print(solution)
input_data.close()