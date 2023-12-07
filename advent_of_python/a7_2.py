from utils import get_path, load_data
import pandas as pd

def hand_type(hand):
    if hand == 'JJJJJ':
        return 6

    unique_cards = list(set(hand))

    # Now do the joker check
    n_jokers = 0
    if 'J' in unique_cards:
        unique_cards.remove('J')
        n_jokers = hand.count('J')

    card_counts = [0] * len(unique_cards)

    for i, c in enumerate(unique_cards):
        for ch in hand:
            if c == ch:
                card_counts[i] += 1

    card_counts = sorted(card_counts, reverse = True)

    # Now add the jokers back
    card_counts[0] += n_jokers

    if card_counts == [5]:
        return 6
    elif card_counts == [4,1]:
        return 5
    elif card_counts == [3,2]:
        return 4
    elif card_counts == [3,1,1]:
        return 3
    elif card_counts == [2,2,1]:
        return 2
    elif card_counts == [2,1,1,1]:
        return 1
    else:
        return 0


def parse_input(data):
    lines = data.split("\n")

    hands = []
    bids = []

    for line in lines:
        hand, bid = line.split()
        hands.append(hand.strip())
        bids.append(int(bid))

    return hands, bids

def hands_to_df(hands, bids):
    
    hands_df = []

    for hand, bid in zip(hands, bids):
        hands_df.append([hand] + [x for x in hand] + [bid])

    return pd.DataFrame(hands_df, columns = ['hand'] + ['col' + str(i + 1) for i in range(5)] + ['bid'])

def df_to_values(df):
    
    card_dct = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }


    for col in ['col' + str(i + 1) for i in range(5)]:
        df[col] = df[col].map(card_dct)

    df['hand_value'] = df['hand'].apply(lambda x: hand_type(x))

    return df

if __name__ == "__main__":
    path = get_path(7, False)
    data = load_data(path)

    hands, bids = parse_input(data)
    
    df = hands_to_df(hands, bids)
    df = df_to_values(df)

    df = df.sort_values(by = ['hand_value', 'col1', 'col2', 'col3', 'col4', 'col5'], ascending=False).reset_index(drop = True)
    df['rank'] = len(df) - df.index
    print((df['bid'] * df['rank']).sum())

    # print(hand_type("AAAJJ"))
