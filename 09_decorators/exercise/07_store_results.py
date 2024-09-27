class store_results:
    def __init__(self, function) -> None:
        self.function = function

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a+") as file:
            func_result = self.function(*args, **kwargs)
            file.write(f"Function {self.function.__name__} was called. Result: {func_result}\n")

        return func_result


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)