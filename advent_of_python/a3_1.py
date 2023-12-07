import re
from utils import get_path, load_data
import numpy as np

def get_symbols(data):
    chars = set(data)
    not_a_symbol = "0123456789\n."
    
    symbols = []
    for char in chars:
        if char not in not_a_symbol:
            symbols.append(char)

    return symbols

def get_numbers(line):
    pattern = r"\d+"

    matches = re.finditer(pattern, line)

    numbers = []
    indexes = []
    for match in matches:
        numbers.append(int(match.group()))
        indexes.append(match.start())

    return numbers, indexes

def parse_data(data):

    n_rows = len(data.split("\n"))
    n_columns = len(data.split("\n")[0])

    return n_columns, n_rows, data.replace("\n", "")

def get_adjacent_indexes(n_rows, n_columns, index):

    column_number = index % n_columns
    row_number = (index - column_number) / n_columns

    add_to_index = [
        -1 - n_columns, - n_columns, 1 - n_columns,
        -1,                          1            , 
        -1 + n_columns,   n_columns, 1 + n_columns
    ]

    r_idx = []
    # First row
    if row_number == 0:
        r_idx = r_idx + [0,1,2]
    # Last row
    if row_number == n_rows - 1:
        r_idx = r_idx + [5,6,7]
    # First column
    if column_number == 0:
        r_idx = r_idx + [0,3,5]
    # Last column
    if column_number == n_columns - 1:
        r_idx = r_idx + [2,4,7]

    r_idx = list(set(r_idx))

    indexes = [item + index for idx, item in enumerate(add_to_index) if idx not in r_idx]

    return indexes

def get_symbol_positions(linear_data):
    symbols = get_symbols(linear_data)
    char_array = np.array(list(linear_data))

    mask = np.isin(char_array, symbols)

    return np.where(mask)[0].tolist()

def get_many_adjacent_indexes(n_rows, n_columns, indexes):
    x = []
    for idx in indexes:
        x = x + get_adjacent_indexes(n_rows, n_columns, idx)
    return list(set(x))

def get_all_indexes(numbers, starting_indexes):
    all_indexes = []

    for i, (number, starting_idx) in enumerate(zip(numbers, starting_indexes)):
        all_indexes.append(list(range(starting_idx, starting_idx + len(str(number)))))

    return all_indexes

def in_engine_schematic(number_indexes, symbol_neighbours):
    for n in number_indexes:
        if n in symbol_neighbours:
            return True
    return False

if __name__ == "__main__":
    path = get_path(3, False)
    data = load_data(path)
    
    symbols = get_symbols(data)

    n_rows, n_columns, linear_data = parse_data(data)

    symbol_positions = get_symbol_positions(linear_data)
    symbol_neighbours = get_many_adjacent_indexes(n_rows, n_columns, symbol_positions)

    numbers, starting_indexes = get_numbers(linear_data)
    all_indexes = get_all_indexes(numbers, starting_indexes)

    total = 0
    for n, idxs in zip(numbers, all_indexes):
        if in_engine_schematic(idxs, symbol_neighbours):
            total += n

    print(total)

    # print(numbers, indexes)

    # n = 0
    # for i in range(10):
    #     for j in range(10):
    #         print(n, end=" ")
    #         n += 1
    #     print()
    # print(get_adjacent_indexes(n_rows, n_columns, 87))
