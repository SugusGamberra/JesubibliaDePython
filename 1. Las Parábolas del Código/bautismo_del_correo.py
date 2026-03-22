# Pide el nombre y apellido de un fiel acólito y su correo electrónico del santuario
# con el formato nombre.apellido@santuario.com, todo humillado en minúsculas y sin espacios.

nombre_alma = input("Dime tu nombre de pila: ").strip().lower()
linaje = input("Dime tu primer apellido terrenal: ").strip().lower()

correo_bautizado = f"{nombre_alma}.{linaje}@santuario-daw.com"

print("Tu correo institucional bendecido es: ", correo_bautizado)