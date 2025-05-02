# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
#       Nombre
#       Género
#       Desarrollador
#       Clasificación ESRB
#              Ejemplo de archivo final:
#                        nombre,genero,desarrollador,clasificacion
#                        Grand Theft Auto IV,Accion,Rockstar Games,M
#                        The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
#                        Tony Hawk's Pro Skater 2,Deportes,Activision,T

import csv

def ask_for_game_info():
    games = []
    while True:
        name = input("Enter the game name: ")
        genre = input("Enter the game genre: ")
        developer = input("Enter the game creator: ")
        classification = input("Enter the game ESRB classification: ")
        games.append({"name": name, "genre": genre, "developer": developer, "classification": classification})
        print(f"Added {name}, {genre}, {developer}, {classification}, to the collection")
        
        another = input("Add another game? (y/n): ").lower()
        if another != 'y':
            break
    return games

def save_to_csv(games, filename=None):
    if not filename:
        filename = "game_collection.csv"
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'genre', 'developer', 'classification']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for game in games:
                writer.writerow(game)
            print(f"\nSuccessfully saved {len(games)} game(s) to {filename}")
    except Exception as error:
        print(f"\nError saving file: {error}")

def main():
    games = ask_for_game_info()
    if games:
        save_to_csv(games)
    else:
        print("No games were entered. File not created.")

if __name__ == "__main__":
    main()