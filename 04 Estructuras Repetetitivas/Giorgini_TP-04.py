# ejercicio 1: 
print("Ejercicio 1:")
for i in range(101):
    print(i)

# ejercicio 2: 
print("\nEjercicio 2:")
numero = int(input("Ingrese un número entero: "))
digitos = len(str(abs(numero)))
print(f"El número tiene {digitos} dígitos.")

# ejercicio 3: 
print("\nEjercicio 3:")
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = sum(range(min(inicio, fin) + 1, max(inicio, fin)))
print(f"La suma es: {suma}")

# ejercicio 4: 
print("\nEjercicio 4:")
total = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print(f"Total acumulado: {total}")

# ejercicio 5:
print("\nEjercicio 5:")
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Intentos: {intentos}")
        break
    print("Intenta nuevamente.")

# ejercicio 6: 
print("\nEjercicio 6:")
for i in range(100, -1, -2):
    print(i)

# ejercicio 7: 
print("\nEjercicio 7:")
n = int(input("Ingrese un número positivo: "))
suma = sum(range(n + 1))
print(f"La suma es: {suma}")

# ejercicio 8: 
print("\nEjercicio 8:")
pares = impares = positivos = negativos = 0
cantidad = 100  # Cambiar a menos para pruebas
print(f"Ingrese {cantidad} números enteros:")
for _ in range(cantidad):
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}")
print(f"Positivos: {positivos}, Negativos: {negativos}")

# ejercicio 9: 
print("\nEjercicio 9:")
cantidad = 100  
suma = 0
print(f"Ingrese {cantidad} números enteros:")
for _ in range(cantidad):
    suma += int(input())
media = suma / cantidad
print(f"Media: {media:.2f}")

# ejercicio 10: Invertir número
print("\nEjercicio 10:")
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print(f"Número invertido: {invertido}")