from math import ceil
from typing import List


class PhotoAlbum:
    PAGE_LIMIT = 4

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        pages = ceil(photos_count / cls.PAGE_LIMIT)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        for i, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_LIMIT:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"

        return "No more free slots"

    def display(self) -> str:
        page_separator = "-" * 11
        print_info = [page_separator]
        for item in self.photos:
            page_items = len(item) * "[] "
            print_info.append(page_items.strip())
            print_info.append(page_separator.strip())

        return "\n".join(print_info)


# Test code:
# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())


