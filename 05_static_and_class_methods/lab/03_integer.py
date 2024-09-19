"""Example of 'Class Methods' used with different requirements and functionality to
instantiate objects"""


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float or str) -> "Integer" or str:
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str) -> "Integer":
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }

        int_value = 0

        for i in range(len(value)):
            if value[i] in roman_numerals:
                if i + 1 < len(value) and roman_numerals[value[i]] < roman_numerals[value[i + 1]]:
                    int_value -= roman_numerals[value[i]]
                else:
                    int_value += roman_numerals[value[i]]

        return cls(int_value)

    @classmethod
    def from_string(cls, value: str or float) -> "Integer" or str:
        if not isinstance(value, str):
            return "wrong type"
        try:
            cls(int(value))
        except ValueError:
            return "wrong type"


# Test code:
# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))