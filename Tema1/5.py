#Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
distancia = abs(num1 - num2)
print('La distancia de los dos números es de: ' + str(distancia))
