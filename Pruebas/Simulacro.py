#Ejercicio 3

flagA=True
flagB=True
boton=0

# while boton!="P" and boton!="p":
#     boton=str(input("¿Que botón quieres pulsar? (A, B o P): "))
#     if boton!="A" and boton!="a" and boton!="B" and boton!="b" and boton!="P" and boton!="p":
#         print("Pulsa un boton correcto")
#     if boton=="A" or boton=="a":
#         if flagA==True:
#          print("Melodia A1")
#             flagA=False
#         elif flagA==False:
#             print("Melodia A2")
#             flagA=True
#     elif boton=="B" or boton=="b":
#         if flagB==True:
#             print("Melodia B1")
#             flagB=False
#         elif flagB==False:
#             print("Melodia B2")
#             flagB=True
#     elif boton=="P" or boton=="p":
#         print("Programa apagado")

#Ejercicio 2

altura=1
peso=1
edad=1

# while altura>0 and peso>0 and edad>0:
#     altura=float(input("Introduce tu altura: "))
#     peso=float(input("Introduce tu peso: "))
#     edad=int(input("Introduce tu edad: "))
#     imc=peso/altura**2
#
#     if altura<0 or peso<0 or edad<0:
#         print("Programa terminado")
#     else:
#
#         print("Tu IMC es de "+str(round(imc, 2)))
#
#         if imc<18.5:
#             print("Tu IMC indica que tienes un peso insuficiente")
#         elif imc<25:
#             print("Tu IMC indica que tienes un peso normal")
#         elif imc<30:
#             print("Tu IMC indica que tienes sobrepeso")
#         elif imc<40:
#             print("Tu IMC indica que tienes obesidad")
#         else:
#             print("Tu IMC indica que tienes obesidad mórbida")
#
#         if edad>45 and imc>25:
#             print("Dada su edad e IMC es recomendable que cuide su salud cardiovascular")
#         elif imc>30:
#             print("Dado su IMC es muy recomendable que cuide su salud cardiovascular")

#Ejercicio 1

edad=int(input("Introduce la edad de Juan: "))
total=20
añado=0
if edad==1:
    print("Juan tiene "+str(total)+" euros")
elif edad>1:
    for i in range(edad):
        añado=total+15
        total=total+añado
    print(total)


#Ejercicio 4

def ejercicio4(lista):
    listaNueva=[]
    for i in range(len(lista)-1):
        if lista[i]==lista[i+1]:
            listaNueva.append(0)
        if lista[i]>lista[i+1]:
            listaNueva.append(1)
        if lista[i]<lista[i+1]:
            listaNueva.append(-1)
    return listaNueva

num=1
lista=[]
while num!=0:
    num=int(input("Introduce números para añadir a la lista: "))
    if num!=0:
        lista.append(num)
print(lista)

print(ejercicio4(lista))




        