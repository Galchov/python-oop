def cache(function):
    def wrapper(*args, **kwargs):
        n = int(*args)
        if not wrapper.log.get(n):
            wrapper.log[n] = function(*args, **kwargs)
        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
