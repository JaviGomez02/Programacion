
opcion=0
surtidor=-1
cantidad=-1



while opcion!=8:
    print("1. Llenar surtidor")
    print("2. Llegada de coche")
    print("3. Ver puntos")
    print("4. Comprobar ventas")
    print("5. Ver surtidores")
    print("6. Asignar precio de gasolina")
    print("7. Asignar precio de diesel")
    print("8. Salir")
    opcion=int(input("Elige la opcion que quieres realizar: "))
    if opcion==1:
        while surtidor<0 or surtidor>4:
            surtidor=int(input("¿Que surtidor quieres llenar (1-4)? "))
            
        while cantidad<0:   
            cantidad=int(input("¿Qué cantidad quieres añadir? "))
            if cantidad<0:
                print("No se puede introducir una cantidad negativa")
        
        