from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # Users (Objects) of the Library
        self.books_available = {}  # {Author: [Books available]}
        self.rented_books = {}  # {Username: {Book name: Days to return}}

    def add_user(self, user: User):
        if user not in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        pass
