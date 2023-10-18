
# CODE:9
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada nombre_completo_1
  para almacenar el primer nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre_completo_2
  para almacenar el primer nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una una variable llamada nombre
  para almacenar el nombre del hijo/a que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Cuando utilice la función split para dividir
  el nombre_completo_1, almacene los resultados
  en las variables llamadas nombre_1 y apellido_1
  Imprimir en consola el contenido de estas variables

- Cuando utilice la función split para dividir
  el nombre_completo_2, almacene los resultados
  en las variables llamadas nombre_2 y apellido_2
  Imprimir en consola el contenido de estas variables

- Crear una una variable llamada hijo
  para almacenar el nombre del hijo/a contenido en
  la variable nombre sumando/concatenando
  los apellidos almaecnados en apellido_1 y apellido_2
  Imprimir en consola el contenido de esta variable

'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

nombre_completo_1 = input('Ingrese el nombre completo de su padre por favor: ')

print (f'Muy bien, su padre es: {nombre_completo_1}')

nombre_completo_2 = input ('Ingrese el nombre completo de su madre por favor: ')

print (f'Excelente, tomamos a su madre como {nombre_completo_2}')

nombre = input('Ahora. Ingrese solamente su primer nombre por favor: ')

print(f'De acuerdo, {nombre}, si ese es tu nombre...')

nombre_1, apellido_1 = nombre_completo_1.split()

print(f'Y ya que usted ha ingresado a {apellido_1}, {nombre_1} como su padre...')

nombre_2, apellido_2 = nombre_completo_2.split()

print(f'Y también ha ingresado a {apellido_2}, {nombre_2} como su madre...')

hijo = nombre + ' ' + apellido_1 + ' ' + apellido_2

print(f'Entendemos que su nombre completo ha de ser {hijo}')





