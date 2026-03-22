# Crea un programa que almacene la palabra sagrada en una variable
# le preguntamos al fiel por la contraseña e imprima si coincide con la guardada
# sin tener en cuenta las debilidades humanas (minúsculas o mayúsculas)

palabra_sagrada = "jesubiblia"

plegaria = input("Ingresa la palabra sagrada para poder acceder al reino: ")

# Usamos el método .lower() para humillar a minúsculas lo que el usuario ingresó
# Si quisiéramos exaltarlo a mayúsculas usamos .upper()
if palabra_sagrada == plegaria.lower():
    print("Bendición concedida. Contraseña correcta. 💅🏻")
else:
    print("Herejía detectada. Contraseña incorrecta. 🛑")