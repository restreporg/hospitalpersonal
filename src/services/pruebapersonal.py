from datetime import date
from src.models.empleado import MedicoGeneral, EspecialistaMedico, Enfermeria, TecnicoApoyo

def ejecutar_prueba():
    medico = MedicoGeneral("Valeria", "MG010", date(2020, 5, 12), 2100, 15, 40)
    especialista = EspecialistaMedico("Ricardo", "ESP010", date(2017, 3, 8), 3200, "Oncología", 9, 500)
    enfermero = Enfermeria("María", "ENF010", date(2021, 9, 1), 1600, "profesional", "noche")
    tecnico = TecnicoApoyo("Felipe", "TEC010", date(2019, 11, 20), 1500, "Laboratorio", ["CertX", "CertY"])

    medico.asignar_turno("Lunes mañana")
    especialista.asignar_turno("Martes tarde")
    enfermero.asignar_turno("Miércoles noche")
    tecnico.asignar_turno("Jueves mañana")

    equipo = [medico, especialista, enfermero, tecnico]

    print("---PRUEBA DE PERSONAL HOSPITALARIO ---\n")
    nomina_total = 0

    for persona in equipo:
        print(persona)
        print("Rol:", persona.rol_profesional())
        print("Acción:", persona.atender())
        print("Turnos asignados:", persona._turnos)
        pago = persona.calcular_pago_mensual()
        print("Pago mensual:", pago)
        print("-"*50)
        nomina_total += pago

    print("\nNómina total del hospital:", nomina_total)
