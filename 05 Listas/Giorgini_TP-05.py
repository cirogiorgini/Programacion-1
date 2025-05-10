# Ejercicio 1: 
multiples_de_4 = list(range(4, 101, 4))
print(multiples_de_4)

# Ejercicio 2: 
mis_elementos = [10, "perro", 3.14, "hola", True]
print(mis_elementos[-2])  

# Ejercicio 3: 
lista_vacia = []
lista_vacia.append("manzana")
lista_vacia.append("banana")
lista_vacia.append("cereza")
print(lista_vacia)

# Ejercicio 4: 
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Cambiar el segundo elemento
animales[-1] = "oso"  # Cambiar el último elemento
print(animales)

# Ejercicio 5: Analizar el siguiente programa y explicar qué hace:
# El código proporciona una lista 'numeros' con varios valores. Luego se obtiene el valor máximo de la lista usando max(numeros),
# y ese valor se elimina de la lista con el método remove.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # Elimina el valor máximo, en este caso 22.
print(numeros)  # Imprime la lista sin el valor máximo.

# Ejercicio 6:
numeros_saltos = list(range(10, 31, 5))
print(numeros_saltos[:2])  

# Ejercicio 7: 
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fiesta", "camioneta"]  
print(autos)

# Ejercicio 8: 
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Ejercicio 9: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
# d) Imprimir la lista resultante por pantalla.
print(compras)

# Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
