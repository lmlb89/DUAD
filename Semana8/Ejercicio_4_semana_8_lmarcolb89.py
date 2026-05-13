# Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
# Ejemplo de archivo final:
#       nombre	genero	desarrollador	clasificacion
#       Grand Theft Auto IV	Accion	Rockstar Games	M
#       The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
#       Tony Hawk's Pro Skater 2	Deportes	Activision	T


import csv

def ask_for_game_info():
    games = []
    while True:
        name = input("Enter the game name: ")
        genre = input("Enter the game genre: ")
        developer = input("Enter the game creator: ")
        classification = input("Enter the game ESRB classification: ")
        games.append({"name": name, "genre": genre, "developer": developer, "classification": classification})
        print(f"Added {name} {genre} {developer} {classification} to the collection")  # Spaces instead of commas
        
        another = input("Add another game? (y/n): ").lower()
        if another != 'y':
            break
    return games

def save_to_txt(games, filename=None):
    if not filename:
        filename = "game_collection.txt"
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as txtfile:
                writer = csv.DictWriter(txtfile, 
                            fieldnames=['name', 'genre', 'developer', 'classification'],
                            delimiter=' ',
                            quoting=csv.QUOTE_MINIMAL)
                writer.writeheader()
                for game in games:
                    writer.writerow(game)
                    print(f"Successfully saved {len(games)} game(s) to {filename}")
    except Exception as error:
        print(f"\nError saving file: {error}")

def main():
    games = ask_for_game_info()
    if games:
        save_to_txt(games)
    else:
        print("No games were entered. File not created.")

if __name__ == "__main__":
    main()