
#Creamos las listas que vamos a usar para la función; Una lista con todas las letras mayúsculas, otra con todas las minúsculas y otra con los dígitos del 0 al 9
mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
digitos=["0","1","2","3","4","5","6","7","8","9"]



def contraseña(cadena):
    #Definimos tres banderas que vamos a usar para cada caso(mayusculas, minusculas, digitos)
    flag1=False
    flag2=False
    flag3=False
    if len(cadena)>=8: #If en el que solo entra si la cadena es igual o mayor a 8 carácteres
        for i in range(len(cadena)): #Recorremos la cadena.
            if cadena[i] in mayusculas: #Si algún carácter de la cadena es mayúsculas se activa la bandera 1. Lo mismo con la bandera 2 en el caso de las minúsculas y la bandera 3 en el caso de los dígitos
                flag1=True
            elif cadena[i] in minusculas:
                flag2=True
            elif cadena[i] in digitos:
                flag3=True

        if flag1==True and flag2==True and flag3==True: #Si las tres banderas están activadas devuelve True
            resultado=True
        else:
            resultado=False

    else:
        resultado=False
    return resultado #Devuelve True si la contraseña es fuerte o False si la contraseña es débil
    
print(contraseña("Aaaaq333434234324234"))
        