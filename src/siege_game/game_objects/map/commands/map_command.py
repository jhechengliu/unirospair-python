from abc import ABC
import abc
from siege_game.game_objects.states.state import State


import typing

class MapCommand(ABC):
    def __init__(self, game, args:tuple[str], identity):
        from siege_game.game import Game
        from siege_game.game_objects.player import Identity
        self.__game:Game = game
        self.__args:tuple[str] = args
        self.__identity:Identity = identity

    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def check(self) -> bool: 
        raise NotImplementedError()
    
    def get_map(self):
        return self.__game.get_map()
    
    def get_args(self) -> tuple:
        return self.__args
    
    def get_identity(self):
        return self.__identity
    

    

    
    
    