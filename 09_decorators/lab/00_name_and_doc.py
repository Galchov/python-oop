from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            ready_collection = dict()
            for i in range(times):
                ready_collection[i + 1] = result
                print(f"Item {i + 1} added to the collection.")
            return ready_collection
        return wrapper
    return decorator


@multiply(10)
def create_matrix(size):
    """Creates and returns a matrix with a given size"""
    return [['*' for _ in range(size)] for _ in range(size)]


print(create_matrix.__name__)
print(create_matrix.__doc__)
