mes=-2 #Creamos las variables. A la variable mes le damos un valor negativo. Esto luego no influye ya que le pediremos al usuario que introduzca su mes.
ano=0 #A las demás variables le damos el valor 0
pac30=0 #Las variables pac significan paciente, y el número de al lado es la edad de los pacientes
pac31_49=0
pac50=0
while mes!=-1: #Este primer bucle se ejecutará hasta que el usuario introduzca el valor -1 en mes
    mes=-2
    while mes<-1 or mes>12: #Este bucle sirve para volver a pedir el mes en caso de ser incorrecto--
        mes=int(input("Introduce tu mes de nacimiento (1 para enero, 2 para febrero, 3 para marzo...) "))
        if mes<-1 or mes>12:
            print("Por favor introduce un número del 1 al 12")
    if mes!=-1: #Al igual que el anterior bucle, este vuelve a pedir el año en caso de que sea incorrecto
        while ano<1900 or ano>2015:
            ano=int(input("Introduce tu año de nacimiento: "))
            if ano<1900 or ano>2015:
                print("Introduce un año válido")    
    edad=(2021-ano) #Calculamos la edad
    if mes>=11: #Le sumamos un año en caso de que el mes sea noviembre o diciembre
        edad=edad+1
    if edad<=30: 
        pac30=pac30+1 #Vamos sumando 1 cada vez que haya un paciente de dicha edad.
    elif edad>=31 and edad<=49:
        pac31_49=pac31_49+1 #Hacemos lo mismo que en el if anterior
    elif edad>=50:
        pac50=pac50+1 #Sumamos 1 al paciente de esa edad
print("Hay "+str(pac30)+" enfermos menores de 30 años") #Cuando termine el programa, recibiremos un mensaje con el número de pacientes de cada edad
print("Hay "+str(pac31_49)+" enfermos entre 31 y 49 años")
print("Hay "+str(pac50)+" enfermos mayores de 50 años")