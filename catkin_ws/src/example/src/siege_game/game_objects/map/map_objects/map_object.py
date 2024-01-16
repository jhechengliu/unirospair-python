from abc import ABC
from typing import Tuple

class MapObject(ABC):

    def __init__(self, location:Tuple):
        """
            Initialize the object with a location attribute.

            Args:
                location (tuple): A pair of coordinates (x, y) representing the location of the object.

            Attributes:
                __isbroken (bool): A private attribute to indicate if the object is broken. Default to False.
                __location (tuple): A private attribute to store the location of the object.
        """
        self.__is_breakable = None
        self.__location = location

    def get_location(self) -> Tuple:
        return self.__location
    
    def set_is_breakable(self, is_breakable:bool) -> None:
        self.__is_breakable = is_breakable

    def get_is_breakable(self) -> Tuple:
        return self.__is_breakable