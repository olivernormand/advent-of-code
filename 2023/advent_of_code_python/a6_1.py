from utils import get_path, load_data
import numpy as np

def parse_input(data):
    data = data.split("\n")

    data = [x.split(":")[1].strip() for x in data]

    time = [int(x) for x in data[0].split()]
    distance = [int(x) for x in data[1].split()]
    
    return time, distance

def t1_t2(time, distance, acceleration):

    determinant = time ** 2 - 4 * distance / acceleration

    t1 = (1/2) * (time - np.sqrt(determinant))
    t2 = (1/2) * (time + np.sqrt(determinant))

    t1 = int(t1) + 1

    if t2.is_integer():
        t2 = int(t2) - 1
    else:
        t2 = int(t2)

    return t1, t2

def number_of_ways(t1, t2):
    return t2 - t1 + 1

if __name__ == "__main__":
    path = get_path(6, False)
    data = load_data(path)

    acceleration = 1

    time, distance = parse_input(data)

    start = 1
    for t, d in zip(time, distance):
        t1, t2 = t1_t2(t, d, acceleration)
        x = number_of_ways(t1, t2)
        print(x)
        start *= x

    print(start)