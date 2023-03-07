from pokemon import *
from random import choice
from data import GENERATION_index,gen

def get_pokemon(id, shiny):
    return Pokemon(id, shiny).get_attributes()

TYPES_SPRITE={
    'normal': 50,
    'fighting': 100,
    'flying': 150,
    'poison': 200,
    'ground': 250,
    'rock': 300,
    'bug': 350,
    'ghost': 400,
    'steel': 450,
    'fire': 550,
    'water': 600,
    'grass': 650,
    'electric': 700,
    'psychic': 750,
    'ice': 800,
    'dragon': 850,
    'dark': 900,
    'fairy': 950,
}

def get_type_sprite(type):
    pos= (0,TYPES_SPRITE[type])
    return pos

random_pokemon= get_pokemon(3, False)

print(random_pokemon)

