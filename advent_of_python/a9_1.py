from utils import get_path, load_data
import numpy as np

def parse_input(data):
    historys = data.split('\n')
    historys = [[int(x.strip()) for x in history.split(" ")] for history in historys]
    return historys

def extrapolate_history(history):
    diffs = []
    diff = np.array(history)
    while True:
        diffs.append(diff)
        diff = np.diff(diff)
        if np.all(diff == 0):
            diffs.append(diff)
            break

    diffs = diffs[::-1]

    for i in range(len(diffs) - 1):
        x1 = diffs[i][-1]
        x2 = diffs[i+1][-1]

        diffs[i+1] = np.append(diffs[i+1], [x1 + x2])

    return diffs[-1][-1]
    

if __name__ == "__main__":
    path = get_path(9, False)
    data = load_data(path)

    historys = parse_input(data)

    total = 0
    for history in historys:
        next = extrapolate_history(history)
        total += next
        print(next)

    print(total)