"""
The book doesn't really have to be aware of its own location, which is another responsibility.

So for the purpose of keeping the SRP, we have created a new class with a single responsibility,
to manage the books.

Single-Responsibility Principle -> A class should have only one reason to change.
"""


from typing import List


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        # self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)

    def remove_books(self, book_title: str):
        for book_obj in self.books:
            if book_obj.title == book_title:
                self.books.remove(book_obj)
                return

    def get_book(self, book_title: str):
        try:
            book = [b for b in self.books if b.title == book_title][0]
            return book
        except IndexError:
            return "Book not found."
