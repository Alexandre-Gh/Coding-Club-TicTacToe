#
# This is where you can code your game and the logic
# You can write inside the functions, create new functions and variables or modify the variables
#
# /!\ Do not modify the actual structures of the functions, otherwise it will not work /!\
#

import sys
import pygame
from workshopFunctions import drawCircle, drawCross, drawGrid, drawEndScreen, foreachField, printField, createEndScreenText, noMoreSpace


###################
#### Variables ####
###################

# Colours
black = 0, 0, 0
grey = 122, 122, 122
white = 255, 255, 255

# window
size = 30
window = None

# game logic

field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

status = 'playing'
endScreenText = None
turn = 'Player1'


###################
#### Functions ####
###################

# handle mouse clicks
def onClick(cursorPositionX, cursorPositionY):


# handle whats visible in the window
def draw(window):
    



#########################
# background game logic #
#     Can be ignored    #
#########################

pygame.init()
window = pygame.display.set_mode([size, size])

while (1):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                onClick(event.pos[0], event.pos[1])
    window.fill(black)
    draw(window)
    pygame.display.flip()
