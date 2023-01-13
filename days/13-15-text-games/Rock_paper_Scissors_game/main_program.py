from player import Player
from action import Action


def print_header():
    print("------------------------------------")
    print("       ROCK, PAPER, SCISSORS")
    print("------------------------------------")
    print()
    print("Welcome to Rock, Paper, Scissors")
    print()

    # def build_the_three_rolls():
    # choices = ["Rock", "Paper", "Scissors"]
    # return choices


def add_score(outcome, p1, p2):
    if outcome == "Draw":
        p1.draws += 1
        p2.draws += 1
        return "a draw! "
    elif outcome == "Win":
        p1.wins += 1
        p2.loses += 1
        return f"{p1.name} Wins!"
    else:
        p1.loses += 1
        p2.wins += 1
        return f"{p2.name} Wins!"


def reset_game(p1, p2):
    p1.wins = 0
    p1.loses = 0
    p1.draws = 0
    p2.wins = 0
    p2.loses = 0
    p2.draws = 0


def get_players_name() -> str:
    name = input("What is your name? ")
    return name


def game_loop(player1, player2):
    count = 1
    while True:
        try:
            p1_roll = player1.Choose_Action()  # have player choose a roll
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        p2_roll = player2.Get_Random_Action()  # get random roll
        print()

        # display throws
        print(f"Round {count} rolls are:")
        print(f"{player2.name} chose {p2_roll.name}")
        print(f"{player1.name} chose {p1_roll.name}")

        # display winner for this round
        print()
        outcome = p1_roll.can_defeat(p2_roll)
        result = add_score(outcome, player1, player2)
        print(f"Round {count} outcome is {result}")

        count += 1

        if player1.wins == player2.wins + 2 or player2.wins == player1.wins + 2:
            break

    # Compute who won
    if player1.wins == player2.wins + 2:
        print(f"The overall winner is {player1.name}")
    else:
        print(f"The overall winner is {player2.name}")


def main():
    print_header()

    # rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    player1.name = player1.name.title()

    while True:
        game_loop(player1, player2)

        rematch = input("Would you like to play again? (y/n): ")
        if rematch.lower() != "y":
            break

        reset_game(player1, player2)


if __name__ == "__main__":
    main()
