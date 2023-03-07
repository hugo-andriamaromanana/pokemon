import json
import os

def get_data(name):
    path= os.path.join("json", f"{name}.json")
    with open(path, "r") as f:
        data = json.load(f)
    return data

def dump_data(name, data):
    path= os.path.join("json", f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

POKEDEX_ALL= get_data("pokedex")
gen="4"

GENERATION={
    "1": [0,151],
    "2": [151,251],
    "3": [251,387],
    "4": [386,493],
    "all": [0, 493]
}

GENERATION_index={
    "1": 0,
    "2": 151,
    "3": 251,
    "4": 386,
    "all": 0
}

def get_pokedex(gen):
    if gen=="all":
        return POKEDEX_ALL
    else:
        return {str(i): POKEDEX_ALL[str(i)] for i in range(GENERATION[gen][0], GENERATION[gen][1])}

POKEDEX= get_pokedex(gen)
PKMN_descriptions= get_data("descriptions")
PKMN_height_weight= get_data("height_weight")
PKMN_move_set= get_data("move_set")

def get_pokemon(id, shiny):
    if shiny:
        path={
            "front": os.path.join("pokemon_sprites", "shiny", f"{id+GENERATION_index[gen]+1}.png"),
            "front2": os.path.join("pokemon_sprites", "shiny", "frame2", f"{id+GENERATION_index[gen]+1}.png"),
            "back": os.path.join("pokemon_sprites", "shiny", "back", f"{id+GENERATION_index[gen]+1}.png"),
            }
    else:
        path={
            "front": os.path.join("pokemon_sprites", f"{id+GENERATION_index[gen]+1}.png"),
            "front2": os.path.join("pokemon_sprites", "frame2", f"{id+GENERATION_index[gen]+1}.png"),
            "back": os.path.join("pokemon_sprites", "back", f"{id+GENERATION_index[gen]+1}.png"),
            }
    return {
            "name": POKEDEX[str(id+GENERATION_index[gen])]['name']["english"],
            "type": POKEDEX[str(id+GENERATION_index[gen])]['type'],
            "stats": POKEDEX[str(id+GENERATION_index[gen])]["base"],
            "description": PKMN_descriptions[str(id+GENERATION_index[gen]+1)],
            "height": PKMN_height_weight[str(id+GENERATION_index[gen]+1)]["height"],
            "weight": PKMN_height_weight[str(id+GENERATION_index[gen]+1)]["weight"],
            "move_set": PKMN_move_set[str(id+GENERATION_index[gen]+1)],
            "sprites": path
        }


move_data= get_data("move_data")
