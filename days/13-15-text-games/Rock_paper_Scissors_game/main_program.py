from player import Player
from roll import Roll, Rock, Paper, Scissors


def print_header():
    print("------------------------------------")
    print("       ROCK, PAPER, SCISSORS")
    print("------------------------------------")
    print()
    print("Welcome to Rock, Paper, Scissors")
    print()


def build_the_three_rolls():
    choices = ["Rock", "Paper", "Scissors"]
    return choices


def get_players_name():
    name = input("What is your name? ")
    return name


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = rolls[player2.get_random_choice()]  # TODO: get random roll
        p1_roll = rolls[player1.Choose_Choice()]  # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print(f"Round {count} rolls are")
        print(f"{player2.name} chose {p2_roll}")
        print(f"{player1.name} chose {p1_roll}")
        # display winner for this round
        print(f"The winner for Round {count} is {outcome}")

        count += 1

    # Compute who won


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


if __name__ == "__main__":
    main()
