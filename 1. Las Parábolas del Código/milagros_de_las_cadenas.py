# Este milagro formatea la primera letra de cada palabra a mayúscula
# Si usamos capitalize() convierte del string solo la primera letra a mayúscula

pergamino1 = "el señor de los anillos"

formato_titulo = pergamino1.title()
formato_capital = pergamino1.capitalize()
print(f"El título revelado es: {formato_titulo} / {formato_capital}")

# strip para purificar ambos espacios, lstrip a la izq o rstrip a la dcha
pergamino2 = " El Principito "
print(pergamino2.strip())

# split divide un texto en una sagrada lista con cada palabra
pergamino3 = "La Sagrada Jesubiblia"
print(pergamino3.split())

# join coge una lista de ofrendas y la une en un solo cántico
colores_divinos = ['rojo', 'azul', 'verde']
print(" | ".join(colores_divinos))

# find permite buscar la verdad y count para contar las bendiciones
# busca la primera aparición de la cadena TAA y cuenta cuántas veces aparece C
adn_creacion = "ATCCGATAAATTAGCTAA"

posicion_revelada = adn_creacion.find("TAA")
cantidad_c = adn_creacion.count("C")
print(f"La posición de TAA está en {posicion_revelada}. Hay {cantidad_c} C.")

# append para añadir fieles al final, insert los coloca en una posición dada
# extend fusiona una tribu con otra

dias_santos = ["Lunes", "Martes"]

dias_santos.insert(2, "Miércoles")
dias_santos.append("Jueves")
# con la mente enfocada en el código y sin distracciones
dias_santos.extend(["Viernes", "Sábado"])

print(dias_santos)

# pop elimina una ofrenda del diccionario y la devuelve para guardarla
# del para desterrar algo definitivamente al inframundo