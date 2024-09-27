from typing import Optional


class reverse_iter:
    def __init__(self, iterable: Optional) -> None:
        self.iterable = iterable
        self.current_index = len(self.iterable)
        self.end_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index >= self.end_index:
            return self.iterable[self.current_index]
        raise StopIteration


# Test code:
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)