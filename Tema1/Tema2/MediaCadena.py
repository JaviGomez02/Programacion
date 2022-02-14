#3 num entre 10-100 y si da un valor que no es 10-100 pregunta otra vez. Media de esos 3 numeros

def leer(cadena):
    num1=int(input(cadena))
    while num1<10 or num1>100:
        num1=int(input(cadena))
    return num1
suma=0
num1=leer("Introduce el primer número: ")
suma=num1+suma

num2=leer("Introduce el segundo número: ")
suma=num2+suma

num3=leer("Introduce el tercer número: ")
suma=num3+suma

print(suma/3)