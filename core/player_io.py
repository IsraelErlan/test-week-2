def ask_player_action() -> str:
    inpt = input("Enter your choice ('H' to hit, 'S' to stand): ")

    while inpt != 'H' and inpt != 'S':
        print("Please enter validate input!")
        inpt = input("Enter your choice ('H' to hit, 'S' to stand): ")

    return inpt

def game_over(winner: str, player_val:int, dealer_val: int ) -> None:
    print(f"game_over! \nWinner: {winner}\nValues: player-{player_val}, dealer-{dealer_val}")
