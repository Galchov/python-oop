class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    # Less than / self < other
    def __lt__(self, other):
        return self.get_area() < other.get_area()

    # Less than or Equal / self <= other
    def __le__(self, other):
        return self.get_area() <= other.get_area()

    # Equal to / self == other
    def __eq__(self, other):
        return self.get_area() == other.get_area()

    # Not equal / self != other
    def __ne__(self, other):
        return self.get_area() != other.get_area()

    # Greater than / self > other
    def __gt__(self, other):
        return self.get_area() > other.get_area()

    # Greater than or Equal / self >= other
    def __ge__(self, other):
        return self.get_area() >= other.get_area()


# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)
#
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)
#
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)
