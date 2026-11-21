
# ==================================================
# SOFTWARE FJ
# Sistema Integral de Gestion de Clientes,
# Servicios y Reservas
# Archivo: reservas.py
# ==================================================

from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    CalculoInvalidoError
)


class Reserva:
    """
    Clase encargada de gestionar las reservas
    realizadas por los clientes de Software FJ.
    """

    def __init__(self, cliente, servicio, duracion):

        if cliente is None:
            raise ReservaInvalidaError("Debe seleccionar un cliente.")

        if servicio is None:
            raise ReservaInvalidaError("Debe seleccionar un servicio.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaInvalidaError(
                "La duracion debe ser un numero mayor que cero."
            )

        if not servicio.validar_parametros():
            raise ReservaInvalidaError(
                "Los parametros del servicio no son validos."
            )

        servicio.validar_disponibilidad(1)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0

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
        """
        Confirma la reserva y actualiza
        la disponibilidad del servicio.
        """

        if self.__estado != "Pendiente":
            raise ReservaInvalidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self.__servicio.validar_disponibilidad(1)

            self.__servicio.actualizar_disponibilidad(-1)

            self.__estado = "Confirmada"

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible confirmar la reserva."
            ) from error

    def cancelar(self):
        """
        Cancela una reserva y devuelve la disponibilidad
        cuando la reserva ya estaba confirmada.
        """

        if self.__estado in ("Cancelada", "Procesada"):
            raise ReservaInvalidaError(
                "La reserva no puede cancelarse en su estado actual."
            )

        try:
            if self.__estado == "Confirmada":
                self.__servicio.actualizar_disponibilidad(1)

            self.__estado = "Cancelada"

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible cancelar la reserva."
            ) from error

    def procesar(self, impuesto=19, descuento=0):
        """
        Procesa la reserva y calcula su costo final.
        """

        if self.__estado != "Confirmada":
            raise ReservaInvalidaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                impuesto,
                descuento
            )

            if self.__costo <= 0:
                raise CalculoInvalidoError(
                    "El costo calculado no es valido."
                )

            self.__estado = "Procesada"

            return self.__costo

        except Exception as error:
            raise CalculoInvalidoError(
                "Error durante el procesamiento de la reserva."
            ) from error

    def __str__(self):
        return (
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} horas | "
            f"Estado: {self.__estado} | "
            f"Costo: ${self.__costo:,.0f}"
        )
