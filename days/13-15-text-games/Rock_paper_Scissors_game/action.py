from enum import IntEnum



class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

    def can_defeat(user_action, computer_action) -> str:
        if user_action == computer_action:
            print(f"Both players selected {user_action.name}. It's a tie!")
            return "Draw"
        elif user_action == Action.Rock:
            if computer_action == Action.Scissors:
                print("Rock smashes scissors! You win!")
                return "Win"
            else:
                print("Paper covers rock! You lose.")
                return "Lose"
        elif user_action == Action.Paper:
            if computer_action == Action.Rock:
                print("Paper covers rock! You win!")
                return "Win"
            else:
                print("Scissors cuts paper! You lose.")
                return "Lose"
        elif user_action == Action.Scissors:
            if computer_action == Action.Paper:
                print("Scissors cuts paper! You win!")
                return "Win"
            else:
                print("Rock smashes scissors! You lose.")
                return "Lose"
