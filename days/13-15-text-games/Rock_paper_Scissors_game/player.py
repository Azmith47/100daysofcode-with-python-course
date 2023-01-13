from action import Action
import random


class Player:
    def __init__(self, name, wins=0, loses=0, draws=0) -> None:
        self.name = name
        self.wins = wins
        self.loses = loses
        self.draws = draws

    def Choose_Action(self):
        choices = [f"{action.name}[{action.value}]" for action in Action]
        choices_str = ", ".join(choices)
        selection = input(f"Enter a choice ({choices_str}): ")
        selection = int(selection)
        action = Action(selection)
        return action

    def Get_Random_Action(self):
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action
