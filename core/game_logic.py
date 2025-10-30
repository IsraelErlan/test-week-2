from core.player_io import ask_player_action, game_over

def handle_ace(hand_val)-> int:
    inpt = None
    if hand_val > 10:
        return 1
    elif hand_val == 10:
        return 11
    else:
        inpt = input("Do you want add 1 or 11?")
        while(inpt != '1' and inpt != 11):
            print("valid input: 1 or 11")
            inpt = input("Do you want add 1 or 11?")

        return inpt



def calculate_hand_value(hand: [dict]) -> int:
    has_ace = False
    hand_value = 0
    for card in hand:
        rank = card["rank"]
        if rank.isdigit():
            hand_value += int(rank)
        elif rank != 'A':
            hand_value += 10
        else:
            if has_ace:
                hand_value += 1
            else:
                has_ace = True
                hand_value += handle_ace(hand_value)




    return hand_value


def deal_tow_each(deck: [dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    player["hand"].append(deck.pop())

    dealer["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())

    p_val = calculate_hand_value(player["hand"])
    d_val = calculate_hand_value(dealer["hand"])

    print(f"player hand-value:{p_val}, dealer hand-value: {d_val}")




def dealer_play(deck: [dict], dealer: dict) ->bool:
    cur_hand = calculate_hand_value(dealer["hand"])

    while(cur_hand < 17):
        dealer["hand"].append(deck.pop())
        cur_hand = calculate_hand_value(dealer["hand"])

    if cur_hand > 21:
        return False
    return True



def run_full_game(deck: [dict], player: dict, dealer:dict) -> None:
    deal_tow_each(deck, player, dealer)

    choice = ask_player_action()
    while choice == 'H':
        player["hand"].append(deck.pop())
        player_val = calculate_hand_value(player["hand"])

        if player_val > 21:
            dealer_val = calculate_hand_value(dealer["hand"])
            game_over("Dealer",player_val ,dealer_val)
            return

        elif player_val == 21:
            dealer_val = calculate_hand_value(dealer["hand"])
            game_over("Player", player_val, dealer_val)

        print(f"Your hand: {player_val}")
        choice = ask_player_action()

    player_val = calculate_hand_value(player["hand"])

    if not dealer_play(deck, dealer):
        dealer_val = calculate_hand_value(dealer["hand"])
        game_over("Player", player_val, dealer_val)
        return


    dealer_val = calculate_hand_value(dealer["hand"])
    if dealer_val > player_val:
        game_over("Dealer",player_val ,dealer_val)
    elif dealer_val < player_val:
        game_over("Player", player_val, dealer_val)
    elif dealer_val == player_val:
        game_over("Equal", player_val, dealer_val)