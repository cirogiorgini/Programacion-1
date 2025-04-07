#ejercicio 1
print('Hola Mundo!')

#ejercicio 2
nombre =  input('ingrese su nombre: ')
print(f'Hola {nombre}!')

#ejercicio 3
nombre = input('ingrese su nombre')
apellido = input('ingrese su apellido')
edad = input('ingrese su edad')
residencia = input('ingrese su residencia')
print(f'soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ')

#ejercicio 4
import math
radio = float(input('Ingrese el radio del círculo: '))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f'El área del círculo es {area:.2f} y su perimetro es {perimetro:.2f}')

#ejercicio 5
segundos = int(input('Ingrese una cantidad de segundos: '))
horas = segundos / 3600
print(f'{segundos} segundos equivalen a {horas:.2f} horas')

#ejercicio 6
numero = int(input('Ingrese un numero: '))
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

#ejercicio 7
num1 = int(input('Ingrese el primer numero (distinto de 0): '))
num2 = int(input('Ingrese el segundo numero (distinto de 0): '))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f'Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division:.2f}')

#ejercicio 8
peso = float(input('Ingrese su peso en kg: '))
altura = float(input('Ingrese su altura en metros: '))
imc = peso / (altura ** 2)
print(f'Su índice de masa corporal es {imc:.2f}')

#ejercicio 9
celsius = float(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = (9/5) * celsius + 32
print(f'{celsius}°C equivalen a {fahrenheit:.2f}°F')

#ejercicio 10
num1 = float(input('Ingrese el primer numero: '))
num2 = float(input('Ingrese el segundo numero: '))
num3 = float(input('Ingrese el tercer numero: '))
promedio = (num1 + num2 + num3) / 3
print(f'El promedio de los tres numeros es {promedio:.2f}')
