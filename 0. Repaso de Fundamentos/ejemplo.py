# Ejemplo 1

edad = int(input("¿Qué edad tienes?"))
    
if edad > 35:
    print("Así me gustan 💅🏻")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("No tienes la edad suficiente para estar aquí")

# Ejemplo 2

nombre = input("¿Cómo te llamas?")
print(f"Hola {nombre}, bienvenidinchi!")

lugar = input("¿Dónde vives?")
print(f"Se ve que {lugar} es precioso!")

# Ejemplo 3

# Escribe un programa que calcule el area de un circulo y el usuario debe ingresar
# el radio del circulo. El programa debe calcular el area.

# Pi * r2

# libreria, sin ella pues sencillamente pondriamos el valor de pi a mano
import math

radio = float(input("Introduzca el radio del circulo:"))

area = math.pi * (radio ** 2)

print(f"El area del circulo es: {area}")

# Ejemplo 4

# Escribe un programa que compare 2 numeros ingresados por el usuario y diga cual
# es mayor, menor o si son iguales.

num1 = float(input("Introduzca el primer numero:"))
num2 = float(input("Introduzca el segundo numero:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
else:
    print(f"{num1} y {num2} son iguales")

# Ejemplo 5

# Crea un programa que pida al usuario un numero y luego imprima la tabla de
# multiplicar de ese numero del 1 al 10

numero = int(input("Introduzca un numero:"))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")