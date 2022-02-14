'''3. Un oficial de correos decide optimizar el trabajo de su oficina cortando todas 
las palabras de más de cinco letras a sólo cinco letras (e indicando que una palabra fue cortada con 
el agregado de una arroba). Además también elimina todos los espacios en blanco de más.
Por ejemplo, al texto » Llego mañana alrededor del mediodía » se transcribe como 
«Llego mañan@ alred@ del medio@».

Por otro lado cobra un valor para las palabras cortas y otro valor para las palabras largas 
(que deben ser cortadas).
Escribir una función que reciba un texto, la longitud máxima de las palabras (en el caso 
anterior eran 5 letras) y devuelva como resultado el texto del telegrama.

Extra:
Escribir una segunda función que devuelva el costo del texto. Esta función deberá recibir
 como argumento el costo de cada palabra corta, el costo de cada palabra larga y el 
 texto del telegrama, es decir, el texto ya cifrado.'''

 
 
## Función que recibe una cadena de texto y devuelve un array con cada uno de las palabras.
## Se deberá recorrer el array e ir guardando los caracteres, cuando encuentre un espacio
## se deberá ver si se ha guardado algún carácter (porque puede haber más de un espacio seguido
## y si hay algo guardado añadirlo al array y reiniciar la palabra guardada para que empiece a vacia.
## Revisar que se ha guardado la última palabra.

def creaArrayConPalabras(cadena):
    lista=[]
    cadenaNueva=""
    for i in range(len(cadena)):
        if cadena[i]!=" ":
            cadenaNueva=cadenaNueva+cadena[i]
        elif cadena[i]==" ":
            if cadenaNueva!="":
                lista.append(cadenaNueva)
                cadenaNueva=""
        if (i+1)==len(cadena):
            lista.append(cadenaNueva)
    return lista
 
# print(creaArrayConPalabras("hola    que     tal estas"))

## Función que recibe una cadena de texto que tendrá sólo una palabra y la longitud. La función
## debe devolver la misma palabra si la longitud de la palabra es menor o igual que la longitud
## que se pasa por parámetro. En el caso contrario debe devolver los caracteres que indican el tamaño
## pasado por argumento más el carácter @

def cortaPalabra(cadena, longitud):
    palabra=""
    for i in range(len(cadena)):
        if i<longitud:
            palabra=palabra+cadena[i]
    if len(cadena)>longitud:
        palabra=palabra+"@"
    return palabra

# print(cortaPalabra("holeeeeei", 4))




## Función que recibe una lista con palabras y una longitud y devuelve otra lista con las 
## palabras recortadas si se pasan de la longitud
def cortarPalabrasLista(lista, longitud):
    listaNueva=[]
    for i in range(len(lista)):
        listaNueva.append(cortaPalabra(lista[i], longitud))
    return listaNueva

# print(cortarPalabrasLista(creaArrayConPalabras("Hola que tal guapo"), 2))




## Función que recibe un array con palabras y devuelve una cadena con todas las palabras separadas
## por espacio, menos la última palabra que no deberá tener espacio al final.
def formaCadena(lista):
    cadena=""
    for i in range(len(lista)):
        cadena=cadena+lista[i]
        if i+1!=len(lista):
            cadena=cadena+" "
    return cadena

# print(formaCadena(["Hola", "como", "estas"]))


## Función que  recibe una cadena y una longitud y devuelve la cadena recortada a esa longitud.
def recorta(frase, tamanno):
    return formaCadena(cortarPalabrasLista(creaArrayConPalabras(frase), tamanno))
    
    


print(recorta(" Llego mañana alrededor  del mediodía ",5))
print(recorta(" Llego mañana alrededor  del mediodía",4))


## Función que recibe una cadena y devuelve True si el último carácter es @ y False en caso contrario.
def contieneFinal(cadena):
    resultado=False
    for i in range(len(cadena)):
        if i+1==len(cadena):
            if cadena[i]=="@":
                resultado=True
            elif cadena[i]!="@":
                resultado=False
        else:
            resultado=False
    return resultado

# print(contieneFinal("H@la que tal@"))
    

## Función que recibe una cadena cifrada, el precio de las palabras cortas y el precio de las largas 
## y debe devolver el precio de la cadena cifrada.

def precio(cadena, precioCorto, precioLargo):
    precioTotal=0
    listaNueva=creaArrayConPalabras(cadena)
    for i in range(len(listaNueva)):
        res=contieneFinal(listaNueva[i])
        if res==True:
            precioTotal=precioTotal+precioLargo
        else:
            precioTotal=precioTotal+precioCorto
    
    return precioTotal-1

            


print(precio(recorta(" Llego mañana alrededor  del mediodía ",5),1,2))
print(precio(recorta(" Llego mañana alrededor  del mediodía ",4),1,2))
