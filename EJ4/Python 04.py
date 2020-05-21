#definir datos de entrada
numero_1 = float(input("Ingrese el primer valor: \n"))
numero_2 = float(input("Ingrese el segundo valor: \n"))
operacion = str(input("¿Que operación desea realizar?\n"
                      "     1.- Suma +\n"
                      "     2.- Resta -\n"
                      "     3.- Multiplicación x\n"
                      "     4.- División /\n"
                      "     5.- Potencia ^\n"))
#proceso_datos de proceso
if operacion == "+" or operacion == "1" or operacion == "suma":
    total = numero_1 + numero_2
# proceso_datos de salida
    print(f"La suma es de: {total}")
# proceso_datos de proceso
elif operacion == "-" or operacion == "2" or operacion == "resta":
    total = numero_1 - numero_2
# proceso_datos de salida
    print(f"La resta es de: {total}")
#proceso_datos de proceso
elif operacion == "*" or operacion == "3" or operacion == "multiplicacion" or operacion == "multiplicación":
    total = numero_1 * numero_2
# proceso_datos de salida
    print(f"La multiplicación es de: {total}")
#proceso_datos de proceso
elif operacion == "/" or operacion == "4" or operacion == "division" or operacion == "división":
    total = numero_1 / numero_2
# proceso_datos de salida
    print(f"La división es de: {total}")
#proceso_datos de proceso
elif operacion == "^" or operacion == "5" or operacion == "potencia":
    total = numero_1 ** numero_2
# proceso_datos de salida
    print(f"La potencia es de: {total}")
else:
# proceso_datos de salida
    print("La operación no existe inténtelo nuevamente")
