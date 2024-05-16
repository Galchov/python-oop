from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> Player or str:
        for player_obj in self.__players:
            if player_obj.name == player_name:
                obj_to_return = player_obj
                self.__players.remove(player_obj)
                return obj_to_return

        return f"Player {player_name} not found"
