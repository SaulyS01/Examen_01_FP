#definir datos de entrada
salario_final = 0
monto = 0
salario = int(input("Ingrese el salario del docente: "))
puntos = int(input("Ingrese los puntos del docente: "))
#proceso_datos de empresa
if puntos > 50 and puntos <= 100:
    salario_final = salario * 0.10
    monto = salario_final + salario
    #proceso_datos de salida
    print(f"El salario inicial del docente es de: {salario}")
    print(f"Los puntos iniciales del docente son: {puntos}")
    print(f"El salario adicional es de: {salario_final}")
    print(f"El monto final es de: {monto}")
elif puntos > 100 and puntos <= 150:
    salario_final = salario * 0.50
    monto = salario_final + salario
    #proceso_datos de salida
    print(f"El salario inicial del docente es de: {salario}")
    print(f"Los puntos iniciales del docente son: {puntos}")
    print(f"El salario adicional es de: {salario_final}")
    print(f"El monto final es de: {monto}")
elif puntos > 150:
    salario_final = salario * 1
    monto = salario_final + salario
    #proceso_datos de salida
    print(f"El salario inicial del docente es de: {salario}")
    print(f"Los puntos iniciales del docente son: {puntos}")
    print(f"El salario adicional es de: {salario_final}")
    print(f"El monto final es de: {monto}")
else:
    #proceso_datos de salida
    print("Los valores que ingresó no existen")


















