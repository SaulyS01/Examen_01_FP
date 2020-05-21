Algoritmo vacuna_SYS
	Escribir "Ingrese su edad: ";
	Leer edad;
	Escribir "Ingrese su sexo: M/F ";
	Leer sexo;
	Si edad >= 70 y sexo == "M" Entonces 
		Escribir "A usted se le aplica el tipo C por tener ", edad, " años de edad";
	SiNo Si edad >= 70 y sexo == "F"  Entonces
		Escribir "A usted se le aplica el tipo C por tener ", edad, " años de edad";
	SiNo Si edad >= 16 y  edad <= 69 y sexo == "F" Entonces
		Escribir "A usted se le aplica el tipo B por tener ", edad, " años de edad";
	SiNo Si edad >= 16 y  edad <= 69 y sexo == "M" Entonces
		Escribir "A usted se le aplica el tipo A por tener ", edad, " años de edad";
	SiNo Si edad < 16 y sexo == "M" Y edad > 0 Entonces
		Escribir "A usted se le aplica el tipo A por tener ", edad, " años de edad";	
	SiNo Si edad < 16 y sexo == "F" Y edad > 0 Entonces
		Escribir "A usted se le aplica el tipo A por tener ", edad, " años de edad";
	SiNo
		Escribir "El valor que ingresó no existe intentelo nuevamente";
	Fin Si
	Fin Si
	Fin Si
	Fin Si
	Fin Si
	Fin Si
FinAlgoritmo
