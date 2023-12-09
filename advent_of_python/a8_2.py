# from utils import get_path, load_data

# def parse_input(data):
#     data = data.split("\n")

#     navigation = data[0]

#     keys = data[2:]

#     keys = parse_keys(keys)

#     return navigation, keys

# def parse_keys(keys):
#     new_keys = {}
#     for key in keys:
#         input, outputs = key.split('=')
#         input = input.strip()
#         outputs = [x.strip() for x in outputs.split(',')]
#         outputs = [outputs[0][1:], outputs[1][:-1]]

#         new_keys[input] = outputs
    
#     return new_keys

# def get_index(step, navigation):

#     rl_map = {
#         "R": 1,
#         "L": 0,
#     }
#     n_steps = len(navigation)

#     step = step % n_steps

#     return rl_map[navigation[step]]

# def do_a_step(input, step, keys, navigation):
#     index = get_index(step, navigation)

#     return keys[input][index]

# def get_starting_nodes(keys):
#     starting_nodes = []
#     for node in keys.keys():
#         if node[-1] == 'A':
#             starting_nodes.append(node)
#     return starting_nodes

# def get_evolve_nodes(nodes):
#     evolve_nodes = []

#     for node in nodes:
#         if node[-1] != 'Z':
#             return False
#     return True

# if __name__ == "__main__":
#     path = get_path(8, False)
#     data = load_data(path)

#     navigation, keys = parse_input(data)

#     nodes = get_starting_nodes(keys)
#     step = 0
#     stop = False

    
#     # while not stop:
#     #     print(step, nodes)
#     #     nodes = [do_a_step(x, step, keys, navigation) for x in nodes]
#     #     step += 1
#     #     stop = get_evolve_nodes(nodes)

#     # Okay so this doesn't work, we're going to have to take a different approach potentially. I think there'll be quite a large number, which we may or may not be able to reach by just brute forcing it. We probably will be able to get there with enough time but that seems bad. However for each of the underlying starting nodes, we can find out a) how long it takes them to get to their ending Z value the first time, and then how long it takes to get from one to another. Once we know that we can then do a bit of a LCM type of argument


#     print(nodes)

from utils import get_path, load_data
import numpy as np

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

def get_starting_nodes(keys):
    starting_nodes = []
    for node in keys.keys():
        if node[-1] == 'A':
            starting_nodes.append(node)
    return starting_nodes

def step_till_ends_z(nodes, steps):
    ends_new = []
    steps_new = []

    for output, step in zip(nodes, steps):
        initial_output = output

        output = do_a_step(output, step, keys, navigation)
        step += 1


        while (output[2] != 'Z'):
            output = do_a_step(output, step, keys, navigation)
            step += 1
        
        ends_new.append(output)
        steps_new.append(step)

    steps_new = [x - y for x, y in zip(steps_new, steps)]

    return ends_new, steps_new

def find_minimum_common_value(size_start, size_interval):

    n_interval = np.ones(len(size_start), dtype = int)

    while True:
        # Calculate the current values
        current_values = size_start + size_interval * n_interval
        max_value = np.max(current_values)
        min_value = np.min(current_values)

        # Check if all the values are equal
        if max_value == min_value:
            return n_interval, max_value
        
        # Otherwise increment the smallest value
        min_index = np.argmin(current_values)

        n_interval[min_index] += 1 

        print(n_interval)


if __name__ == "__main__":
    path = get_path(8, False)
    data = load_data(path)

    navigation, keys = parse_input(data)

    starting_nodes = get_starting_nodes(keys)
    steps_a = [0,0,0,0,0,0]
    
    a_z, start_steps = step_till_ends_z(starting_nodes, steps_a)

    z_z, interval_steps = step_till_ends_z(a_z, start_steps)

    # If this is also true for you then we're in a nice closed loop
    assert a_z == z_z 

    n_nav = len(navigation)

    print(starting_nodes)
    print(a_z)
    print(z_z)
    print(start_steps)
    print(interval_steps)

    # Our data also has this nice feature
    assert start_steps == interval_steps

    # Our data also has the nice feature where this will only print prime numbers
    n_nav_cycles = [x / n_nav for x in interval_steps]

    # Hence the lowest common multiple is simply the total multiple
    total = n_nav

    for x in n_nav_cycles:
        total *= x
    print(int(total))

    # And that solved it. Would have been more difficult if it weren't for some nice features in that dataset tbh



    # Then we know all the step value that we require to end each stream in a z. We can use this to quickly work out where each stream will end in a z, and then work out where this step value is seen across all the streams. 

    # print(find_minimum_common_value(start_steps, interval_steps))


    