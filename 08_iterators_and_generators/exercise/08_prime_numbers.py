from math import sqrt


def get_primes(int_list):
    for num in int_list:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num


# Test code:
print("---- Test 1 -----")
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print("----- Test 2 -----")
print(list(get_primes([-2, 0, 0, 1, 1, 0])))