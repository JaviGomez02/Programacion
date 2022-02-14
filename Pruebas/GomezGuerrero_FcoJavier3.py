

def telegrama(texto,longitud):
    lista=[]
    cadena=""
    for i in range(len(texto)):
        if texto[i]!=" ":
            cadena=cadena+texto[i]

        for i in range(longitud):
            lista.append(cadena)
        
        
        
    return lista

print(telegrama("hola que tal", 2))