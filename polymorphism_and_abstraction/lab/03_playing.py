def start_playing(some_object):
    """Returns True if the given object has the play() method,
    otherwise returns False"""

    return some_object.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
