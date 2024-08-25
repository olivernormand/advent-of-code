from utils import get_path, load_data

def parse_data(data):
    data = data.split("\n\n")
    seeds_dirty = data[0]
    maps_dirty = data[1:]
    return seeds_dirty, maps_dirty

def parse_seeds(seeds_dirty):
    dont_care, care = seeds_dirty.split(":")
    s = [int(x.strip()) for x in care.split()]

    seeds_clean = []
    for i in range(0, len(s), 2):
        index_start = s[i]
        index_range = s[i + 1]
        seeds_clean.append([index_start, index_range])

    return seeds_clean

def parse_map(map_dirty):
    map_dirty = map_dirty.split("\n")[1:]
    
    map_clean = []

    for m in map_dirty:
        m_clean = [int(x.strip()) for x in m.split()]
        map_clean.append(m_clean)
    
    return map_clean

def get_seed_and_maps(seeds_dirty, maps_dirty):
    seeds_clean = parse_seeds(seeds_dirty)

    maps_clean = []

    for m in maps_dirty:
        maps_clean.append(parse_map(m))

    return seeds_clean, maps_clean

def seperate_inputs_page(inputs, page):
    # d_start --> destination range start
    # s_start --> source range start
    # r_length --> range length

    d_start, s_start, r_length = page
    s_end = s_start + r_length - 1

    new_inputs = []

    for input in inputs:

        i_start, i_length = input
        i_end = i_start + i_length - 1

        if (i_start >= s_start and i_end <= s_end) or (i_end < s_start) or (i_start > s_end):
            # Seed range fits inside a single source range, or sits fully outside it - seed range doesn't change
            new_inputs.append(input)

        elif i_start < s_start and i_end <= s_end:
            # Seed range starts before the source range, but ends within it - return two new seed ranges
            new_inputs.append([i_start, s_start - i_start])
            new_inputs.append([s_start, i_length - (s_start - i_start)])
            print('start before, end in')

        elif i_start >= s_start and i_end > s_end:
            # Seed range starts after the source range, but ends after it - return two new seed ranges
            new_inputs.append([i_start, s_end - i_start + 1])
            new_inputs.append([s_end + 1, i_length - (s_end - i_start + 1)])
            print('start after, end after')

        elif i_start < s_start and i_end > s_end:
            # Seed range starts before the source range, and ends after it - return three new seed ranges
            new_inputs.append([i_start, s_start - i_start])
            new_inputs.append([s_start, r_length])
            new_inputs.append([s_end + 1, i_end - s_end])
            print('start before, end after')

    # Now if the first value of a range falls into a map, then we are guaranteed that the rest of it does as well. 
    # This relies on ranges not overlapping, which seems like a valid assumption
    return new_inputs

def seperate_inputs_map(inputs, map_clean):
    original_n = sum([x[1] for x in inputs])

    for page in map_clean:
        inputs = seperate_inputs_page(inputs, page)

    final_n = sum([x[1] for x in inputs])

    assert original_n == final_n

    return inputs

def use_map(input, map_clean):
    # d_start --> destination range start
    # s_start --> source range start
    # r_length --> range length

    i_start, i_length = input

    for page in map_clean:
        d_start, s_start, r_length = page

        if i_start in range(s_start, s_start + r_length):
            return [d_start + (i_start - s_start), i_length]
        
    return input

def use_maps(s, maps, verbose = True):
    for m in maps:
        if verbose:
            print(s)
            print(m)
            print()
        s = seperate_inputs_map(s, m)
        s = [use_map(i, m) for i in s]
    return s

    

if __name__ == "__main__":
    path = get_path(5, False)
    data = load_data(path)

    s, ms = parse_data(data)
    s, ms = get_seed_and_maps(s, ms)

    s = use_maps(s, ms, verbose = False)

    print(min([x[0] for x in s]))

