
from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Entidad(ABC):

    def __init__(self, identificador):
        if not isinstance(identificador, str) or len(identificador.strip()) < 2:
            raise DatosInvalidosError(
                "El identificador debe contener al menos dos caracteres."
            )

        self.__identificador = identificador.strip()

    @property
    def identificador(self):
        return self.__identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass
