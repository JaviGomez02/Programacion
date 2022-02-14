# nombres = [""]*5
# for i in range(5):
#     nombre = "Por favor introduce un nombre "+str(i+1)+": "
#     nombres[i] = input(nombre)
# print("Tus nombres son: ")
# for i in range (5):
#     print(nombres[i])


#Ejercicio que solicite nombre y lo guarde en una lista para imprimirlos luego.
#Después de cada nombre debe preguntar si quiere introducir más o no (S/N)

def preguntaSeguir():
    respuesta=input("Quieres introducir otro nombre(S/N): ")
    while respuesta!="S" and respuesta!="N":
        print("Introduce S o N")
        respuesta=input("Quieres introducir otro nombre(S/N): ")
    return respuesta

names=[]
nombre=input("Introduce un nombre: ")
names.append(nombre)
respuesta=preguntaSeguir()

while respuesta=="S":
    nombre=input("Introduce un nombre: ")
    names.append(nombre)
    respuesta=preguntaSeguir()
    
print(names)






