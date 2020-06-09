# Bunmi Oluwatudimu
# bmo43
# Class for all text objects

from drawable2 import Drawable
import pygame


class Text(Drawable):
    def __init__(self, message="Score", x=0, y=0, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__message = message
        self.__color = color

    # Getters
    def getColor(self):
        return self.__color

    def getMessage(self):
        return self.__message

    # Setters
    def setColor(self, item):
        self.__color = item

    def setMessage(self, item):
        self.__message = item

    # Abstract methods
    def draw(self, surface):
        fontObj = pygame.font.Font("freesansbold.ttf", 12)
        self.__surface = fontObj.render(self.__message, True, self.__color)
        surface.blit(self.__surface, self.getLocation())

    def getRectangle(self):
        return self.__surface.get_rect()