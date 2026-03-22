# Pide nombre y apellidos y muestra solo las iniciales sagradas en mayúsculas
# (Linus Benedict Torvalds) L.B.T.

nombre_profeta = input("Introduce tu nombre y apellidos completos: ").strip()
fragmentos = nombre_profeta.split() # El milagro de la división

sello_sagrado = ""
for fragmento in fragmentos:
    if fragmento:
        sello_sagrado += fragmento[0].upper() + "."

print("Tus iniciales divinas son: ", sello_sagrado)