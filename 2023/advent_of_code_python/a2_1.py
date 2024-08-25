import re
import json

path = "/Users/olivernormand/Documents/GitHub/advent_of_code/inputs/2.txt"

game_id_pattern = "Game (\d+):"
n_colour_pattern = "(\d+) (red|green|blue)"
cubes = (12, 13, 14)

with open(path, "r") as f:
    lines = f.readlines()

games = {}
for line in lines:
    game_id = int(re.search(game_id_pattern, line).groups()[0])
    games[game_id] = []
    
    draws = [x.strip() for x in line.split(":")[1].strip().split(";")]

    for i, draw in enumerate(draws):
        draw = [x.strip() for x in draw.split(",")]
        draw = [re.search(n_colour_pattern, x).groups() for x in draw]
        draw = {x[1]: int(x[0]) for x in draw}

        games[game_id].append(draw)

def get_cubes(dct, colour):
    try:
        return dct[colour]
    except KeyError:
        return 0


def game_possible(games, cubes):
    possible_games = []
    colours = ['red', 'green', 'blue']
    n_red, n_green, n_blue = cubes

    for game_id, game in games.items():
        game_possible = True
        
        for draw in game:
            print('draw', draw)
            r = get_cubes(draw, 'red')
            g = get_cubes(draw, 'green')
            b = get_cubes(draw, 'blue')

            if (r > n_red) or (g > n_green) or (b > n_blue):
                game_possible = False
                break

        if game_possible:
            possible_games.append(game_id)
    
    return possible_games

def game_power(games):
    powers = 0
    for game_id, game in games.items():
        rs = []
        gs = []
        bs = []

        for draw in game:
            rs.append(get_cubes(draw, 'red'))
            gs.append(get_cubes(draw, 'green'))
            bs.append(get_cubes(draw, 'blue'))


        r_min = max(rs)
        g_min = max(gs)
        b_min = max(bs)

        power = r_min * g_min * b_min
        print(game_id, [r_min, g_min, b_min], power)
        powers += power

    return powers


# possible_games = game_possible(games, cubes)
# print(sum(possible_games))

print(game_power(games))

        

        

    