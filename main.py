from core.deck import build_standard_deck, shuffle_by_suit
from core.game_logic import run_full_game

def play():
    deck = build_standard_deck()
    shuffle_by_suit(deck)
    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(deck, player, dealer)


if __name__ == "__main__":
    play()
