
from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    CalculoInvalidoError
)


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        try:
            if cliente is None:
                raise ReservaInvalidaError(
                    "Debe seleccionar un cliente valido."
                )

            if servicio is None:
                raise ReservaInvalidaError(
                    "Debe seleccionar un servicio valido."
                )

            if not isinstance(duracion, (int, float)) or isinstance(duracion, bool):
                raise ReservaInvalidaError(
                    "La duracion debe ser un valor numerico."
                )

            if duracion <= 0:
                raise ReservaInvalidaError(
                    "La duracion debe ser mayor que cero."
                )

            servicio.validar_parametros()
            servicio.validar_disponibilidad(1)

            self.__cliente = cliente
            self.__servicio = servicio
            self.__duracion = duracion
            self.__estado = "Pendiente"
            self.__costo = 0

        except ReservaInvalidaError:
            raise

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible crear la reserva."
            ) from error

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        try:
            if self.__estado != "Pendiente":
                raise ReservaInvalidaError(
                    "Solo se pueden confirmar reservas pendientes."
                )

            self.__servicio.validar_disponibilidad(1)
            self.__servicio.actualizar_disponibilidad(-1)

            self.__estado = "Confirmada"

        except ReservaInvalidaError:
            raise

        except Exception as error:
            raise ServicioNoDisponibleError(
                "No fue posible confirmar la reserva."
            ) from error

    def cancelar(self):
        try:
            if self.__estado in ("Cancelada", "Procesada"):
                raise ReservaInvalidaError(
                    "No se puede cancelar una reserva cancelada o procesada."
                )

            if self.__estado == "Confirmada":
                self.__servicio.actualizar_disponibilidad(1)

            self.__estado = "Cancelada"

        except ReservaInvalidaError:
            raise

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible cancelar la reserva."
            ) from error

    def procesar(self, impuesto=19, descuento=0):
        try:
            if self.__estado != "Confirmada":
                raise CalculoInvalidoError(
                    "Solo se pueden procesar reservas confirmadas."
                )

            if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool):
                raise CalculoInvalidoError(
                    "El impuesto debe ser numerico."
                )

            if not isinstance(descuento, (int, float)) or isinstance(descuento, bool):
                raise CalculoInvalidoError(
                    "El descuento debe ser numerico."
                )

            if impuesto < 0 or descuento < 0 or descuento > 100:
                raise CalculoInvalidoError(
                    "El impuesto o descuento tiene un valor no permitido."
                )

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

            if self.__costo <= 0:
                raise CalculoInvalidoError(
                    "El costo calculado debe ser mayor que cero."
                )

            self.__estado = "Procesada"

            return self.__costo

        except CalculoInvalidoError:
            raise

        except Exception as error:
            raise CalculoInvalidoError(
                "Ocurrio un error al calcular el costo de la reserva."
            ) from error

    def __str__(self):
        return (
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} | "
            f"Estado: {self.__estado} | "
            f"Costo: ${self.__costo:.2f}"
        )

