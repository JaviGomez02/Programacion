'''Un restaurante te ha encargado una aplicación para colocar a los clientes en sus mesas. En una mesa 
se pueden sentar de 0 (mesa vacía) a 4 comensales (mesa llena). Cuando llega un cliente se le pregunta
cuántos son (dando un mensaje de error si el número de clientes es superior a 4). Para el grupo que 
llega, se busca siempre la primera mesa libre (con 0 personas). Si no quedan mesas libres, se busca 
donde haya un hueco para todo el grupo, por ejemplo si el grupo es de dos personas, se podrá colocar 
donde haya una o dos personas. Cada vez que se sientan nuevos clientes se debe mostrar la mesa en la 
que se sientan y el estado de las mesas (Libre u ocupada con x comensales). Si no hay sitio se deberá 
mostrar el mensaje “Restaurante completo” y el estado de las mesas Los grupos no se pueden romper 
aunque haya huecos sueltos suficientes. El programa terminará cuando se quiera sentar a -1 comensal. 
En nuestro restaurante habrá 10 mesas, pero deja preparado el programa para que se pueda ampliar 
fácilmente el número de mesas.'''

NUM_MESAS=10

## Función que recibe un array y un número como parámetro y añade tantas mesas vacias (0) como indique
## el número. La función no devuelve nada

def annadirMesas(lista,num):
    for i in range(num):
        lista.append(0)
        
        
## Función que devuelve el número de la primera mesa vacia que encuentra, es decir que esté a cero
## Si encuentra mesa deberá asignar el número de personas en esa mesa
## Recuerda que la mesa 1 está en la posición cero. Recibe la lista la lista de las mesas
## Si no encuentra ninguna mesa vacia devuelve -1

def numeroMesaVacia(lista,numPersonas):
    for i in range(len(lista)-1, -1, -1):
        if lista[i]==0:
            
   

## Funcion que devuelve el número de la primera mesa vacía donde quepan los comensales que recibe
## como argumento. 
## Si encuentra mesa deberá asignar el número de personas junto con las que hay a la mesa
## Recuerda que en casa mesa sólo caben 4 comensales. Si no hay sitio debe devolver un -1
def numeroMesaHueco(lista, numPersonas):
  

## Función que recorre la lista que se le pasa como argumento y devuelve una cadena de texto con la 
## ocupación de cada una 
## de las mesas. Recuerda que para que salga bonito pones un \n cuando queremos hacer un salto
## de linea.

def imprimirMesas(lista):
 
  
## Programa principal        
listaMesas = []

     
    
    
    