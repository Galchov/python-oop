class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    def __str__(self) -> str:
        print_data = (f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\n"
                      f"Passing: {self.__passing}\nShooting: {self.__shooting}")

        return print_data
