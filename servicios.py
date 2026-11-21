

from abc import ABC, abstractmethod
from excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError
)


class Servicio(ABC):

    def __init__(self, nombre, precio_base, disponibilidad):
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre del servicio no es valido.")

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool):
            raise DatosInvalidosError("El precio debe ser numerico.")

        if precio_base <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero.")

        if not isinstance(disponibilidad, int) or isinstance(disponibilidad, bool):
            raise DatosInvalidosError("La disponibilidad debe ser un numero entero.")

        if disponibilidad < 0:
            raise DatosInvalidosError("La disponibilidad no puede ser negativa.")

        self.__nombre = nombre
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
        if cantidad <= 0:
            raise ServicioNoDisponibleError(
                "La cantidad solicitada debe ser mayor que cero."
            )

        if self.__disponibilidad < cantidad:
            raise ServicioNoDisponibleError(
                "No hay disponibilidad suficiente para este servicio."
            )

        return True

    def actualizar_disponibilidad(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise DatosInvalidosError(
                "La cantidad debe ser un numero entero."
            )

        nueva_disponibilidad = self.__disponibilidad + cantidad

        if nueva_disponibilidad < 0:
            raise ServicioNoDisponibleError(
                "No se puede reducir mas la disponibilidad."
            )

        self.__disponibilidad = nueva_disponibilidad

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
            raise DatosInvalidosError("La duracion debe ser numerica.")

        if duracion <= 0:
            raise DatosInvalidosError("La duracion debe ser mayor que cero.")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
            raise DatosInvalidosError("El impuesto debe ser numerico.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
            raise DatosInvalidosError("El descuento debe ser numerico.")

        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise DatosInvalidosError(
                "El impuesto o descuento tiene un valor no permitido."
            )

        subtotal = self.__precio_base * duracion
        valor_descuento = subtotal * (descuento / 100)
        subtotal_con_descuento = subtotal - valor_descuento
        valor_impuesto = subtotal_con_descuento * (impuesto / 100)

        total = subtotal_con_descuento + valor_impuesto

        return round(total, 2)

    def calcular_costo_basico(self, duracion):
        return self.calcular_costo(duracion)

    def calcular_costo_con_impuesto(self, duracion, impuesto):
        return self.calcular_costo(duracion, impuesto)

    def calcular_costo_con_descuento(self, duracion, descuento):
        return self.calcular_costo(duracion, 0, descuento)

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    def __str__(self):
        return (
            f"{self.__nombre} | "
            f"Precio: ${self.__precio_base:.2f} | "
            f"Disponibilidad: {self.__disponibilidad} | "
            f"{self.describir_servicio()}"
        )


class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, disponibilidad, capacidad=10):
        super().__init__(nombre, precio_base, disponibilidad)
        self.__capacidad = capacidad
        self.validar_parametros()

    @property
    def capacidad(self):
        return self.__capacidad

    def validar_parametros(self):
        if not isinstance(self.__capacidad, int) or isinstance(self.__capacidad, bool):
            raise DatosInvalidosError("La capacidad debe ser un numero entero.")

        if self.__capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser mayor que cero.")

        return True

    def describir_servicio(self):
        return f"Reserva de sala - Capacidad: {self.__capacidad} personas"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, disponibilidad, tipo_equipo="Computador"):
        super().__init__(nombre, precio_base, disponibilidad)
        self.__tipo_equipo = tipo_equipo
        self.validar_parametros()

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    def validar_parametros(self):
        if not isinstance(self.__tipo_equipo, str) or len(self.__tipo_equipo.strip()) < 2:
            raise DatosInvalidosError("El tipo de equipo no es valido.")

        return True

    def describir_servicio(self):
        return f"Alquiler de equipo - Tipo: {self.__tipo_equipo}"


class Asesoria(Servicio):

    def __init__(self, nombre, precio_base, disponibilidad, especialidad="Software"):
        super().__init__(nombre, precio_base, disponibilidad)
        self.__especialidad = especialidad
        self.validar_parametros()

    @property
    def especialidad(self):
        return self.__especialidad

    def validar_parametros(self):
        if not isinstance(self.__especialidad, str) or len(self.__especialidad.strip()) < 2:
            raise DatosInvalidosError("La especialidad no es valida.")

        return True

    def describir_servicio(self):
        return f"Asesoria especializada - Especialidad: {self.__especialidad}"
