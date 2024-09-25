def multiply(times):
    def decorator(function):
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
    return [['*' for _ in range(size)] for _ in range(size)]


matrices = create_matrix(5)

# Print 'items()', knowing that the function returns dictionary not list after the decorating
for k, v in matrices.items():
    print(f"This is matrix {k}: {v}")
