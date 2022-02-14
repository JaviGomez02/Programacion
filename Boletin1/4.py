#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra
precioTotal = int(input('Introduce el precio total de la compra: '))
descuento = int((precioTotal * 15)/100)
precioDesc = (precioTotal - descuento)
print('El precio con descuento incluido es de ' + str(precioDesc))
