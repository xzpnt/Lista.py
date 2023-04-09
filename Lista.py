import os.path

archivo_existente = os.path.isfile("Lista.txt")

personas = []

if archivo_existente:
	with open("Lista.txt", "r") as archivo:
		for linea in archivo:
			if linea.strip():
				nombre, apellido, edad = linea.strip().split(",")
				edad = int(edad)
				personas.append((nombre, apellido, edad))

while True:
	nombre = input("Escribe tu nombre (o escribe salir para guardar los datos): ")
	if nombre == "salir":
		break
	apellido = input("Escribe tu apellido: ")
	edad = int(input("Escribe tu edad: "))

	personas.append((nombre, apellido, edad))

with open("Lista.txt", "w") as archivo:
	for persona in personas:
		archivo.write(",".join([str(elem) for elem in persona]) + "\n")


print("Los datos han sido guardos en Lista.txt")


