import json

def get_data(name):
    with open("json/"+f"{name}.json") as f:
        data = json.load(f)
    return data


def dump_data(name, data):
    with open("json/"+f"{name}.json", 'w') as f:
        json.dump(data, f, indent=4)

pokedex_all= get_data("pokedex_all")

pokedex_GEN1 = pokedex_all[:151]
pokedex_GEN2= pokedex_all[151:251]
pokedex_GEN3= pokedex_all[251:386]
pokedex_GEN4= pokedex_all[386:493]
pokedex_GEN5= pokedex_all[493:649]
pokedex_GEN6= pokedex_all[649:721]
pokedex_GEN7= pokedex_all[721:809]
pokedex_GEN8= pokedex_all[809:898]

