# Bunmi Oluwatudimu
# bmo43
# Class for all ball objects

from drawable2 import Drawable
import pygame


class Ball(Drawable):
    # Initializes ball class and inherits from drawable class
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
        pygame.draw.circle(surface, self.__color, [int(locationX), int(locationY)], 5)

    def getRectangle(self):
        locationX = self.getXlocation()
        locationY = self.getYlocation()
        return pygame.Rect([int(locationX - 5), int(locationY - 5), 5, 5])