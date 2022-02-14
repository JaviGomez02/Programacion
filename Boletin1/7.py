# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
import math
num = int(input("Introduce un número: "))
raizCuad = str(math.sqrt(num))
raizCubica = str(num**(1/3))
print('La raíz cuadrada es ' + raizCuad)
print('La raíz cúbica es ' + raizCubica)
