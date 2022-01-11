#Este programa calcula IMC
import time
print('Hola! Como es tu nombre?')
nombre = input()
print('Cual es tu edad?')
edad = input()
if edad >= 18:
    print('Sos mayor de edad, podemos continuar')
print('Perfecto ' + nombre + ', empecemos')
for letra in 'Vamos a conocer tu Indice de Masa Corporal':
    time.sleep(0.01)
print('Vamos a conocer tu Indice de Masa Corporal')
for letra in 'Voy a necesitar tu peso':
    time.sleep(0.01)
print('Voy a necesitar tu peso')
peso = float(input())
print('Ahora necesito tu altura, en centimetros y separada por un punto')
altura = float(input())
imc = peso / (altura ** 2);
print(f'Tu IMC es:{imc:.2f}')
if imc <= 18.5:
    print(nombre + ', estas debajo del peso normal')
elif imc <= 24.99:
    print('Felicidades '+ nombre + ', estas en el peso correcto')
elif imc <= 29.99:
    print(nombre + ', tu composicion corporal esta en sobrepeso')
elif imc <= 34.99:
    print(nombre + ', lamentablemente tienes obesidad, deberias visitar un medico')

 








