
class ErrorSoftwareFJ(Exception):
    """Excepcion general del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSoftwareFJ):
    """Error cuando los datos ingresados no son validos."""
    pass


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Error cuando no se encuentra un cliente."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Error cuando un servicio no tiene disponibilidad."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Error cuando una reserva no cumple las condiciones."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Error cuando se intenta realizar una operacion no permitida."""
    pass


class CalculoInvalidoError(ErrorSoftwareFJ):
    """Error cuando ocurre un problema en un calculo."""
    pass
