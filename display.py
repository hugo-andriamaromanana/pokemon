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
PKMN_SPRITE_SURF = pygame.Surface((200, 200))
PKMN_ID_SURF = pygame.Surface((400, 100))
TYPE1_SURF = pygame.Surface((100, 50))
TYPE2_SURF = pygame.Surface((100, 50))
PKMN_DESCRIPTION_SURF = pygame.Surface((700, 100))
BASE_STATS_SURF = pygame.Surface((200, 350))
HEIGHT_WEIGHT_SURF = pygame.Surface((200, 150))
ACTUAL_DESCRIPTION_SURF = pygame.Surface((575, 80))
TRANSPARENT_BAR = pygame.Surface((800, 110), pygame.SRCALPHA)
TRANSPARENT_BAR = TRANSPARENT_BAR.convert_alpha()

NEXT_PKMN_BUTTON = pygame.Rect(0, 400, 400, 200)
PREV_PKMN_BUTTON = pygame.Rect(400, 400, 400, 200)
DARK_BLUE_BAR = pygame.Surface((25, 70))

pygame.display.set_caption("Pokemon")


def display_PKMN_info(random_pokemon):

    type_IMG = pygame.image.load(os.path.join('type_sprites', 'type.png'))
    current_sprite = pygame.image.load(random_pokemon['sprites']['front'])
    current_sprite = pygame.transform.scale(current_sprite, (200, 200))
    type_1 = type_IMG.subsurface(get_type_sprite(random_pokemon['type'][0]))
    type_1 = pygame.transform.scale(type_1, (90, 40))
    if len(random_pokemon['type']) == 2:
        type_2 = type_IMG.subsurface(
            get_type_sprite(random_pokemon['type'][1]))
        type_2 = pygame.transform.scale(type_2, (90, 40))

    TOP_WINDOW.fill(THEME['BACKGROUND'])

    DISPLAYSURF.blit(TOP_WINDOW, (0, 0))
    BOTTOM_WINDOW.fill(COLORS['GREY'])

    DISPLAYSURF.blit(BOTTOM_WINDOW, (0, 400))
    TOP_BORDER_SURF.fill(COLORS['BEIGE2'])

    PKMN_ID_SURF.fill(COLORS['BEIGE'])
    PKMN_ID_SURF.blit(THEME['FONTS']['DEFAULT'].render(
        (f"{random_pokemon['id']}. {random_pokemon['name']}".upper()), False, COLORS['BLACK']), (60, 40))
    DISPLAYSURF.blit(PKMN_ID_SURF, (350, 70))

    PKMN_DESCRIPTION_SURF.fill(COLORS['LIGHT_BLUE'])
    DISPLAYSURF.blit(PKMN_DESCRIPTION_SURF, (50, 290))
    DISPLAYSURF.blit(ACTUAL_DESCRIPTION_SURF, (110, 300))
    ACTUAL_DESCRIPTION_SURF.fill(COLORS['LESS_BEIGE'])

    DISPLAYSURF.blit(TRANSPARENT_BAR, (0, 175))
    TRANSPARENT_BAR.fill(COLORS['CLOUD'])

    DISPLAYSURF.blit(TOP_BORDER_SURF, (0, 0))
    PKMN_SPRITE_SURF.fill(COLORS['LESS_WHITE'])

    DISPLAYSURF.blit(PKMN_SPRITE_SURF, (50, 75))
    PKMN_SPRITE_SURF.fill(COLORS['LESS_WHITE'])

    DISPLAYSURF.blit(DARK_BLUE_BAR, (65, 305))
    DISPLAYSURF.blit(DARK_BLUE_BAR, (710, 305))
    DARK_BLUE_BAR.fill(COLORS['DARK_BLUE'])
    DISPLAYSURF.blit(current_sprite, (50, 75))

    DISPLAYSURF.blit(type_1, (450, 180))
    if len(random_pokemon['type']) > 1:
        DISPLAYSURF.blit(type_2, (545, 180))
    # BASE_STATS_SURF.fill(COLORS['RED'])
    # DISPLAYSURF.blit(BASE_STATS_SURF, (230,230 ))
    # HEIGHT_WEIGHT_SURF.fill(COLORS['BLACK'])
    DISPLAYSURF.blit(THEME['FONTS']['DEFAULT'].render(
        'HW', False, COLORS['BLACK']), (450, 230))
    DISPLAYSURF.blit(THEME['FONTS']['DEFAULT'].render(
        'WT', False, COLORS['BLACK']), (450, 260))
    DISPLAYSURF.blit(THEME['FONTS']['DEFAULT'].render(
        f"{random_pokemon['height']}\"", False, COLORS['BLACK']), (520, 230))
    DISPLAYSURF.blit(THEME['FONTS']['DEFAULT'].render(
        f"{random_pokemon['weight']} lbs", False, COLORS['BLACK']), (520, 260))

    DISPLAYSURF.blit(THEME['FONTS']['SMOL'].render(
        random_pokemon['description'][:65], True, COLORS['BLACK']), (120, 310))
    if len(random_pokemon['description']) > 65:
        DISPLAYSURF.blit(THEME['FONTS']['SMOL'].render(
            random_pokemon['description'][65:130], True, COLORS['BLACK']), (120, 330))
        if len(random_pokemon['description']) > 130:
            DISPLAYSURF.blit(THEME['FONTS']['SMOL'].render(
                random_pokemon['description'][130:], True, COLORS['BLACK']), (120, 350))
