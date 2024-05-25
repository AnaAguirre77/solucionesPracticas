Algoritmo comprasDespensa
	Definir valorLeche,precioFinal,descuentoJubilados1,descuentoJubilados2, descuentoJubilados3, descuentoGral1, descuentoGral2  Como Real
	Definir cantidadUnidades Como Entero
	Definir  jubilado Como Caracter
	
	Escribir "Es usted jubilado? Si / No"
	Leer jubilado
	Escribir "Cuantas unidades desea comprar?" 
	Leer cantidadUnidades
	
	valorLeche <- 1000
	
	precioSinDescuento <- cantidadUnidades * valorLeche
	descuentoDel10 <- cantidadUnidades * valorLeche * 0.90
	descuentoDel20 <- cantidadUnidades * valorLeche * 0.80
	descuentoDel25 <- cantidadUnidades * valorLeche * 0.75
	descuentoDel15 <- cantidadUnidades * valorLeche * 0.85
	
	
	Si jubilado = "Si" Entonces
		Si cantidadUnidades <12 Entonces
			Escribir "El precio final es $", descuentoDel10
			
		SiNo
			Si cantidadUnidades >=12 y cantidadUnidades <=24 Entonces
				Escribir "El precio final es $", descuentoDel20
			SiNo
				Escribir "El precio final es $", descuentoDel25
			FinSi
		FinSi
	SiNo
		Si cantidadUnidades <=12 Entonces
			Escribir "El precio final es $", precioSinDescuento
		SiNo
			Si cantidadUnidades >12 y cantidadUnidades <=24 Entonces
			  Escribir "El precio final es $", descuentoDel10
		    SiNo 
			  Escribir "El precio final es $", descuentoDel15
		     FinSi
		  
		FinSi
		
	FinSi
	
FinAlgoritmo
