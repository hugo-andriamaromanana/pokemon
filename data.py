import json
import os

def get_data(name):
    with open("json/"+f"{name}.json") as f:
        data = json.load(f)
    return data

def dump_data(name, data):
    with open("json/"+f"{name}.json", "w") as f:
        json.dump(data, f, indent=4)

def convert_to_dict(data):
    new_data = {}
    for i in range(len(data)):
        new_data[str(i)] = data[i]
    return new_data

POKEDEX_ALL= get_data("pokedex")
gen="4"

GENERATION={
    "1": POKEDEX_ALL[0:151],
    "2": POKEDEX_ALL[151:251],
    "3": POKEDEX_ALL[251:386],
    "4": POKEDEX_ALL[386:493],
    "all": POKEDEX_ALL
}

GENERATION_index={
    "1": 0,
    "2": 151,
    "3": 251,
    "4": 386,
    "all": 0
}
POKEDEX= GENERATION[gen]

POKEDEX= convert_to_dict(POKEDEX)

def get_pokemon(id, language,shiny):
    if shiny:
        path={
            "front": os.path.join("pokemon_sprites", "shiny", f"{id+GENERATION_index[gen]}.png"),
            "front2": os.path.join("pokemon_sprites", "shiny", "frame2", f"{id+GENERATION_index[gen]}.png"),
            "back": os.path.join("pokemon_sprites", "shiny", "back", f"{id+GENERATION_index[gen]}.png"),
            }
    else:
        path={
            "front": os.path.join("pokemon_sprites", f"{id+GENERATION_index[gen]}.png"),
            "front2": os.path.join("pokemon_sprites", "frame2", f"{id+GENERATION_index[gen]}.png"),
            "back": os.path.join("pokemon_sprites", "back", f"{id+GENERATION_index[gen]}.png"),
            }
    return {
            "name": POKEDEX[str(id)]['name'][language],
            "type": POKEDEX[str(id)]['type'],
            "stats": POKEDEX[str(id)]["base"],
            "sprites": path
        }

PKMN_descriptions= get_data("descriptions")
PKMN_height_weight= get_data("height_weight")
PKMN_move_set= get_data("move_set")
move_data= get_data("move_data")