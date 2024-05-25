"""
Un estudiante está cursando 5 materias, tiene la nota de cada
materia y quiere saber cuál es su promedio.

Analisis E P S:

Entrada:
nota1, nota2, nota 3, nota4, nota5 E Reales
Salida: 
promedio E Reales
Proceso:
suma = nota1 + nota2 + nota3 + nota4 + nota5 

"""

nota1 = float(input("Ingrese la primer nota:"))
nota2 = float(input("Ingrese la segunda nota:"))
nota3 = float(input("Ingrese la tercer nota:"))
nota4 = float(input("Ingrese la cuarta nota:"))
nota5 = float(input("Ingrese la quinta nota:"))

suma = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma / 5
print(f"El promedio de las materias es", promedio)
