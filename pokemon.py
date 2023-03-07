from data import *
from random import choice

ID= choice(range(1, 107))
language= "english"

class Pokemon:
    def __init__(self, id, language, shiny):
        self.__id= id
        self.__language= language
        self.__shiny= shiny
        self.__data= get_pokemon(self.__id, self.__language, self.__shiny)
        self.__name= self.__data["name"]
        self.__type= self.__data["type"]
        self.__stats= self.__data["stats"]
        self.__sprites= self.__data["sprites"]
        self.__front= self.__sprites["front"]
        self.__front2= self.__sprites["front2"]
        self.__back= self.__sprites["back"]
        self.__description= PKMN_descriptions[str(self.__id)]
        self.__height= PKMN_height_weight[str(self.__id)]["height"]
        self.__weight= PKMN_height_weight[str(self.__id)]["weight"]
        self.__move_set= PKMN_move_set[str(self.__id)]

    def get_attributes(self):
        return {
            "name": self.__name,
            "type": self.__type,
            "stats": self.__stats,
            "sprites": self.__sprites,
            "front": self.__front,
            "front2": self.__front2,
            "back": self.__back,
            "move_set": self.__move_set,
            "description": self.__description,
            "height": self.__height,
            "weight": self.__weight
        }
    
pokemon1= Pokemon(ID, language, True)

def pretty_print(data):
    for key, value in data.items():
        print('-' * 20)
        print(key, ":", value)

pretty_print(pokemon1.get_attributes())