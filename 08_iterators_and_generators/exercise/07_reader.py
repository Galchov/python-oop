from typing import Iterable


def read_next(*collections: Iterable):
    for collection in collections:
        # for el in collection:
        #     yield el
        yield from collection


# Test code:
print("----- Test 1 -----")
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
print("----- Test 2 -----")
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
