# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

monedas2 = int(input('¿Cuántas monedas de dos euros tienes? '))
monedas1 = int(input('¿Cuántas monedas de un euro tienes? '))
monedas50 = int(input('¿Cuántas monedas de 50 céntimos tienes? '))
monedas20 = int(input('¿Cuántas monedas de 20 céntimos tienes? '))
monedas10 = int(input('¿Cuántas monedas de 10 céntimos tienes? '))
euros = 0
centimos = 200*monedas2+100*monedas1+50*monedas50+20*monedas20+10*monedas10
while centimos >= 100:
    euros = euros+1
    centimos = centimos-100
print('Tenemos '+str(euros)+' euros y '+str(centimos)+' céntimos')
