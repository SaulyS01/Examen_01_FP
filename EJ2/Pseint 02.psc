Algoritmo puntos_profesor_SYS
	//definir_datos de entrada
	Definir puntos, salario Como Entero;
	Definir salario_final, monto Como Real;
	Escribir "Ingrese el salario del docente: ";
	Leer salario;
	Escribir  "Ingrese los puntos del docente: ";
	Leer puntos;
	//proceso_datos de empresa
	Si puntos > 50 y puntos <= 100 Entonces
		salario_final <- salario * 0.10;
		monto <- salario_final + salario;
	//proceso_datos de salida
		Escribir "El salario inicial del docente es de: ", salario;
		Escribir "Los puntos iniciales del docente son: ", puntos;
		Escribir "El salario adicional es de: ", salario_final;
		Escribir "El monto final es de: ", monto;
		
	SiNo Si puntos > 100 y puntos <= 150 Entonces	
		salario_final <- salario * 0.50;
		monto <- salario_final + salario;
	//proceso_datos de salida
		Escribir "El salario inicial del docente es de: ", salario;
		Escribir "Los puntos iniciales del docente son: ", puntos;
		Escribir "El salario adicional es de: ", salario_final;
		Escribir "El monto final es de: ", monto;
		
	SiNo Si puntos > 150 Entonces
		salario_final <- salario * 1;
		monto <- salario_final + salario;	
	//proceso_datos de salida
		Escribir "El salario inicial del docente es de: ", salario;
		Escribir "Los puntos iniciales del docente son: ", puntos;
		Escribir "El salario adicional es de: ", salario_final;
		Escribir "El monto final es de: ", monto;
	SiNo
	//proceso_datos de salida
		Escribir "Los valores que ingresó no existen";
	Fin Si
	Fin Si
	Fin Si
FinAlgoritmo
