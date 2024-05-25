
Algoritmo puntosEquipo
    Definir partidosEmpatados,partidosGanados, partidosPerdidos, TotalPuntos como Enteros

	Escribir "Ingrese cantidad de partidos que el equipo ha empatado"
	Leer partidosEmpatados
	Escribir "Ingrese cantidad de partidos que el equipo ha ganado"
	Leer partidosGanados
	Escribir "Ingrese cantidad de partidos perdidos"
	Leer partidosPerdidos
	
	TotalPuntos = partidosEmpatados *1 + partidosGanados *3  + partidosPerdidos *0
	Escribir "El total de puntos acumulados es: ", TotalPuntos
FinAlgoritmo
