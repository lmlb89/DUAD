# 1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


def open_and_print_file_per_line(path):
	with open(path) as file:
		for line in file.readlines():
			print(f'Line: {line}')

def sort_and_save_songs(input_path, output_path):
    with open(input_path) as file:
        songs = sorted(file.readlines(), key=lambda x: x.lower())
    
    with open(output_path, 'w') as file:
        file.writelines(songs)
    print(f"Here is the sorted list: {songs}")
    print(f"Sorted songs have been saved to: {output_path}")

open_and_print_file_per_line("C:\\Users\\Marcolopez\\Documents\\Songs.txt")

sort_and_save_songs("C:\\Users\\Marcolopez\\Documents\\Songs.txt", "C:\\Users\\Marcolopez\\Documents\\Songs_final.txt")