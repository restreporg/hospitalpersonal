from abc import ABC, abstractmethod
from datetime import date

class EmpleadoHospital(ABC):
    def __init__(self, nombre, cedula, fecha_ingreso, salario_base):
        self._nombre = nombre
        self._cedula = cedula
        self._fecha_ingreso = fecha_ingreso
        self._salario_base = self.__validar_salario(salario_base)
        self._turnos = []
        self._historial = []

    def __validar_salario(self, salario):
        if salario < 0:
            raise ValueError("El salario debe ser positivo")
        return salario

    def __calcular_bonus(self):
        años = date.today().year - self._fecha_ingreso.year
        return años * 120

    def asignar_turno(self, turno):
        self._turnos.append(turno)

    def get_salario_base(self):
        return self._salario_base

    def _get_bonus(self):
        return self.__calcular_bonus()

    @abstractmethod
    def calcular_pago_mensual(self):
        pass

    @abstractmethod
    def rol_profesional(self):
        pass

    def __str__(self):
        return f"{self._nombre} ({self._cedula}) - Ingreso: {self._fecha_ingreso}"


class MedicoGeneral(EmpleadoHospital):
    def __init__(self, nombre, cedula, fecha_ingreso, salario_base, pacientes_dia, tarifa_consulta):
        super().__init__(nombre, cedula, fecha_ingreso, salario_base)
        self.pacientes_dia = pacientes_dia
        self.tarifa_consulta = tarifa_consulta

    def calcular_pago_mensual(self):
        return self.get_salario_base() + (self.pacientes_dia * self.tarifa_consulta * 30) + self._get_bonus()

    def rol_profesional(self):
        return "Médico General"

    def atender(self):
        return "Realiza consulta médica general"


class EspecialistaMedico(EmpleadoHospital):
    def __init__(self, nombre, cedula, fecha_ingreso, salario_base, campo, experiencia, tarifa_especialidad):
        super().__init__(nombre, cedula, fecha_ingreso, salario_base)
        self.campo = campo
        self.experiencia = experiencia
        self.tarifa_especialidad = tarifa_especialidad

    def calcular_pago_mensual(self):
        return self.get_salario_base() + (self.experiencia * self.tarifa_especialidad) + self._get_bonus()

    def rol_profesional(self):
        return f"Especialista en {self.campo}"

    def atender(self):
        return f"Atiende casos especializados en {self.campo}"


class Enfermeria(EmpleadoHospital):
    def __init__(self, nombre, cedula, fecha_ingreso, salario_base, categoria, horario):
        super().__init__(nombre, cedula, fecha_ingreso, salario_base)
        self.categoria = categoria
        self.horario = horario

    def calcular_pago_mensual(self):
        extra = 400 if self.categoria == "jefe" else 150
        return self.get_salario_base() + extra + self._get_bonus()

    def rol_profesional(self):
        return f"Enfermero/a {self.categoria}"

    def atender(self):
        return f"Cuida pacientes en turno {self.horario}"


class TecnicoApoyo(EmpleadoHospital):
    def __init__(self, nombre, cedula, fecha_ingreso, salario_base, departamento, certificados):
        super().__init__(nombre, cedula, fecha_ingreso, salario_base)
        self.departamento = departamento
        self.certificados = certificados

    def calcular_pago_mensual(self):
        return self.get_salario_base() + (len(self.certificados) * 100) + self._get_bonus()

    def rol_profesional(self):
        return f"Técnico en {self.departamento}"

    def atender(self):
        return f"Apoya en área técnica: {self.departamento}"
