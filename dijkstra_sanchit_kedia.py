import cv2
import numpy as np
import math
import time
import pygame

pygame.init()

# Create the display surface object
display_surface = pygame.display.set_mode((600, 250))
# display_surface = pygame.display.set_mode((600*5, 250*5))
pygame.display.set_caption('Project 2')

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


pygame.draw.rect(display_surface, GREEN, (95,0,60,105)) # For Clearance
pygame.draw.rect(display_surface, RED, (100,0,50,100))
pygame.draw.rect(display_surface, GREEN, (95,145,60,105)) # For Clearance
pygame.draw.rect(display_surface, RED, (100,150,50,100))
pygame.draw.polygon(display_surface, GREEN, [(455,20),(455,230),(515,125)]) # For Clearance
pygame.draw.polygon(display_surface, RED, [(460,25),(460,225),(510,125)])
pygame.draw.polygon(display_surface, GREEN, [(300,45),(231,85),(231,165),(300,205),(369,165),(369,85)]) # For Clearance
pygame.draw.polygon(display_surface, RED, [(300,50),(235,87),(235,162),(300,200),(365,163),(365,88)])
pygame.display.update()

# pygame.draw.rect(display_surface, RED, (100*5,0*5,50*5,100*5))
# pygame.draw.rect(display_surface, RED, (100*5,150*5,50*5,100*5))
# pygame.draw.polygon(display_surface, RED, [(460*5,25*5),(460*5,225*5),(510*5,125*5)])
# pygame.draw.polygon(display_surface, RED, [(300*5,50*5),(235*5,87*5),(235*5,162*5),(300*5,200*5),(365*5,163*5),(365*5,88*5)])
# pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


