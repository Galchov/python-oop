def squares(n):
    current_number = 1
    while current_number <= n:
        yield current_number ** 2
        current_number += 1


# Test code:
print(list(squares(5)))
