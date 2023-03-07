from data import *
from random import choice

ID= choice(range(1, 107))
language= "english"

class Pokemon:
    def __init__(self, id, language, shiny):
        self.id= id
        self.language= language
        self.shiny= shiny
        self.name= get_pokemon(id, language, shiny)["name"]
        self.type= get_pokemon(id, language, shiny)["type"]
        self.stats= get_pokemon(id, language, shiny)["stats"]
        self.sprites= get_pokemon(id, language, shiny)["sprites"]
        self.hp= self.stats["HP"]
        self.attack= self.stats["Attack"]
        self.defense= self.stats["Defense"]
        self.sp_attack= self.stats["Sp. Attack"]
        self.sp_defense= self.stats["Sp. Defense"]
        self.speed= self.stats["Speed"]
        self.front= self.sprites["front"]
        self.front2= self.sprites["front2"]
        self.back= self.sprites["back"]
        self.description= PKMN_descriptions[str(id+GENERATION_index[gen]+1)]
        self.height= PKMN_height_weight[str(id+GENERATION_index[gen]+1)]["height"]
        self.weight= PKMN_height_weight[str(id+GENERATION_index[gen]+1)]["weight"]
        self.move_set= PKMN_move_set[str(id+GENERATION_index[gen]+1)]

    def __getattribute__(self, name):
        if name == "HP":
            return self.stats["HP"]
        elif name == "Attack":
            return self.stats["Attack"]
        elif name == "Defense":
            return self.stats["Defense"]
        elif name == "Sp. Attack":
            return self.stats["Sp. Attack"]
        elif name == "Sp. Defense":
            return self.stats["Sp. Defense"]
        elif name == "Speed":
            return self.stats["Speed"]
        elif name == "front":
            return self.sprites["front"]
        elif name == "front2":
            return self.sprites["front2"]
        elif name == "back":
            return self.sprites["back"] 
        elif name == "description":
            return PKMN_descriptions[str(self.id+GENERATION_index[gen]+1)]
        elif name == "height":
            return PKMN_height_weight[str(self.id+GENERATION_index[gen]+1)]["height"]
        elif name == "weight":
            return PKMN_height_weight[str(self.id+GENERATION_index[gen]+1)]["weight"]
        elif name == "move_set":
            return PKMN_move_set[str(self.id+GENERATION_index[gen]+1)]
        else:
            return object.__getattribute__(self, name)

pokemon= Pokemon(ID, language, False)

print('-'*20)
print(pokemon.id)
print(pokemon.id + GENERATION_index[gen])
print('-'*20)
print(pokemon.name)
print(pokemon.type)
print('-'*20)
print(pokemon.hp)
print(pokemon.attack)
print(pokemon.defense)
print(pokemon.sp_attack)
print(pokemon.sp_defense)
print('-'*20)
print(pokemon.description)
print(pokemon.move_set)
print('-'*20)