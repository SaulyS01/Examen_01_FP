#definir datos de entrada
edad = int(input("Ingrese su edad: \n"))
sexo = str(input("Ingrese su sexo M/F: \n"))
#proceso_datos de empresa
if edad >= 70 and sexo == "M":
    # proceso_datos de salida
    print(f"A usted se le aplica el tipo C por tener {edad} años de edad")
elif edad >= 70 and sexo == "F":
    # proceso_datos de salida
    print(f"A usted se le aplica el tipo C por tener {edad} años de edad")
elif edad >= 16 and edad <= 69 and sexo == "F":
    # proceso_datos de salida
    print(f"A usted se le aplica el tipo B por tener {edad} años de edad")
elif edad >= 16 and edad <= 69 and sexo == "M":
    # proceso_datos de salida
    print(f"A usted se le aplica el tipo A por tener {edad} años de edad")
elif edad < 16 and sexo == "M" and edad > 0:
    # proceso_datos de salida
    print(f"A usted se le aplica el tipo A por tener {edad} años de edad")
elif edad < 16 and sexo == "F" and edad > 0:
    # proceso_datos de salida
    print(f"A usted se le aplica el tipo A por tener {edad} años de edad")
else:
    # proceso_datos de salida
    print("El valor que ingresó no existe intentelo nuevamente")