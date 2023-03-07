import pygame
from pygame.locals import *

def ESC_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True
