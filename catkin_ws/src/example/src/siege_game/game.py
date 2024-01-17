import rospy
from std_msgs.msg import String
# from sensor_msgs.msg import Mouse

from siege_game.game_objects.map_builder import MapBuilder
from siege_game.game_objects.logger import Logger
from siege_game.game_objects.commander import Commander
import time

class Game():
    instance = None
    logger = Logger("Game")

    def __init__(self):
        self.__map_name = "map_example"
        self.__commander = None
        self.__map = None
        builder = MapBuilder(self.__map_name)
        self.__map = builder.get_map()
        self.__commander = Commander(self)
        Game.logger.info(f"Command set: {self.__commander}")

    @classmethod
    def get_instance(cls):
        if (cls.instance == None):
            cls.instance = Game()

        return cls.instance
    
    def run(self, my_publisher):
        counter = 0
        self.__map.print_map()
        while not rospy.is_shutdown():
            my_publisher.publish(counter)
            rospy.sleep(0.1)
            counter += 1

    def get_commander(self):
        return self.__commander
    
    def get_map(self):
        return self.__map




