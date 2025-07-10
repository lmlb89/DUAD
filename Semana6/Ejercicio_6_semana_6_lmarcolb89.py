# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sorting_phrase():
    phrase = "this-is-a-random-list-of-words-like-resume-company-position-that-we-need-to-sort-alphabetically"
    new_phrase = phrase.split("-")
    new_phrase.sort()
    final = ' '.join(new_phrase)
    return print(final)

sorting_phrase()
