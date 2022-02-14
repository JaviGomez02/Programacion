#Mostrar en pantalla los N primero números primos.
#Se pide por teclado la cantidad de números primos que queremos mostrar
primos=int(input("Indica cuantos números primos quieres saber: "))
num=int(input("Introduce un número: "))
esPrimo=True
cont=2
while cont <= num//2 and esPrimo==True:
    if (num%cont==0):
        esPrimo=False
    cont=cont+1
if esPrimo==True:
    print("El número ", num, " es primo")
else:
    print("El número ", num, " no es primo")