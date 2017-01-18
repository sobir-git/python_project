#! /usr/bin/env python

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))#creates game screen with 800 x #600 in size


pygame.mouse.set_visible(0)

ship = pygame.image.load("images/ship.png")#loads an image onto the pygame screen
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width() / 2 - ship.get_width() / 2

screen.blit(ship, (ship_left, ship_top))


while True:
    clock.tick(60)#Using this clock object will let the game run at 60 frames per second.
    pygame.display.update()
#The code below allows for the user to close the application using the x button at the top right corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
