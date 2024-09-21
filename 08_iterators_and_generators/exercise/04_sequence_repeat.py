class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            current_index = self.counter % len(self.sequence)
            self.counter += 1
            return self.sequence[current_index]
        raise StopIteration


# Test code:
print("----- Test 1 -----")
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()
print("----- Test 2 -----")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

print()
print("----- Test 3 -----")
result = sequence_repeat('abc', 15)
for item in result:
    print(item, end='')
