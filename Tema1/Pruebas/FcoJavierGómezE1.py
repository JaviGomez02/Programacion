#Definimos con valor 0 las tres variables con las que vamos a trabajar
edad=0
covid=0
vac=0
while edad<=8 or edad>100: #Hacemos un bucle que no parará hasta recibir los valores correctos
    edad=int(input("Introduce tu edad: ")) #Pedimos la edad al usuario
    if edad<=8 or edad>100: #Con este if mandaremos un mensaje al usuario en caso de que los valores sean incorrectos
        print("Por favor, introduce una edad correcta")
while covid<1 or covid>2: #Este bucle tiene el mismo objetivo que el anterior
    covid=int(input("¿Has pasado el covid? Introduce 1 para si y 2 para no: ")) #Preguntamos al usuario si ha pasado el covid
    if covid<1 or covid>2:
        print("Por favor introduce 1 para si y 2 para no")
while vac<1 or vac>3: #Mismo bucle para recibir los valores correctos
    vac=int(input("¿Que vacuna has recibido? Introduce 1 para pfizer, 2 para astrazeneca y 3 para moderna: ")) #Preguntamos al usuaruio que vacuna ha recibido
    if vac<1 or vac>3:
        print("Por favor introduce 1 para pfizer, 2 para astrazeneca y 3 para moderna")
 
if vac==2: #Este if funciona si el usuario ha recibido Astrazeneca
    print("Debes volver a vacunarte")
elif vac==3 and edad>=60: #Este elif funciona si el usuario ha recibido Moderna y tiene mas de 60 años
    if covid==2: #Si no ha pasado el covid, manda ese print al usuario
        print("Debes volver a vacunarte")
elif vac==3 and covid==1: #Si ha pasado el covid y ha recibido Moderna, manda el print de abajo al usuario
    print("No debes volver a vacunarte")
elif vac==1: #Este elif funciona si el usuario ha recibido Pfizer
    if covid==2: #Si no ha pasado el covid, manda ese print al usuario
        print("Debes volver a vacunarte")
    elif covid==1 and edad>=70: #Si ha pasado el covid pero tiene mas de 70 años manda el print al usuario
        print("Debes volver a vacunarte")
    else: #Si no es ninguna de las anteriores opciones, envia el siguiente print al usuario
        print("No debes volver a vacunarte")