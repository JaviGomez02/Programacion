#Ejercicio 1
def minusculas(letra):
    if ord(letra)>=97 and ord(letra)<=122:
        return True
    else:
        return False

def mayusculas(letra):
    if ord(letra)>=66 and ord(letra)<=90:
        return True
    else:
        return False

def charactersInString(cadena, letra):
    contador=0
    if minusculas(letra):
        suma=-32
    else:
        suma=32
    for i in range (len(cadena)):
        if ord(cadena[i])==ord(letra) or ord(cadena[1])==ord(letra)+suma: 
            contador=contador+1
    return contador

# cadena=input("Introduce una cadena: ")
# letra=input("Introduce un carácter: ")
# print(charactersInString(cadena, letra))

#Ejercicio 2

def lowCaseInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if minusculas(cadena[i])==True:
            contador+=1
    return contador
# print(lowCaseInString("Hola Soy Javi"))

#Ejercicio 3

def upperCaseInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if mayusculas(cadena[i])==True:
            contador+=1
    return contador


#Ejercicio 4

def numberInString(cadena):
    contador=0
    numeros=["1","2","3","4","5","6","7","8","9"]
    for i in range(len(cadena)):
        if cadena[i] in numeros:
            contador+=1
    return contador

#Ejercicio 7
def ejercicio7(cadena, palabraBuscar, palabraNueva):
    array=[]
    cadenaAux=""
    for i in range (len(cadena)):
        if cadena[i]!=" ":
            cadenaAux+=cadena[i]
        else:
            array.append(cadenaAux)
            cadenaAux=""
    array.append(cadenaAux)

    for i in range(len(array)):
        if array[i]==palabraBuscar:
            array[i]=palabraNueva   
    return array
print (ejercicio7("Mi perro es grande", "perro", "gato"))


#Ejercicio 8
def numVocales(cadena):
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    contador=0
    for i in range(len(vocales)):
        if vocales[i] in cadena:
            contador+=1
    return contador


#Ejercicio 9
def ejercicio9(cadena):
    consonantes=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z" ]
    vocales=["a","e","i","o","u"]
    array=[]
    for i in range(len(cadena)):
        if cadena[i] in consonantes:
            array.append(cadena[i])
    for i in range(len(cadena)):
        if cadena[i] in vocales:
            array.append(cadena[i])
    return array

print(ejercicio9("me llamo javi"))

#Ejercicio 10


