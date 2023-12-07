from utils import get_path, load_data

def parse_data(data):
    data = data.split("\n\n")
    seeds_dirty = data[0]
    maps_dirty = data[1:]
    return seeds_dirty, maps_dirty

def parse_seeds(seeds_dirty):
    dont_care, care = seeds_dirty.split(":")
    seeds_clean = [int(x.strip()) for x in care.split()]
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

def use_map(input, map_clean):
    # d_start --> destination range start
    # s_start --> source range start
    # r_length --> range length

    for page in map_clean:
        d_start, s_start, r_length = page

        if input in range(s_start, s_start + r_length):
            return d_start + (input - s_start)
        
    return input

def use_maps(s, maps):
    for m in maps:
        s = [use_map(i, m) for i in s]
    return s

if __name__ == "__main__":
    path = get_path(5, False)
    data = load_data(path)

    s, ms = parse_data(data)
    s, ms = get_seed_and_maps(s, ms)
    
    print(min(use_maps(s, ms)))