# Bunmi Oluwatudimu
# bmo43
# Main script to simulate a ball hitting blocks using pygame

import pygame
import random
from drawable2 import Drawable
from ball import Ball
from block import Block
from text import Text

# initializes pygame, display mode and display caption
pygame.init()
surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('CS 172 Pygame')
fpsClock = pygame.time.Clock()

# constants used in calculations
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5
xv = 0
yv = 0
score = 0


# intersect function used for collision determination
def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (
            rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False


# Instantiate all objects and append into object lists drawables and blocks
drawables = []
blocks = []

newBall = Ball(10, 350, (255, 0, 0))
newBlock1 = Block(300, 320, (0, 0, 255))
newBlock2 = Block(300, 330, (0, 0, 255))
newBlock3 = Block(300, 340, (0, 0, 255))
newBlock4 = Block(310, 320, (0, 0, 255))
newBlock5 = Block(310, 330, (0, 0, 255))
newBlock6 = Block(310, 340, (0, 0, 255))
newBlock7 = Block(320, 320, (0, 0, 255))
newBlock8 = Block(320, 330, (0, 0, 255))
newBlock9 = Block(320, 340, (0, 0, 255))
newText = Text('Score: 0', 0, 0, (0, 0, 0))
resetText = Text('Press r to reset ball', 250, 0, (0, 0, 0))
quitText = Text('Press q to quit game', 250, 10, (0, 0, 0))

drawables.append(newBall)
drawables.append(newBlock1)
drawables.append(newBlock2)
drawables.append(newBlock3)
drawables.append(newBlock4)
drawables.append(newBlock5)
drawables.append(newBlock6)
drawables.append(newBlock7)
drawables.append(newBlock8)
drawables.append(newBlock9)
drawables.append(newText)
drawables.append(resetText)
drawables.append(quitText)

blocks.append(newBlock1)
blocks.append(newBlock2)
blocks.append(newBlock3)
blocks.append(newBlock4)
blocks.append(newBlock5)
blocks.append(newBlock6)
blocks.append(newBlock7)
blocks.append(newBlock8)
blocks.append(newBlock9)

# main game loop
shot = False

while True:
    for event in pygame.event.get():
        # quit event
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()

        # shooting ball even
        if (event.type == pygame.MOUSEBUTTONDOWN):
            shot = False
            startpos = event.pos

        elif (event.type == pygame.MOUSEBUTTONUP):
            if not shot:
                endpos = event.pos
                shot = True
                xv = endpos[0] - startpos[0]
                yv = -(endpos[1] - startpos[1])

        # reset event
        elif (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_r):
            newBall.setLocation([10, 350])
            shot = False

    # physics behind ball animation
    if shot == True:
        y = newBall.getYlocation()
        x = newBall.getXlocation()

        x = x + (dt * xv)
        y = y - (dt * yv)

        newBall.setY(y)
        newBall.setX(x)

        if y > 350:
            yv = -R * yv
            xv = eta * xv
        else:
            yv = yv - (g * dt)

    surface.fill((255, 255, 255))
    pygame.draw.line(surface, (0, 0, 0), (0, 350), (400, 350), 1)

    # drawing of objects
    for drawable in drawables:
        drawable.draw(surface)

    for block in blocks:
        block.draw(surface)

    # collision detection, removing visibility of blocks, and updating score
    for b in range(len(blocks)):
        if intersect(newBall.getRectangle(), blocks[b].getRectangle()):
            if blocks[b].getVisibility():
                score += 1
                myString = 'Score: ' + str(score)
                newText.setMessage(myString)
            blocks[b].setVisibility(False)

    pygame.display.update()
    fpsClock.tick(50)