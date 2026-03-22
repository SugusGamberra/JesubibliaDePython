# Crea un programa que pide al usuario peso y estatura terrenales
# y muestra su Índice de Masa Corporal (IMC) divino, redondeado a 2 decimales.

peso_terrenal = input("Ingresa tu peso de mortal en kg: ")
estatura_celestial = input("Ingresa tu estatura en metros mirando al cielo: ")
imc_divino = round(float(peso_terrenal) / float(estatura_celestial) ** 2, 2)

# Convertimos el número sagrado en string para poder castearlo a texto
print("Tu índice de masa corporal terrenal es " + str(imc_divino) + " 🙏🏻")