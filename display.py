from colors import COLORS
import pygame
import pokemon
import os

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

DISPLAYSURF= pygame.display.set_mode((800, 600))
PKMN_SPRITE_WINDOW= pygame.Rect(0, 0, 400, 400)
PKMN_DESCRIPTION_WINDOW= pygame.Rect(400, 0, 400, 400)
NEXT_PKMN_BUTTON= pygame.Rect(0, 400, 400, 200)
PREV_PKMN_BUTTON= pygame.Rect(400, 400, 400, 200)
pygame.display.set_caption("Pokemon")

def display_PKMN_info():
    DISPLAYSURF.fill(THEME['BACKGROUND'])
    DISPLAYSURF.blit(PKMN_SPRITE_WINDOW, (0, 0))
    PKMN_SPRITE_WINDOW.fill(THEME['BORDER'])
    DISPLAYSURF.blit(PKMN_DESCRIPTION_WINDOW, (400, 0))
    PKMN_DESCRIPTION_WINDOW.fill(THEME['BORDER'])
    DISPLAYSURF.blit(NEXT_PKMN_BUTTON, (0, 400))
    NEXT_PKMN_BUTTON.fill(THEME['BORDER'])
    DISPLAYSURF.blit(PREV_PKMN_BUTTON, (400, 400))
    PREV_PKMN_BUTTON.fill(THEME['BORDER'])

