from math import sqrt
from time import time
from typing import List


def measure_time(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"Time running: {end_time - start_time:.2f}")
        return result
    return wrapper


@measure_time
def find_primes(numbers: List[int]) -> List[int]:
    prime_numbers = []

    for num in numbers:
        if num < 2:
            continue

        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)

    return prime_numbers


print(find_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
