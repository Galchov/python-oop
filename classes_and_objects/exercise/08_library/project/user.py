from project.library import Library


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        pass

    def return_book(self, author: str, book_name: str, library: Library):
        pass

    def info(self):
        pass

    def __str__(self):
        pass
