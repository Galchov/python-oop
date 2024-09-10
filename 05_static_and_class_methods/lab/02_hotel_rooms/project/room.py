class Room:
    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> str or None:
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests += people

    def free_room(self) -> str or None:
        if not self.is_taken:
            return "Room number {number} is not taken"

        self.is_taken = False
        self.guests = 0
