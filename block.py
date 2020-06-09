# Bunmi Oluwatudimu
# bmo43
# Class for all block objects

from drawable2 import Drawable
import pygame


class Block(Drawable):
    # Initializes class and inherits from drawable class
    def __init__(self, x=0, y=0, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__color = color

    # Getters
    def getColor(self):
        return self.__color

    # Setters
    def setColor(self, item):
        self.__color = item

    # Abstract methods
    def draw(self, surface):
        locationX = self.getXlocation()
        locationY = self.getYlocation()
        if self.getVisibility():
            pygame.draw.rect(surface, self.__color, [int(locationX), int(locationY), 10, 10])
            pygame.draw.lines(surface, (0, 0, 0), True,
                              [(int(locationX), int(locationY)), (int(locationX), int(locationY + 10)),
                               (int(locationX + 10), int(locationY + 10)), (int(locationX + 10), int(locationY))], 1)

    def getRectangle(self):
        locationX = self.getXlocation()
        locationY = self.getYlocation()
        return pygame.Rect([int(locationX), int(locationY), 10, 10])