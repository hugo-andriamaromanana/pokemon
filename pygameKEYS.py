import pygame
from pygame.locals import *
from display import *


def ESC_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return False
    return True


def NEXT_PKMN_KEYDOWN(event):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        return True
    return False
