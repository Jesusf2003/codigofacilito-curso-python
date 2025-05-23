"""
# Sublistas
"""
# Slicing: [start:end:skips]
# Shallow copy: [:]
# Slicing: [::-1] -> Reverso
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # str

# Slicing
# Crear una sublista de los primeros 3 elementos
# Al no declarar un índice inicial, se interpreta por defecto como 0
# Al no declarar un índice final, se interpreta por defecto hasta el último índice
new_list = courses[2:5]
courses_copy = courses[::2] # Shallow copy

print(new_list)
print(courses_copy)