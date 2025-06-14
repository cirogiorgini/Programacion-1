
# Ejercicio 1: Factorial recursivo y listado desde 1 hasta n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingrese un número para calcular los factoriales desde 1 hasta ese número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# Ejercicio 2: Fibonacci hasta una posición indicada
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

limite = int(input("\nIngrese hasta qué posición desea mostrar la serie de Fibonacci: "))
for i in range(limite + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Ejercicio 3: Potencia con recursividad
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# Ejercicio 4: Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("\nIngrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")

# Ejercicio 5: Verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("\nIngrese una palabra para verificar si es un palíndromo: ").lower()
print("Es palíndromo." if es_palindromo(palabra) else "No es palíndromo.")

# Ejercicio 6: Suma de dígitos de un número
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("\nIngrese un número para calcular la suma de sus dígitos: "))
print(f"La suma de los dígitos es: {suma_digitos(numero)}")

# Ejercicio 7: Contar bloques en pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("\nIngrese la cantidad de bloques del nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# Ejercicio 8: Contar ocurrencias de un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("\nIngrese un número: "))
digito = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
