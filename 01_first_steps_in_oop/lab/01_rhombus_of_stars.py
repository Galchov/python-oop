n = int(input())

for row in range(1, n + 1, 1):
    print(" " * (n - row), *["*"] * row)

for row in range(n - 1, 0, -1):
    print(" " * (n - row), *["*"] * row)


# Played with functions

# def print_row(n, row):
#     print(" " * (n - row), *["*"] * row)
#
#
# def print_triangle(n):
#     for row in range(1, n + 1, 1):
#         print_row(n, row)
#
#
# def print_reversed_triangle(n):
#     for row in range(n - 1, 0, -1):
#         print_row(n, row)
#
#
# def create_rhombus(n):
#     print_triangle(n)
#     print_reversed_triangle(n)
#
#
# create_rhombus(int(input()))
