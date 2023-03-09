import json
import os


def get_data(name):
    path = os.path.join("json", f"{name}.json")
    with open(path, "r") as f:
        data = json.load(f)
    return data


def dump_data(name, data):
    path = os.path.join("json", f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


POKEDEX_ALL = get_data("pokedex")
gen = "1"

GENERATION = {
    "1": [1, 151],
    "2": [151, 251],
    "3": [251, 386],
    "4": [386, 494],
    "all": [1, 494]
}

GENERATION_index = {
    "1": 0,
    "2": 151,
    "3": 251,
    "4": 386,
    "all": 0
}


def get_pokedex(gen):
    if gen == "all":
        return POKEDEX_ALL
    else:
        return {str(i): POKEDEX_ALL[str(i)] for i in range(GENERATION[gen][0], GENERATION[gen][1])}


POKEDEX = get_pokedex(gen)
PKMN_descriptions = get_data("descriptions")
PKMN_height_weight = get_data("height_weight")
PKMN_move_set = get_data("move_set")


def pretty_print(data):
    for key, value in data.items():
        print('-' * 20)
        print(key, ":", value)


def get_pokemon(id, shiny):
    if shiny:
        path = {
            "front": os.path.join("pokemon_sprites", "shiny", f"{id}.png"),
            "front2": os.path.join("pokemon_sprites", "shiny", "frame2", f"{id}.png"),
            "back": os.path.join("pokemon_sprites", "shiny", "back", f"{id}.png"),
        }
    else:
        path = {
            "front": os.path.join("pokemon_sprites", f"{id}.png"),
            "front2": os.path.join("pokemon_sprites", "frame2", f"{id}.png"),
            "back": os.path.join("pokemon_sprites", "back", f"{id}.png"),
        }
    return {
        "name": POKEDEX[str(id)]['name']["english"],
        "type": POKEDEX[str(id)]['type'],
        "stats": POKEDEX[str(id)]["base"],
        "description": PKMN_descriptions[str(id)],
        "height": PKMN_height_weight[str(id)]["height"],
        "weight": PKMN_height_weight[str(id)]["weight"],
        "move_set": PKMN_move_set[str(id)],
        "sprites": path
    }


move_data = get_data("move_data")
