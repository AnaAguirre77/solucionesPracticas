"""Mostrar los números desde el 0 al número solicitado al usuario (input)"""

"""
Analisis:
Entrada:
num E Enteros
Salida:
variable contadora  i E Enteros
"""

num = int(input("Ingrese un numero entero..."))
i = 0

while i <= num:
  print(f"{i}")
  i = i + 1  

