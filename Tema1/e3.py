a=int(input("¿Cuantos números quieres introducir? "))
for i in range (a):
    num=int(input("Introduce un número mayor que 0: "))
    if num<=0:
        print("Número no válido")
    elif num%2==0:
        print("El número "+str(num)+" es par")
    else:
        print("El número "+str(num)+" es impar")