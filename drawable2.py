# Bunmi Oluwatudimu
# bmo43
# Abstract Basic Class for all drawables

import abc


class Drawable(metaclass=abc.ABCMeta):
    # Initializes class
    def __init__(self, x=0, y=0, visible=True):
        self.__x = x
        self.__y = y
        self.__visible = visible

    # Getters
    def getLocation(self):
        return (self.__x, self.__y)

    def getXlocation(self):
        return self.__x

    def getYlocation(self):
        return self.__y

    def getVisibility(self):
        return self.__visible

    # Setters
    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    def setX(self, point):
        self.__x = point

    def setY(self, point):
        self.__y = point

    def setVisibility(self, item):
        self.__visible = item

    # Abstract methods
    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def getRectangle(self):
        pass