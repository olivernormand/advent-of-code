from utils import get_path, load_data
from a4_1 import parse_lines

def how_many_matching(winning_numbers, numbers):
    n = 0
    for number in numbers:
        if number in winning_numbers:
            n += 1

    return n

def how_many_scratchcards(lines):

    total_cards = len(lines)

    n_cards = [1] * total_cards

    for i, line in enumerate(lines):
        wn, n = line
        copies = n_cards[i]

        n_matching = how_many_matching(wn, n)

        for j in range(i + 1, i + n_matching + 1):
            n_cards[j] += copies

    return sum(n_cards)




if __name__ == "__main__":
    path = get_path(4, False)
    data = load_data(path)

    lines = parse_lines(data)

    print(how_many_scratchcards(lines))