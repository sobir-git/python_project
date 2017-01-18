#! /usr/bin/env python

import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))#creates game screen with 800 x #600 in size


pygame.mouse.set_visible(0)#turns mouse invisible on game screen 

ship = pygame.image.load("images/ship.png")#loads a ship image onto the pygame screen
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width() / 2 - ship.get_width() / 2

screen.blit(ship, (ship_left, ship_top))

shot = pygame.image.load("images/ammo.png")#loads shot image onto screen
shot_y = 0

while True:
    clock.tick(60)#Using this clock object will let the game run at 60 frames per second.
    screen.fill((0,0,0))#makes screen filled with black or no color
    x,y = pygame.mouse.get_pos()#gets position of mouse and makes x,y positions
    screen.blit(ship, (x-ship.get_width()/2, ship_top))#draws ship onto screen  
    pygame.display.update()

#The code below allows for the user to close the application using the x button at the top right corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:#when mouse is pressed set shot_y to 500 and moves 10 px during
            #each loop
            shot_y = 500
            shot_x = x

    if shot_y > 0:
        screen.blit(shot, (shot_x, shot_y))
        shot_y -= 10

    pygame.display.update()
