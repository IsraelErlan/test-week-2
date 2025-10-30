from random import randint as rand



def build_standard_deck() -> [dict]:
    cards_list = []
    suites_list = ['S', 'H', 'C', 'D']
    ranks_list = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    for rank in ranks_list:
        for suite in suites_list:
            cards_list.append({"rank": rank, "suite": suite})

    return cards_list


def shuffle_by_suit(deck: [dict], swaps: int = 5000) -> [dict]:
    while swaps > 0:
        i = rand(0, 51)
        j = rand(0, 51)
        if i == j:
            continue

        if deck[i]["suite"] == 'H' and j % 5 != 0:
            continue

        if deck[i]["suite"] == 'C' and j % 3 != 0:
            continue

        if deck[i]["suite"] == 'D' and j % 2 != 0:
            continue

        if deck[i]["suite"] == 'S' and j % 7 != 0:
            continue

        deck[i], deck[j] = deck[j], deck[i]
        swaps -= 1

    return deck








