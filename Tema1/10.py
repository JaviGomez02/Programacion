#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es

from math import sqrt

A=int(input("Dame el valor de un lado: "))
B=int(input("Dame el valor de otro lado: "))
C=int(input("Dame el valor de otro lado: "))

if C==sqrt((A**2) + (B**2)):
    print("El triángulo es rectángulo")
if A==B or A==C or B==C:
    print("El triángulo es isósceles")
if A==B and B==C:
    print("El triángulo es equilatero")
else:
    print("El triángulo es escaleno")
