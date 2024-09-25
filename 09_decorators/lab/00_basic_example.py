def uppercase(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


@uppercase
def give_historical_info():
    return "Gaius Marius was a Roman general and statesman."


print(give_historical_info())
