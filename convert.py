import json
import requests

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

POKEDEX=convert_to_dict(get_data("pokedex_all"))

def get_pokemon_description(pokemon_descriptions):
    for i in range(152, 494):
        url= f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
        response= requests.get(url)
        data= response.json()
        pokemon_descriptions[str(i)]=data["flavor_text_entries"][0]["flavor_text"]
    dump_data("pokemon_descriptions", pokemon_descriptions)


def remove_stuff(pokemon_descriptions):
    for i in range(1, 493):
        if pokemon_descriptions[str(i)] == '':
            pokemon_descriptions[str(i)]= 'No description available.'
    dump_data("pokemon_descriptions", pokemon_descriptions)

# pokemon_descriptions=get_data("pokemon_descriptions")
# get_pokemon_description(pokemon_descriptions)
# remove_stuff(get_data("pokemon_descriptions"))

def get_pokemon_height_weight(pokemon_height_weight):
    for i in range(1, 493):
        url= f"https://pokeapi.co/api/v2/pokemon/{i}/"
        response= requests.get(url)
        data= response.json()
        pokemon_height_weight[str(i)]={"height":data["height"], "weight":data["weight"]}
    dump_data("pokemon_height_weight", pokemon_height_weight)

pokemon_height_weight=get_data("pokemon_height_weight")    
get_pokemon_height_weight(pokemon_height_weight)