
"""Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento."""

nombre = input("Ingrese su nombre: ")

apellido = input("Ingrese su apellido: ")

dni = input("Ingrese su dni: ")

email = input("Ingrese su email: ")

fechaNacimiento = input("Ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ")

persona1 = {"nombre": nombre, "apellido": apellido, "dni": dni, "email":email, "fecha_de_Nacimiento":fechaNacimiento}

print(persona1)
