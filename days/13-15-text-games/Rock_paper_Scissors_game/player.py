from random import randint


class Player:
    def __init__(self, name) -> None:
        self.name = name

    def get_random_choice(self):
        return randint(0, 2)

    def Choose_Choice(self):
        choice = 3
        while choice not in range(0, 3):
            choice = input("Choose either Rock (r), Paper (p) or Scissors (s): ")
            if choice == "r":
                return 0
            if choice == "p":
                return 1
            if choice == "s":
                return 2
