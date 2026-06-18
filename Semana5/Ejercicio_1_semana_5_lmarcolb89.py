
#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#       1. Ejemplos:
#       2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
#       `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
#       Hay casos
#       en los
#       que la
#       iteracion por
#       indice es
#       muy util



first_list = ["This ", "an ", "of ", "different ", "that ", "combined ", "look ", "one "]
second_list = ["is ", "example ", "two ", "lists ", "are ", "and ", "like ", "which is pretty cool."] 


combined_list = []
for i in range(len(first_list)):
    combined_list.append(first_list[i] + second_list[i])
sentence = ''.join(combined_list)

print(sentence)