from colors import COLORS
from pyagmekeys import pygame
import os

THEME = {
        'BACKGROUND': COLORS['WEIRD_GREEN'],
        'BORDER': COLORS['WEIRD_GREY'],
        'FONTS': {
            'SMOL': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 20),
            'DEFAULT': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 30),
            'BIG': pygame.font.Font(os.path.join('fonts', 'Retro_Gaming.ttf'), 80)
        }
    }