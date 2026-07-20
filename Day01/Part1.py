input_data = open('/home/advent-of-code-2023/Day01/advent_of_code_1.txt','r')
total = 0
for line in input_data:
    digits = [c for c in line if c.isdigit()]
    if digits:
        total += int(digits[0] + digits[-1])
    else:
        total += 0
print(total)
input_data.close()