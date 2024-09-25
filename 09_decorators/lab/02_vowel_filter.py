def vowel_filter(function):

    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        final_result = [letter for letter in func_result if letter.lower() in 'aeouiy']
        return final_result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
