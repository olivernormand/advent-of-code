import os

def get_path(n, test = False):
    root = "/Users/olivernormand/Documents/GitHub/advent_of_code/inputs"

    if test:
        next_bit = f"{n}_test.txt"
    else:
        next_bit = f"{n}.txt"

    return os.path.join(root, next_bit)

def load_data(path):
    with open(path, "r") as f:
        data = f.read()
    return data