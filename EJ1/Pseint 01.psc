Algoritmo Notas_del_estudiante_SYS
	//definir_datos de entrada
	Definir nota1, nota2, nota3, nota4 Como Real
	Definir nota_final, nota_1, nota_2, nota_3, nota_4 Como Real;
	Escribir "Ingresar valor de la 1 unidad: ";
	Leer nota1;
	Escribir "Ingresar valor de la 2 unidad: ";
	Leer nota2;
	Escribir "Ingresar valor de la 3 unidad: ";
	Leer nota3;
	Escribir "Ingresar valor de la 4 unidad: ";
	Leer nota4;
	//proceso_datos de proceso
	nota_1 <- nota1 * 0.10;
	nota_2 <- nota2 * 0.15;
	nota_3 <- nota3 * 0.25;
	nota_4 <- nota4 * 0.50;
	nota_final <- nota_1 + nota_2 +nota_3 + nota_4;
	//proceso_datos de salida
	Escribir "La nota 1 es de: ", nota_1;
	Escribir "La nota 2 es de: ", nota_2;
	Escribir "La nota 3 es de: ", nota_3;
	Escribir "La nota 4 es de: ", nota_4;
	Escribir "La suma de las 4 notas es de: ", nota_final;
FinAlgoritmo

