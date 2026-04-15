from Logica.entidades import paciente, gestion_paciente

def menu():
    gestion = gestion_paciente()
    
    while True:
        print("\n| Sistema de Gestion de Salud |")
        print("1. Registrar Paciente")
        print("2. Ver Lista de Pacientes")
        print("3. Actualizar Peso/Altura")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            if edad < 0:
                print("Edad no puede ser negativa.")
                continue
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))
            
            nuevo_paciente = paciente(nombre, apellido, edad, peso, altura)
            gestion.agregar_paciente(nuevo_paciente)
            print(f"\n¡Paciente {nombre} {apellido} registrado con éxito!")

        elif opcion == "2":
            if not gestion.lista_pacientes:
                print("\nNo hay pacientes registrados.")
            else:
                print("\n| LISTA DE PACIENTES |")
                for paciente_encontrado in gestion.lista_pacientes:
                    imc = paciente_encontrado.calcular_imc()
                    estado = paciente_encontrado.obtener_estado()
                    print(f"Nombre: {paciente_encontrado.nombre} {paciente_encontrado.apellido} | Edad: {paciente_encontrado.edad} | Peso: {paciente_encontrado.peso}kg | Altura: {paciente_encontrado.altura}m | IMC: {imc:.2f} | Estado: {estado}")

        elif opcion == "3":
            apellido_buscar = input("Ingrese el apellido del paciente a actualizar: ")
            paciente_encontrado = gestion.buscar_paciente(apellido_buscar)
            if paciente_encontrado:
                nuevo_peso = float(input(f"Nuevo peso para {paciente_encontrado.nombre} (actual: {paciente_encontrado.peso}kg): "))
                nueva_altura = float(input(f"Nueva altura para {paciente_encontrado.nombre} (actual: {paciente_encontrado.altura}m): "))
                gestion.actualizar_datos(apellido_buscar, nuevo_peso, nueva_altura)
                print("¡Datos actualizados correctamente!")
            else:
                print("Paciente no encontrado.")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")
