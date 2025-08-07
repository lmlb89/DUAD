# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def lowercase_and_uppercase_count():
    text = "In here we are mixing both Uppercase and Lowercase for PRACTICING purposes only"
    lower=0
    upper=0
    for i in text:
      if i.islower():
        lower+=1
      if i.isupper():
        upper+=1
    print("Lowercase count is:",lower)
    print("Uppercase count is:",upper)

lowercase_and_uppercase_count()