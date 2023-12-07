import re

file = "/Users/olivernormand/Documents/GitHub/advent_of_code/inputs/1.txt"
pattern = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

word_to_digit = {
        'one': 1, 
        'two': 2, 
        'three': 3, 
        'four': 4,
        'five': 5, 
        'six': 6, 
        'seven': 7, 
        'eight': 8, 
        'nine': 9
    }

with open(file, "r") as f:
    lines = f.readlines()


def line_to_calibration(line):
    matches = re.findall(pattern, line)

    numbers = []
    for x in matches:
        if x.isdigit():
            numbers.append(int(x))
        else:
            numbers.append(word_to_digit[x.lower()])

    return numbers[0] * 10 + numbers[-1]

total = 0
for line in lines:

    total += line_to_calibration(line)

print(total)