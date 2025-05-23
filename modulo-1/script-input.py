"""
# Pedir al usuario ingresar un número por teclado
# La consola esperará a que el usuario ingrese
# un valor desde el teclado
"""

msg = input("Ingresa un nombre: ")
age = int(input("Ingresa tu edad: ")) # Espera un entero
height = float(input("Ingresa tu altura: ")) # Espera un flotante
status = input("¿Tu usuario se encuentra activo? ") == "yes" # Retorna un booleano

print("Se ingresó: ", msg)
print("Edad: ", age)
print("Altura: ", height)
print("Estado: ", status)

print(type(msg))
print(type(age))
print(type(height))
print(type(status))