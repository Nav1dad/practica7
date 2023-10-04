# Ejercicio 2
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: Debe ingresar un numero entero")
else:
    print(f"Su edad es de : {edad} años")