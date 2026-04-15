from Logica.Mascota import Perro, Gato

def registrar_mascota():
    print("Registra una mascota")
    print("Selecciona el tipo de mascota:")
    print("1. Perro")
    print("2. Gato")

    opcion = input("Elige el tipo de mascota: ")
    nombre = input("Ingresa el nombre de tu mascota: ")
    edad = int(input("Ingresa la edad cronológica de tu mascota: "))

    if opcion == '1':
        tamaño = input("Ingresa el tamaño (pequeño, mediano, grande): ")
        mi_mascota = Perro(nombre, edad, tamaño)

    elif opcion == '2':
        mi_mascota = Gato(nombre, edad)

    else:
        print("Opción inválida")
        return

    print(f"Has registrado a {mi_mascota.nombre} con {mi_mascota.edad_cronologica} años cronológicos.")

    edad_humana = mi_mascota.calcular_edad_humana()
    print(f"La edad humana de {mi_mascota.nombre} es: {edad_humana} años.")