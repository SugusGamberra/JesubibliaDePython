# Truco para VSC: Para comentar varias lineas a la vez, selecciona las lineas
# Pulsa Ctrl + K + C

# Hola mundo
print("Hola mundo")

# Variables
nombre = "Sugus"
edad = 32
altura = 1.62
es_estudiante = True

# Concatenar
print(nombre, edad, altura, es_estudiante)

#type
print(type(nombre))

# Operadores matemáticos
a = 10
b = 8

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
exponente = a ** b

print("Suma: ", suma, " Resta: ", resta, " Multiplicacion: ", multiplicacion, " Division: ", division, " Modulo: ", modulo, " Exponente: ", exponente)

# Operadores de comparacion
x = 5
y = 10

igual = x == y
diferente = x != y
mayor = x > y
menor = x < y
mayor_igual = x >= y
menor_igual = x <= y

print("Igual: ", igual, " Diferente: ", diferente, " Mayor: ", mayor, " Menor: ", menor, " Mayor o igual: ", mayor_igual, " Menor o igual: ", menor_igual)

# Entradas de texto
edad_usuario = int(input("Introduzca su edad: "))

print(f"Hola! Tienes {edad_usuario} años")

altura_usuario = float(input("Introduzca su altura: "))

print(f"Hola! Mides {altura_usuario} cm")

# Condicionales

if edad_usuario >= 18:
    print("Eres mayor de edad")
elif edad_usuario >= 13:
    print("Eres un adolescente")
else:
    print("Eres un niño")

# Operadores lógicos
c = True
d = False

and_logico = c and d
or_logico = c or d

# Bucles

# For

for i in range(5 + 1): # Para que incluya al 5, o poner 6 directamente
    print(i)

# While

contador = 0

while contador < 5:
    print(contador)
    contador += 1