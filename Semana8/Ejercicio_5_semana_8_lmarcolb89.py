# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
#    1. Debe leer el archivo para importar los Pokémones existentes.
#    2. Luego debe pedir la información del Pokémon a agregar.
#    3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def open_json_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)
        return data

def new_pokemon_info(path):
    pokemon_list = open_json_file(path)
    print("Enter new Pokemon details:")
    new_pokemon = {
        "name": {
            "english": input("English name: ").strip()
        },
        "type": [
            t.strip() for t in input("Type(s), comma-separated: ").split(',')
        ],
        "base": {
            "HP": int(input("HP: ")),
            "Attack": int(input("Attack: ")),
            "Defense": int(input("Defense: ")),
            "Sp. Attack": int(input("Sp. Attack: ")),
            "Sp. Defense": int(input("Sp. Defense: ")),
            "Speed": int(input("Speed: "))
        }
    }
    
    pokemon_list.append(new_pokemon)
    
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_list, file, indent=4)
    
        print(f"\nSuccessfully added {new_pokemon['name']['english']}!")
                    

new_pokemon_info("C:\\Users\\Marcolopez\\Documents\\pokemons.json")
    