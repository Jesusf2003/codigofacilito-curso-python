"""
# Operadores relacionales

# Usualmente dan un resultado booleano
# ==, !=, <, >, <=, >=

"""

print("Operadores relacionales")
number_one = 10
number_two = 20

result = number_one < number_two

print(result)
print(type(result))
print("\n")

"""
# Operadores lógicos

# Usualmente dan un resultado booleano único
# and, or, not
"""

print("Operadores lógicos")

number_one = 10
number_two = 20

#result = True and True and number_one != number_two
# La comparación debe ser verdadera
# Se recomiendo encapsular código o comparaciones entre paréntesis

result = (
    (number_one == number_two and True)
    and (number_one < 100)
    and (number_two < 100)
    or (number_one > 100 and number_two > 200)
)

print(not not not result)