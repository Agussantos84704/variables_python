
# CODE:4
# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ingrese tres palabras y arme un acrónimo con ellas
palabra_1 = str(input('Ingrese palabra 1:'))

palabra_2 = str(input('Ingrese palabra 2:'))

palabra_3 = str(input('Ingrese palabra 3:'))


# Alumno:
# Crear una variable llamada acronimo donde se 
# almacene la primera letra de cada palabra
# en el orden corespondiente

caracter_inicial_1 = palabra_1[0]

caracter_inicial_2 = palabra_2[0]

caracter_inicial_3 = palabra_3[0]


acronimo = caracter_inicial_1 + caracter_inicial_2 + caracter_inicial_3

# Imprimir la variable acronimo en pantalla

print("Entonces, las palabras enumeradas formarán el acronimo: ", caracter_inicial_1 + caracter_inicial_2 + caracter_inicial_3," Y así se nombrará.")