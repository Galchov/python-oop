# from itertools import permutations


def possible_permutations(numbers_list):
    # for perm in permutations(numbers_list):
    #     yield list(perm)
    if len(numbers_list) <= 1:
        yield numbers_list
    else:
        for i in range(len(numbers_list)):
            for perm in possible_permutations(numbers_list[:i] + numbers_list[i + 1:]):
                yield [numbers_list[i]] + perm


# Test code:
print("----- Test 1 -----")
[print(n) for n in possible_permutations([1, 2, 3])]
print("----- Test 2 -----")
[print(n) for n in possible_permutations([1])]
