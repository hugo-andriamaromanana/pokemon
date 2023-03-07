# import json
# # import requests

# # def get_data(name):
# #     with open("json/"+f"{name}.json") as f:
# #         data = json.load(f)
# #     return data


# # def dump_data(name, data):
# #     with open("json/"+f"{name}.json", "w") as f:
# #         json.dump(data, f, indent=4)


# # def convert_to_dict(data):
# #     new_data = {}
# #     for i in range(len(data)):
# #         new_data[str(i)] = data[i]
# #     return new_data


# # POKEDEX = convert_to_dict(get_data("pokedex_all"))

# # def get_pokemon_description(pokemon_descriptions):
# #     for i in range(152, 494):
# #         url= f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
# #         response= requests.get(url)
# #         data= response.json()
# #         pokemon_descriptions[str(i)]=data["flavor_text_entries"][0]["flavor_text"]
# #     dump_data("pokemon_descriptions", pokemon_descriptions)


# # def remove_stuff(pokemon_descriptions):
# #     for i in range(1, 493):
# #         if pokemon_descriptions[str(i)] == '':
# #             pokemon_descriptions[str(i)]= 'No description available.'
# #     dump_data("pokemon_descriptions", pokemon_descriptions)

# # pokemon_descriptions=get_data("pokemon_descriptions")
# # get_pokemon_description(pokemon_descriptions)
# # remove_stuff(get_data("pokemon_descriptions"))

# # def get_pokemon_height_weight(pokemon_height_weight):
# #     for i in range(1, 493):
# #         url= f"https://pokeapi.co/api/v2/pokemon/{i}/"
# #         response= requests.get(url)
# #         data= response.json()
# #         pokemon_height_weight[str(i)]={"height":data["height"], "weight":data["weight"]}
# #         print(pokemon_height_weight)
# #     # dump_data("pokemon_height_weight", pokemon_height_weight)

# # pokemon_height_weight=get_data("pokemon_height_weight")
# # get_pokemon_height_weight(pokemon_height_weight)

# # def get_pokemon_moves(pokemon_moves):
# #     for i in range(1):
# #         url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
# #         response = requests.get(url)
# #         data = response.json()
# #         moves = []
# #         bruh = 5
# #         if len(data["moves"]) < 5:
# #             bruh = len(data["moves"])
# #         for j in range(1, bruh):
# #             moves.append(data["moves"][j]["move"]["name"])
# #             print(data["moves"][j]["move"])
# #         pokemon_moves[str(i)] = moves
# #         print(pokemon_moves)
#     # dump_data("pokemon_moves", pokemon_moves)

# # pokemon_moves = {}
# # get_pokemon_moves(pokemon_moves)

# # pokemon_moves = get_data("pokemon_moves")

# # def get_pokemon_moves_data(pokemon_moves_data):
# #     for i in range(1):
# #         url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
# #         response = requests.get(url)
# #         data = response.json()
# #         moves = []
# #         bruh = 5
# #         if len(data["moves"]) < 5:
# #             bruh = len(data["moves"])
# #         for j in range(1, bruh):
# #             moves.append(data["moves"][j]["move"])
# #             print(data["moves"][j]["move"])
# #         pokemon_moves_data[str(i)] = moves
# #     print(pokemon_moves_data)

# # pokemon_moves_data = get_data("pokemon_moves_data")
# # get_pokemon_moves_data(pokemon_moves_data)



# # def get_pokemon_moves_data(pokemon_moves_data):
# #     for i in range(1, 493):
# #         url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
# #         response = requests.get(url)
# #         data = response.json()
# #         moves = []
# #         bruh = 5
# #         if len(data["moves"]) < 5:
# #             bruh = len(data["moves"])
# #         for j in range(1, bruh):
# #             moves.append(data["moves"][j]["move"]["name"])
# #         pokemon_moves_data[str(i)] = moves
# #     dump_data("pokemon_moves_data", pokemon_moves_data)

# # pkmn_moves_data = get_data("pokemon_moves")

# # def create_unique_moves(pkmn_moves_data):
# #     unique_moves = {}
# #     for i in range(1, 493):
# #         bruh = 5
# #         if len(pkmn_moves_data[str(i)]) < 5:
# #             bruh = len(pkmn_moves_data[str(i)])
# #         for j in range(0, bruh):
# #             if pkmn_moves_data[str(i)][j] not in unique_moves:
# #                 unique_moves[pkmn_moves_data[str(i)][j]] = {}
# #     dump_data("unique_moves", unique_moves)

# # create_unique_moves(pkmn_moves_data)

# # def get_move_data(unique_moves):
# #     for i in unique_moves:
# #         url = f"https://pokeapi.co/api/v2/move/{i}/"
# #         response = requests.get(url)
# #         data = response.json()
# #         unique_moves[i] = {
# #             "accuracy": data["accuracy"],
# #             "power": data["power"],
# #             "pp": data["pp"],
# #             "type": data["type"]["name"],
# #             "damage_class": data["damage_class"]["name"],
# #             "effect_chance": data["effect_chance"],
# #             "effect_entries": data["effect_entries"][0]["effect"],
# #             "flavor_text_entries": data["flavor_text_entries"][0]["flavor_text"],
# #             "generation": data["generation"]["name"],
# #             "priority": data["priority"],
# #             "target": data["target"]["name"],
# #         }
# #     dump_data("unique_moves", unique_moves)

# # unique_moves = get_data("unique_moves")
# # get_move_data(unique_moves)

# import os

# def get_data(name):
#     path= os.path.join("json", f"{name}.json")
#     with open(path, "r") as f:
#         data = json.load(f)
#     return data

# def dump_data(name, data):
#     path= os.path.join("json", f"{name}.json")
#     with open(path, "w") as f:
#         json.dump(data, f, indent=4)

# def turn_to_dic(data):
#     new_data = {}
#     for i in data:
#         new_data[i["id"]] = i
#     return new_data

# poke_dex= get_data('pokedex')
# poke_dex= turn_to_dic(poke_dex)
# dump_data('pokedex', poke_dex)

