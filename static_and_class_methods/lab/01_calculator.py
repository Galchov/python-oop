class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        r = 1
        for x in args:
            r *= x

        return r

    @staticmethod
    def divide(initial, *args):
        r = initial
        for x in args:
            r /= x

        return r

    @staticmethod
    def subtract(initial, *args):
        r = initial
        for x in args:
            r -= x

        return r


# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
