from player import Player


class Roll(Player):
    def __init__(self, name) -> None:
        super().__init__(name)


class Rock(Roll):
    def __init__(self) -> None:
        pass


class Paper(Roll):
    def __init__(self) -> None:
        pass


class Scissors(Roll):
    def __init__(self) -> None:
        pass
