from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, gender="Male")

    @staticmethod
    def make_sound() -> str:
        return "Hiss"
