from Logica.entidades import Medico, Cita, GestorClinica

def iniciar_agenda():
    gestor = GestorClinica()
    
    while True:
        print("\n" + "="*35)
        print("   SISTEMA DE AGENDA MÉDICA")
        print("="*35)
        print("1. Registrar Cita")
        print("2. Mostrar Agenda de Paciente")
        print("3. Salir")
        print("-" * 35)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- DATOS DEL PACIENTE ---")
            id_paciente = input("ID del Paciente: ")
            nom_paciente = input("Nombre del Paciente: ")
            
            print("\n--- DATOS DEL MÉDICO ---")
            nom_medico = input("Nombre del Médico: ")
            esp_medico = input("Especialidad: ")
            id_medico = input("ID Registro Médico: ")

            medico_objetivo = Medico(nom_medico, esp_medico, id_medico)
            
            print("\n--- DATOS DE LA CITA ---")
            fecha = input("Fecha (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")

            cita_objetivo = Cita(fecha, hora, medico_objetivo)
            
            # Procesar cita
            exito, msj = gestor.programar_cita(id_paciente, cita_objetivo, nom_paciente)
            print(f"\n>> {msj}")

        elif opcion == "2":
            id_paciente = input("\nIngrese el ID del paciente: ")

            if id_paciente in gestor.diccionario_pacientes:
                paciente = gestor.diccionario_pacientes[id_paciente]
                print(f"\nAgenda de: {paciente.nombre_paciente}")
                print("-" * 40)

                if not paciente.lista_citas:
                    print("No hay citas registradas.")
                else:
                    for c in paciente.lista_citas:
                        # Corregido: c.medico es el objeto Medico dentro de la Cita
                        print(f"Fecha: {c.fecha} | Hora: {c.hora} | Dr. {c.medico.nombre_medico} ({c.medico.especialidad})")
            else:
                print("\n>> Paciente no encontrado.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    iniciar_agenda()