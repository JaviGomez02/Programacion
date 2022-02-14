#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
gradosF = int(input('Introduce un valor de grados Fahrenheit: '))
gradosC = round((((gradosF - 32) * 5)/9),2)
print(str(gradosF) + ' grados Fahrenheit son ' + str(gradosC) + ' grados Celcius')

