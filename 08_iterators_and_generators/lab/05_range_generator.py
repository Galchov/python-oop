def genrange(start: int, end: int):
    current_number = start
    while current_number <= end:
        yield current_number
        current_number += 1


# Test code:
print(list(genrange(1, 10)))
