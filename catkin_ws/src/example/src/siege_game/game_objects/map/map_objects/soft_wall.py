from typing import Tuple
from siege_game.game_objects.map.map_objects.map_object import MapObject

class SoftWall(MapObject):
    def __init__(self, location:Tuple):
        super().__init__(location)
        self.set_is_breakable(True)
        self.__is_broken = False

    def get_is_broken(self) -> bool:
        return self.__is_broken
    
    def break_it(self) -> None:
        self.__is_broken = True

    def __str__(self):
        return f"Soft Wall ({self.get_location()})"
    
    def __repr__(self):
        return f"Soft Wall ({self.get_location()})"