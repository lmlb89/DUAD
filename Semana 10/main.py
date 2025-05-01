# Requerimientos

# Cree un programa tener tenga una interfaz por linea de comando (es decir, a base de `inputs` y `prints`). Este debe tener un menu que me permita accesar a todas las funciones (**deberá validar que se ingrese una opción del valida del menú**):

# 1. Ingresar información de `n` cantidad de estudiantes, *uno por uno*.
#    1. Cada estudiante debe incluir:
#        1. Nombre completo
#        2. Sección (ejemplo: *11B*)
#        3. Nota de español
#        4. Nota de inglés
#        5. Nota de sociales
#        6. Nota de ciencias
#    2. Deberá validar que las notas ingresadas sean validas (números de 0 a 100) y seguir pidiéndola hasta que sea valida.
# 2. Ver la información de todos los estudiantes ingresados.
# 3. Ver el top 3 de los estudiantes con la mejor nota promedio (*es decir, el promedio de su* `nota de español`+ `nota de inglés` + `nota de sociales` + `nota de ciencias`).
# 4. Ver la nota promedio entre las notas de todos los estudiantes (es decir, el promedio del `promedio de notas` *de cada uno*). 
# 5. Exportar todos los datos actuales a un archivo CSV.
# 6. Importar los datos de un archivo CSV previamente exportado.
#    1. Si no hay un archivo previamente exportado, debe de decírselo al usuario.

# Divida el proyecto en los siguientes módulos:

# `main`: tendrá el punto de entrada del programa.
#  `menu`: tendrá toda la lógica relacionada al menu de opciones.
# `actions`: tendrá toda la lógica de las acciones del menu, excepto las de exportar e importar datos.
# `data`: tendrá toda la lógica de exportación e importación de datos.

from menu import menu
from actions import (
    add_students,
    show_all_students,
    show_top_3,
    show_total_average,
)
from data import export_to_csv, import_from_csv

def main():
    students = []
    
    while True:
        choice = menu()
        
        if choice == 1:
            add_students(students)
        elif choice == 2:
            show_all_students(students)
        elif choice == 3:
            show_top_3(students)
        elif choice == 4:
            show_total_average(students)
        elif choice == 5:
            export_to_csv(students)
        elif choice == 6:
            students = import_from_csv()
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



