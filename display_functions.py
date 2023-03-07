from pokemon import *
from random import choice
from data import GENERATION_index,gen

def get_pokemon(id, shiny):
    return Pokemon(id, shiny).get_attributes()

TYPES_SPRITE={
    'Normal': 50,
    'Fighting': 100,
    'Flying': 150,
    'Poison': 200,
    'Ground': 250,
    'Rock': 300,
    'Bug': 350,
    'Ghost': 400,
    'Steel': 450,
    'Fire': 550,
    'Water': 600,
    'Grass': 650,
    'Electric': 700,
    'Psychic': 750,
    'Ice': 800,
    'Dragon': 850,
    'Dark': 900,
    'Fairy': 950,
}

def get_type_sprite(type):
    pos= (0,TYPES_SPRITE[type])
    return pos

random_pokemon= get_pokemon(3, False)

