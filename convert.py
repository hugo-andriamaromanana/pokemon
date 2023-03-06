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
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\f", " ")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\n", " ")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\r", " ")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\t", " ")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\v", " ")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e9", "E")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e8", "E")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e0", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e2", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e7", "C")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f4", "O")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f6", "O")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00fc", "U")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f9", "U")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e4", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f3", "O")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f1", "N")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00ed", "I")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00fa", "U")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e1", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f2", "O")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e3", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e6", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00df", "S")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f8", "O")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e5", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00e7", "C")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00f0", "D")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u2019", "'")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u2018", "'")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u201c", '"')
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u201d", '"')
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00ad", "-")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00c9", "E")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00c8", "E")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00c0", "A")
        pokemon_descriptions[str(i)]=pokemon_descriptions[str(i)].replace("\u00c2", "A")
    dump_data("pokemon_descriptions", pokemon_descriptions)

# pokemon_descriptions=get_data("pokemon_descriptions")
# get_pokemon_description(pokemon_descriptions)
remove_stuff(get_data("pokemon_descriptions"))