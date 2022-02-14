#Definimos todas las variables. Cada variable es una mesa distinta
mesa1=0
mesa2=0
mesa3=0
mesa4=0
mesa5=0
mesa6=0
mesa7=0
mesa8=0
mesa9=0
mesa10=0

grupo=-2
while grupo!=-1: #Bucle que termina cuando se introduce -1
    grupo=int(input("¿Cuantas personas sois? "))
    while grupo<-1 or grupo>4: #Bucle que termina solo cuando grupo es un número entre 1 y 4
        grupo=int(input("¿Cuantas personas sois? "))
        if grupo<-1 or grupo>4:
            print("Solo se permite un máximo de 4 clientes")
    if grupo==-1: #Mensaje de programa terminado que se imprime cuando grupo es igual a -1
        print("Programa terminado")
    else: #Creamos un if para cada variable.
        if (mesa1+grupo)<=4:
            mesa1=mesa1+grupo #Se le suma la cantidad del grupo a la mesa correspondiente. Cuando la suma del grupo y la mesa superan las 4 personas pasa al siguiente if
            print("Pueden sentarse en la mesa 1")
        elif (mesa2+grupo)<=4:
            mesa2=mesa2+grupo
            print("Pueden sentarse en la mesa 2")
        elif (mesa3+grupo)<=4:
            mesa3=mesa3+grupo
            print("Pueden sentarse en la mesa 3")
        elif (mesa4+grupo)<=4:
            mesa4=mesa4+grupo
            print("Pueden sentarse en la mesa 4")
        elif (mesa5+grupo)<=4:
            mesa5=mesa5+grupo
            print("Pueden sentarse en la mesa 5")
        elif (mesa6+grupo)<=4:
            mesa6=mesa6+grupo
            print("Pueden sentarse en la mesa 6")
        elif (mesa7+grupo)<=4:
            mesa7=mesa7+grupo
            print("Pueden sentarse en la mesa 7")
        elif (mesa8+grupo)<=4:
            mesa8=mesa8+grupo
            print("Pueden sentarse en la mesa 8")
        elif (mesa9+grupo)<=4:
            mesa9=mesa9+grupo
            print("Pueden sentarse en la mesa 9")
        elif (mesa10+grupo)<=4:
            mesa10=mesa10+grupo
            print("Pueden sentarse en la mesa 10")
        else: #Cuando no entra en ningún if de los anteriores imprime el siguiente mensaje.
            print("No hay ninguna mesa disponible. El restaurante está completo")   
        #Imprimimos la cantidad de comensales que tiene cada mesa
        print("La mesa 1 tiene "+str(mesa1)+" comensales")
        print("La mesa 2 tiene "+str(mesa2)+" comensales") 
        print("La mesa 3 tiene "+str(mesa3)+" comensales") 
        print("La mesa 4 tiene "+str(mesa4)+" comensales") 
        print("La mesa 5 tiene "+str(mesa5)+" comensales") 
        print("La mesa 6 tiene "+str(mesa6)+" comensales") 
        print("La mesa 7 tiene "+str(mesa7)+" comensales") 
        print("La mesa 8 tiene "+str(mesa8)+" comensales") 
        print("La mesa 9 tiene "+str(mesa9)+" comensales") 
        print("La mesa 10 tiene "+str(mesa10)+" comensales") 
        
            
            
            
            
            
            
            
            
            
            
            
