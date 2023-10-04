# Ejercicio 1
try:
    contra = int(input("Ingrese la contraseña: "))

except ValueError:
    print("Error: Debe ingresar un dato de tipo entero")
    
if contra > 100:
    print(f"Su contra se {contra}")
elif contra <= 50:
    print("Error: Debe ingresar una contra mas larga")


