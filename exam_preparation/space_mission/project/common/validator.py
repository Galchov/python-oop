class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(value, error_message):
        if value.strip() == '':
            raise ValueError(error_message)
