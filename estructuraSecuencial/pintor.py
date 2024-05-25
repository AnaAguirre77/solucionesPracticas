"""Un pintor de casas debe hacer un presupuesto para un cliente. 
Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. 
El cliente le indica que necesita conocer el costo de mano de obra para pintar 
una pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
cuadrado. 
Hacer un algoritmo para calcular el costo de mano de obra para
pintar la pared.

Analisis:

Entrada:
metros_cuadrados E enteros
mano_de_obra E enteros
Salida: 
presupuesto E enteros
Proceso:
presupuesto = metros_cuadrados * mano_de_obra 

"""

metros_cuadrados = int(input("Ingrese la cantidad de metros cuadrados: "))

mano_de_obra = int(input("Ingrese el precio por metro cuadrado pintado: "))

presupuesto = metros_cuadrados * mano_de_obra 

print(f"El presupuesto final es ${presupuesto}")