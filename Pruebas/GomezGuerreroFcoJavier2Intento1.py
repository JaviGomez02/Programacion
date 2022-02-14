'''Crear función que reciba una cadena como parámetro y que devuelva si es una contraseña 
FUERTE (True) o DÉBIL (False). Se considera que una contraseña es fuerte si contiene 8 o más 
caracteres, y entre ellos al menos hay una mayúscula, una minúscula y un dígito.'''

'''
Función que recibe una cadena de texto, y dos argumentos: un valor inicial y un valor final.
La función debe recorrer todos los carácteres de la cadena, y devolver True si el código ascii de
alguno de esos caracteres está comprendido entre el valor inicial (incluyendo el valor inicial) y
el valor final (incluyendo el valor final).
Si se encuentra algún carácter que cumple la condición no se debe seguir mirando.
'''
def compruebaValoresAscii(cadena, vInicial, vFinal):
    

# Ejemplos de llamada a la función.
# Para ver si hay alguna mayúsculas
# print(compruebaValoresAscii("Inmaculada", 65, 90))
# print(compruebaValoresAscii("inmaculada", 65, 90))

''' Función de devuelve True si la cadena tiene más de 8 carácteres y al menos una mayúsucula, una
minúscula y un número.'''

def contrasennaFuerte(contrasenna):
   

# Ejemplos para ver si funciona.
# print(contrasennaFuerte("Inmaculada2"))
# print(contrasennaFuerte("Ilada2"))
# print(contrasennaFuerte("inmaculada2"))
# print(contrasennaFuerte("Inmaculada"))
# print(contrasennaFuerte("INMACULADA2"))
