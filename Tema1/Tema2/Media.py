#3 num entre 10-100 y si da un valor que no es 10-100 pregunta otra vez. Media de esos 3 numeros
suma=0
for i in range(3):
    num=int(input("Introduce un número entre 10 y 100: "))
    while num<=10 or num>=100:
        num=int(input("Introduce un número entre 10 y 100: "))
    suma=suma+num
    
media=suma/3
print("La media es "+str(media))