# Ejercicio 1
try:
    valor = int(input("Ingrese el numero: "))
    resultado = 10 / valor
except ValueError:
    print("Error: Debe ingresar un numero valido")
except ZeroDivisionError:
    print("Error: No puedesn dividir entre cero")
else:
    print(f"El resultado de la division es: {resultado}")