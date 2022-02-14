'''Realizar un programa que solicite números enteros al usuario. El programa
debe terminar cuando el usuario introduzca -1. Al final del programa se nos 
informará de la suma de todos los números introducidos por el usuario (menos el
-1 que nos servirá para salir) y de si hay algún número par o no entre 
los introducidos por el usuario.'''
num=0
suma=int(0)
par=True
while num!=-1:
    num=int(input("Introduce números enteros. Cuando quieras parar introduce -1: "))
    if num%2==0:
        par=False
    if num!=-1:
        suma=suma+num
print("La suma de todos los números es: "+str(suma))
if par==False:
    print("Hay algún número par")
    