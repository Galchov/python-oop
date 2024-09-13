"""
'If it walks like a duck, and it quacks like a duck, then it must be a duck.'

Just a brief example of so called 'Duck Typing' in Python,
without diving too deep into it.
"""


def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


guitar = Guitar()
print(start_playing(guitar))

children = Children()
print(start_playing(children))
