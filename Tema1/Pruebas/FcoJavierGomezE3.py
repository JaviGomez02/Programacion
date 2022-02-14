
#Pedimos al usuario que introduzca la cantidad de números que va a introducir más tarde
numeros=int(input("¿Cuántos números quieres introducir para generar la clave? "))
suma=0 #Le damos el valor 0 a la variable suma
for i in range(numeros): #Creamos un bucle que se repite las veces que nos ha indicado el usuario anteriormente
    numClave=int(input("Introduce un número: ")) #Le pedimos un número para crear la clave
    if numClave<0: #Con este if, en caso de que el usuario nos dé un número negativo, lo pasamos a positivo. Esto lo hago para evitar problemas con la operación que vamos a realizas
        numClave=abs(numClave)
    if numClave%2!=0: #Este if solo se ejecuta cuando el número que nos da el usuario es impar
        resto=numClave%5 #Calculamos el resto de dividir el número entre 5
        suma=suma+resto #Creamos una variable para ir sumando todos los restos
print("El resultado de la clave es " + str(suma)) #Al final este mensaje nos indica la clave final