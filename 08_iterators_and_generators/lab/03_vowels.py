class vowels:
    def __init__(self, string: str) -> None:
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.filtered_chars = [ch for ch in self.string if ch.lower() in self.vowels]
        self.start_index = 0
        self.end_index = len(self.filtered_chars) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index <= self.end_index:
            current_index = self.start_index
            self.start_index += 1
            return self.filtered_chars[current_index]
        raise StopIteration


# Test code:
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
