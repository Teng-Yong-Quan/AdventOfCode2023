input_data = open('/home/advent-of-code-2023/Day01/advent_of_code_1.txt','r')

word_digit_dict = {"one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6',
			"seven" : '7', "eight" : '8', "nine" : '9'}
total = 0
for line in input_data:
	line = line.strip()
	start_digit = ""
	end_digit = ""
	word_digit = ""
	for alphanumeric in line:
		if alphanumeric.isdigit():
			if start_digit == "":
				start_digit = alphanumeric
			end_digit = alphanumeric
			word_digit = ""
		else:
			word_digit += alphanumeric
		for word, digit in word_digit_dict.items():
			if word in word_digit:
				if start_digit == "":
					start_digit = digit
				end_digit = digit
				word_digit = word[1:]
	total += int(
		(start_digit if start_digit != "" else "0") +
		(end_digit if end_digit != "" else "0"))
print(total)
input_data.close()