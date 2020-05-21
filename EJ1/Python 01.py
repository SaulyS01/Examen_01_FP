#definir_datos de entrada

nota_1 = 0
nota_2 = 0
nota_3 = 0
nota_4 = 0

nota1 = int(input("Ingresar valor de la 1 unidad: "))
nota2 = int(input("Ingresar valor de la 2 unidad: "))
nota3 = int(input("Ingresar valor de la 3 unidad: "))
nota4 = int(input("Ingresar valor de la 4 unidad: "))

#proceso_datos de proceso

nota_1 = nota1 * 0.10;
nota_2 = nota2 * 0.15;
nota_3 = nota3 * 0.25;
nota_4 = nota4 * 0.50;
nota_final = nota_1 + nota_2 +nota_3 + nota_4;

#proceso_datos de salida

print(f"La nota 1 es de: {nota_1}")
print(f"La nota 2 es de: {nota_2}")
print(f"La nota 3 es de: {nota_3}")
print(f"La nota 4 es de: {nota_4}")
print(f"La suma de las 4 notas es de: {nota_final}")
