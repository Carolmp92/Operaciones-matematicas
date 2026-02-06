#Calcula el valor exponencial de un número dado una base y un exponente.
# Solicita al usuario que ingrese la base y el exponente.
base = float(input("Ingrese la base: "))
exponente = float(input("Ingrese el exponente: "))

# Calcula el valor exponencial utilizando el operador de potencia (**).
resultado = base ** exponente

# Muestra el resultado.
print("Resultado:", resultado)
#==============================
print("Introduce un número: ")
numeUsu= input()
num = int(numeUsu)


if (num % 2 == 0):
    print("El número introducido es par: " + numeUsu)
elif (num % 2 !=0):
    print("El número introducido no es par: " + numeUsu)