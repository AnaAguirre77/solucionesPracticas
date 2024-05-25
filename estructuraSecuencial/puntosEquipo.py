
"""
Un hincha de fútbol desea conocer la cantidad de puntos que su
equipo lleva acumulados en el campeonato.
Para ello recibe cada semana la información de la cantidad total de partidos, 
desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado. 
Por cada partido empatado recibe un punto, 
por cada partido ganado tres puntos 
y por los perdidos cero puntos.

Analisis:
Entrada:
partidos_empatados E enteros
partidos_ganados E enteros
Salida: 
puntos_acumulados E enteros

"""

partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))

# partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos"))

puntos_acumulados = partidos_empatados + (partidos_ganados * 3)

print(f"La cantidad de puntos acumulados es {puntos_acumulados}. ")