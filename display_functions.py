from pokemon import *
from random import choice
from data import gen


def get_pokemon(id, shiny):
    return Pokemon(id, shiny).get_attributes()


TYPES_SPRITE = {
    'Normal': [0, 0, 64, 28],
    'Fighting': [0, 28, 64, 28],
    'Flying': [0, 56, 64, 28],
    'Poison': [0, 84, 64, 28],
    'Ground': [0, 112, 64, 28],
    'Rock': [0, 140, 64, 28],
    'Bug': [0, 168, 64, 28],
    'Ghost': [0, 196, 64, 28],
    'Steel': [0, 224, 64, 28],
    '???': [0, 252, 64, 28],
    'Fire': [0, 280, 64, 28],
    'Water': [0, 308, 64, 28],
    'Grass': [0, 336, 64, 28],
    'Electric': [0, 364, 64, 28],
    'Psychic': [0, 392, 64, 28],
    'Ice': [0, 420, 64, 28],
    'Dragon': [0, 448, 64, 28],
    'Dark': [0, 476, 64, 28],
    'Fairy': [0, 504, 64, 28]
}


def get_type_sprite(type):
    return TYPES_SPRITE[type]


ID = choice(range(GENERATION[gen][0], GENERATION[gen][1]))

random_pokemon = Pokemon(ID, False).get_attributes()
