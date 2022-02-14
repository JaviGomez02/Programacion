#Ejercicio 1
# from random import uniform
# lista=[]
# for i in range(0,100):
#     numero=int(uniform(0,100))
#     lista.append(numero)
def numeroMax(lista):
    maximo=0
    for i in lista:
        if i>maximo:
            maximo=i
    return maximo

def numeroMin(lista):
    minimo=9999
    for i in lista:
        if i<minimo:
            minimo=i
    return minimo

def sumaTotal(lista):
    suma=0
    for i in lista:
        suma=suma+i
    return suma

def mediaNumeros(lista):
    media=sumaTotal(lista)/100
    return media

def todosNumeros(lista):
    return lista

def cambiarNumero(lista):
    numeroCambiar=int(input("¿Qué número quieres sustituir? "))
    numeroNuevo=int(input("¿Qué número quieres añadir? "))
    for i in range(len(lista)):
        if lista[i]==numeroCambiar:
            lista[i]=numeroNuevo
    return lista
#
#
# print("1. Conocer el mayor de los números")
# print("2. Conocer el menor de los números")
# print("3. Obtener la suma de todos los números")
# print("4. Obtener la media de ellos números")
# print("5. Sustituir el valor de un elemento por otro número introducido por teclado")
# print("6. Mostrar todos los números.")
# opcion=0
#
# while opcion!=-1 and opcion<=6:
#     opcion=int(input("¿Qué quieres hacer? Introduce un número del 1 al 6; Introduce -1 para acabar el programa:  "))
#
#     if opcion==1:
#         print("El número máximo de la lista es: " + str(numeroMax(lista)))
#     elif opcion==2:
#         print("El número mínimo de la lista es: " + str(numeroMin(lista)))
#     elif opcion==3:
#         print("La suma de todos los números es: " + str(sumaTotal(lista)))
#     elif opcion==4:
#         print("La media de todos los números es: " + str(mediaNumeros(lista)))   
#     elif opcion==5:
#         print(lista)
#         print(cambiarNumero(lista))
#     elif opcion==6:
#         print(todosNumeros(lista))
 

# Ejercicio 2
# lista=[]
# for i in range(0,10):
#     numero=int(input("Introduce un número: "))
#     lista.append(numero)
# print(lista)
# listaNueva=[]
# for i in range(len(lista)):
#     if i<=9:
#         i=i-1
#     elif i==10:
#         i=i+9
#     listaNueva.append(lista[i])
# print(listaNueva)
#
#
# lista=[]
# for i in range(0,10):
#     numero=int(input("Introduce un número: "))
#     lista.append(numero)
# print(lista)
#
def mueveDerecha(listaNumeros):
    primerNumero=listaNumeros[len(listaNumeros)-1]
    posicion=len(listaNumeros)-2
    while posicion>=0:
        listaNumeros[posicion]=listaNumeros[posicion-1]
        posicion-=1
    listaNumeros[0]=primerNumero
    return listaNumeros
# print(mueveDerecha(lista))


#Ejercicio 3

# dia=1
# meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# meses2=["Abril", "Junio", "Septiembre", "Noviembre"]
# while dia>0:
#     dia=int(input("Introduce el día de la fecha: "))
#     while dia>31:
#         print("No existe ningún mes con más de 31 días")
#         dia=int(input("Introduce el día de la fecha: "))
#     mes=int(input("Introduce el mes de la fecha: "))
#     while mes<1 or mes>12:
#         print("Introduce un mes correcto")
#         mes=int(input("Introduce el mes de la fecha: "))
#     ano=int(input("Introduce el año de la fecha: "))
#
#     mes=meses[mes-1]
#     if mes=="Febrero" and dia>28:
#         print("Fecha incorrecta")
#     elif mes in meses2 and dia>30:
#         print("Fecha incorrecta")
#     else:
#         print("La fecha en formato largo es "+str(dia)+" de "+mes+" de "+str(ano))
        

#Ejercicio 4
def numeroPar(lista):
    pares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
    return pares

# numero=0

# lista=[]
# while numero>=0:
#     numero=int(input("Introduce un número: "))
#     if numero>=0:
#         lista.append(numero)
# print(lista)
# print("El número máximo es "+(numeroMax(lista)))
# print("Los números pares son: " (numeroPar(lista)))

#Ejercicio 5

def listaInvertida(lista):
    listaNueva=[]
    for i in range(len(lista)-1, -1, -1):
        listaNueva.append(lista[i])
    return listaNueva

print(listaInvertida(["Hola", "que", "tal"]))

#Ejercicio 6

def listaOrdenada(lista):
    listaNueva=[]
    return listaNueva
    
    

#Ejercicio 8

def primos(lista):
    listaPrimos=[]
    flag=True
    posicion=2
    for i in lista:
        while posicion!=i:
            if i%(posicion)==0:
                flag=0
            posicion+=1
        posicion=2
        if flag==True and i!=1:
            listaPrimos.append(i)
        flag=True
    return listaPrimos

def variasFunciones(lista):
    resultado=[]
    solucion=primos(lista)
    resultado.append(solucion)

    solucion=sumaTotal(lista)
    resultado.append(solucion)

    solucion=mediaNumeros(lista)
    resultado.append(solucion)
    return resultado
#
# lista=[]
# numero=0
# while numero>=0:
#     numero=int(input("Introduce un número: "))
#     if numero>=0:
#         lista.append(numero)
#
# print(variasFunciones(lista))

#Ejercicio 10


def binarioDecimal(lista):
    exponente=0
    numero=0
    for i in range(len(lista)-1, -1, -1):
        operacion=lista[i]*(2**exponente)
        exponente+=1
        numero=operacion+numero
    return numero

def decimalBinario(numero):
    operacion=[]
    resultado=[]
    operacion.append(1)
    while numero>1:
        numero=numero//2
        resto=numero%2
        operacion.append(resto)
    for i in range(len(operacion)-1, -1, -1):
        resultado.append(operacion[i])
    return resultado

# print(binarioDecimal([1,1,0,1,0,0,1]))

# print(decimalBinario(23))

#Ejercicio 11

def elementosComunes(lista1, lista2):
    listaNueva=[]
    for i in range(len(lista1)):
        if lista1[i] in lista2 and lista1[i] not in listaNueva:
            listaNueva.append(lista1[i])
    return listaNueva

# print(elementosComunes([1,3,6,4,3], [2,3,5,4,3]))

#Ejercicio 12

def conjuntos(lista1, lista2):
    listaNueva=[]
    for i in range (len(lista1)):
        if lista1[i] not in listaNueva:
            listaNueva.append(lista1[i])
    for i in range (len(lista2)):
        if lista2[i] not in listaNueva:
            listaNueva.append(lista2[i])
    return listaNueva

# print(conjuntos([1,2,3,4,5,6], [5,1,2,3,4,6]))

#Ejercicio 13

def nombres(lista, letra):
    listaNueva=[]
    for i in range (len(lista)):
        nombre=lista[i]
        if nombre[0]==letra:
            listaNueva.append(nombre)
    return listaNueva

# print(nombres(["Antonio", "Juan", "Alvaro"], ("A")))        
    
#Ejercicio 14
def cadenaMasLarga(lista):
    for i in range(len(lista)):
        cadena=lista[i]
        if len(cadena)>len(lista[i-1]):
            cadenaLarga=cadena
    return cadenaLarga

print(cadenaMasLarga(["aaa", "aaaaaaa", "eewwwwe", "ertergd", "urrt"]))












