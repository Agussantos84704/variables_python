
# CODE:6
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Almacenar el valor de cada operación realizada en las
  variables que usted creará con los siguientes nombres:
  suma, resta, multiplicacion, division, potencia

- Al final imprimir todos los resultados almacenados
  en esas variables
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio


numero_1 = float(input('Ingrese el primer numero decimal: '))

numero_2 = float(input('Ingrese el segundo numero decimal: '))

suma = numero_1 + numero_2

resta = numero_1 - numero_2

multiplicacion = numero_1 * numero_2

division = numero_1 / numero_2

potencia = numero_1 ** numero_2

print("Los resultados son: SUMA:", suma, "; RESTA: ", resta,"; MULTIPLICACION: ", multiplicacion, "; DIVISION: ", division, "; POTENCIA:", potencia,"... Finalizadas todas las operaciones.")
