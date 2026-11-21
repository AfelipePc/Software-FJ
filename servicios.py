
# ==================================================
# SOFTWARE FJ
# Sistema Integral de Gestion de Clientes,
# Servicios y Reservas
# Archivo: servicios.py
# ==================================================

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Servicio(ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, nombre, precio_base, disponibilidad):
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool) or precio_base <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero.")

        if not isinstance(disponibilidad, int) or isinstance(disponibilidad, bool) or disponibilidad < 0:
            raise DatosInvalidosError("La disponibilidad debe ser un entero no negativo.")

        self.__nombre = nombre.strip()
        self.__precio_base = precio_base
        self.__disponibilidad = disponibilidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    @property
    def disponibilidad(self):
        return self.__disponibilidad

    def validar_disponibilidad(self, cantidad=1):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise DatosInvalidosError("La cantidad debe ser un entero positivo.")

        if cantidad > self.__disponibilidad:
            raise DatosInvalidosError("No hay disponibilidad suficiente.")

        return True

    def actualizar_disponibilidad(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise DatosInvalidosError("La cantidad debe ser un numero entero.")

        nueva_disponibilidad = self.__disponibilidad + cantidad

        if nueva_disponibilidad < 0:
            raise DatosInvalidosError("La disponibilidad no puede ser negativa.")

        self.__disponibilidad = nueva_disponibilidad

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo con parametros opcionales
        para impuestos y descuentos.
        """
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("La duracion debe ser mayor que cero.")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not 0 <= descuento <= 100:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 100.")

        subtotal = self.__precio_base * duracion
        valor_descuento = subtotal * descuento / 100
        subtotal_con_descuento = subtotal - valor_descuento

        return subtotal_con_descuento * (1 + impuesto / 100)

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    def __str__(self):
        return self.describir_servicio()


class ReservaSala(Servicio):
    """Servicio especializado en reserva de salas."""

    def __init__(self, nombre, precio_base, disponibilidad, capacidad=10):
        super().__init__(nombre, precio_base, disponibilidad)

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un entero positivo.")

        self.__capacidad = capacidad

    def validar_parametros(self):
        return self.__capacidad > 0

    def describir_servicio(self):
        return (
            f"Reserva de sala: {self.nombre} | "
            f"Precio por hora: ${self.precio_base:,.0f} | "
            f"Capacidad: {self.__capacidad} personas | "
            f"Disponibilidad: {self.disponibilidad}"
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, nombre, precio_base, disponibilidad, tipo_equipo="Computador"):
        super().__init__(nombre, precio_base, disponibilidad)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError("El tipo de equipo es obligatorio.")

        self.__tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self):
        return bool(self.__tipo_equipo)

    def describir_servicio(self):
        return (
            f"Alquiler de equipo: {self.nombre} | "
            f"Precio por hora: ${self.precio_base:,.0f} | "
            f"Tipo: {self.__tipo_equipo} | "
            f"Disponibilidad: {self.disponibilidad}"
        )


class Asesoria(Servicio):
    """Servicio especializado en asesorias profesionales."""

    def __init__(self, nombre, precio_base, disponibilidad, especialidad="Software"):
        super().__init__(nombre, precio_base, disponibilidad)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("La especialidad es obligatoria.")

        self.__especialidad = especialidad.strip()

    def validar_parametros(self):
        return bool(self.__especialidad)

    def describir_servicio(self):
        return (
            f"Asesoria especializada: {self.nombre} | "
            f"Precio por hora: ${self.precio_base:,.0f} | "
            f"Especialidad: {self.__especialidad} | "
            f"Disponibilidad: {self.disponibilidad}"
        )
