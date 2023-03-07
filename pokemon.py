from data import get_pokemon
from random import choice

ID= choice(range(1, 152))

class Pokemon:
    def __init__(self, id, shiny):
        self.__id= id
        self.__shiny= shiny
        self.__data= get_pokemon(self.__id, self.__shiny)
        self.__name= self.__data["name"]
        self.__type= self.__data["type"]
        self.__stats= self.__data["stats"]
        self.__sprites= self.__data["sprites"]
        self.__front= self.__sprites["front"]
        self.__front2= self.__sprites["front2"]
        self.__back= self.__sprites["back"]
        self.__description= self.__data["description"]
        self.__height= self.__data["height"]
        self.__weight= self.__data["weight"]
        self.__move_set= self.__data["move_set"]

    def get_attributes(self):
        return {
            "name": self.__name,
            "type": self.__type,
            "stats": self.__stats,
            "sprites": self.__sprites,
            "move_set": self.__move_set,
            "height": self.__height,
            "weight": self.__weight,
            "description": self.__description
        }
    
pokemon1= Pokemon(ID, True)

def pretty_print(data):
    for key, value in data.items():
        print('-' * 20)
        print(key, ":", value)

pretty_print(pokemon1.get_attributes())