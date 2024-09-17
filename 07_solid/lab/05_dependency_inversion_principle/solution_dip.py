"""
Here, the problem is solved with abstraction, which removes the bad example of instantiating
new 'Formatter' object within the 'Printer' class every time we need to work with it.
Now based on the abstract 'Formatter' class, there's the opportunity to extend its functionality
and apply it in the 'Printer' without changing anything in the last.

Dependency Inversion Principle -> Abstractions should not depend upon details. Details should
depend upon abstractions.
"""


from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:10]


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter):
        formatted_book = formatter.format(book)
        return formatted_book
