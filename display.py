from colors import COLORS
import pygame
import os
from display_functions import *

pygame.init()
pygame.font.init()

THEME = {
    'BACKGROUND': COLORS['WEIRD_GREEN'],
    'BORDER': COLORS['WEIRD_GREY'],
    'FONTS': {
        'SMOL': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 20),
        'DEFAULT': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 30),
        'BIG': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 80)
    }
}

DISPLAYSURF = pygame.display.set_mode((800, 600))

TOP_WINDOW = pygame.Surface((800, 400))
BOTTOM_WINDOW = pygame.Surface((800, 200))

TOP_BORDER_SURF = pygame.Surface((800, 50))
PKMN_SPRITE_SURF = pygame.Surface((250, 250))
PKMN_ID_SURF = pygame.Surface((400, 100))
TYPE1_SURF = pygame.Surface((100, 50))
TYPE2_SURF = pygame.Surface((100, 50))
PKMN_DESCRIPTION_SURF = pygame.Surface((800, 250))
BASE_STATS_SURF = pygame.Surface((200, 350))
HEIGHT_WEIGHT_SURF = pygame.Surface((200, 150))

NEXT_PKMN_BUTTON = pygame.Rect(0, 400, 400, 200)
PREV_PKMN_BUTTON = pygame.Rect(400, 400, 400, 200)

pygame.display.set_caption("Pokemon")


def display_PKMN_info():
    type_IMG = os.path.join('type_sprites', 'type.png')
    TOP_WINDOW.fill(THEME['BACKGROUND'])
    DISPLAYSURF.blit(TOP_WINDOW, (0, 0))
    BOTTOM_WINDOW.fill(COLORS['GREY'])
    DISPLAYSURF.blit(BOTTOM_WINDOW, (0, 400))

    TOP_BORDER_SURF.fill(THEME['BORDER'])
    DISPLAYSURF.blit(TOP_BORDER_SURF, (0, 0))
    PKMN_SPRITE_SURF.fill(COLORS['WHITE'])
    DISPLAYSURF.blit(PKMN_SPRITE_SURF, (20, 75))
    PKMN_SPRITE_SURF.fill(COLORS['WHITE'])
    PKMN_ID_SURF.fill(COLORS['BEIGE'])
    DISPLAYSURF.blit(PKMN_ID_SURF, (370, 70))
    DISPLAYSURF.blit(pygame.image.load(type_IMG).subsurface(get_type_sprite(random_pokemon['type'][0])), (450, 180))
    if len(random_pokemon['type']) > 1:
        DISPLAYSURF.blit(pygame.image.load(type_IMG).subsurface(get_type_sprite(random_pokemon['type'][1])), (530, 180))
    # TYPE_SURF.fill(COLORS['PURPLE'])
    # DISPLAYSURF.blit(TYPE_SURF, (300, 180))
    # PKMN_DESCRIPTION_SURF.fill(COLORS['BLUE'])
    # DISPLAYSURF.blit(PKMN_DESCRIPTION_SURF, (0, 200))
    # BASE_STATS_SURF.fill(COLORS['RED'])
    # DISPLAYSURF.blit(BASE_STATS_SURF, (230,230 ))
    # HEIGHT_WEIGHT_SURF.fill(COLORS['BLACK'])
