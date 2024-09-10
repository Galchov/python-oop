from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> object:
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> str or None:
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self) -> str:
        vacant_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        occupied_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(vacant_rooms)}\n"
                f"Taken rooms: {', '.join(occupied_rooms)}")


