#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente
base = int(input("Introduce la base de la potencia: "))
exponente = int(input("Introduce el exponente de la potencia: "))
potencia = (base)**(exponente)
if exponente>=0:
    print(potencia)
if exponente<0:
    exponente = (-exponente)
    potencia = str((base)**(exponente))
    print("1/" + potencia)
