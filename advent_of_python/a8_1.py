from utils import get_path, load_data

def parse_input(data):
    data = data.split("\n")

    navigation = data[0]

    keys = data[2:]

    keys = parse_keys(keys)

    return navigation, keys

def parse_keys(keys):
    new_keys = {}
    for key in keys:
        input, outputs = key.split('=')
        input = input.strip()
        outputs = [x.strip() for x in outputs.split(',')]
        outputs = [outputs[0][1:], outputs[1][:-1]]

        new_keys[input] = outputs
    
    return new_keys

def get_index(step, navigation):

    rl_map = {
        "R": 1,
        "L": 0,
    }
    n_steps = len(navigation)

    step = step % n_steps

    return rl_map[navigation[step]]

def do_a_step(input, step, keys, navigation):
    index = get_index(step, navigation)

    return keys[input][index]

if __name__ == "__main__":
    path = get_path(8, False)
    data = load_data(path)

    navigation, keys = parse_input(data)

    output = 'RMA'
    step = 0

    while (output != 'ZZZ'):
        output = do_a_step(output, step, keys, navigation)
        step += 1

    print(step, output)
    