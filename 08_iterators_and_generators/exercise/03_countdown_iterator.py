class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            current_number = self.count
            self.count -= 1
            return current_number
        raise StopIteration


# Test code:
print("----- Test 1 -----")
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()
print("----- Test 2 -----")
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
