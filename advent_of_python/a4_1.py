from utils import get_path, load_data

def parse_line(line):
    dont_care, do_care = line.split(":")
    winning_numbers, numbers = do_care.split("|")
    winning_numbers = [int(x.strip()) for x in winning_numbers.split()]
    numbers = [int(x.strip()) for x in numbers.split()]

    return winning_numbers, numbers

def parse_lines(data):
    data = data.split("\n")
    res = [parse_line(line) for line in data]
    return res

def calculate_line_points(winning_numbers, numbers):
    n = 0
    for number in numbers:
        if number in winning_numbers:
            n += 1

    if n == 0:
        return 0
    else:
        return 2 ** (n-1)

def calculate_total_points(data):

    res = parse_lines(data)

    total = 0

    for line in res:
        wn, n = line
        total += calculate_line_points(wn, n)

    return total

if __name__ == "__main__":
    path = get_path(4, False)
    data = load_data(path)

    print(calculate_total_points(data))
