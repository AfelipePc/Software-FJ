
# ============================================
# SOFTWARE FJ
# Sistema Integral de Gestion de Clientes,
# Servicios y Reservas
# Archivo: entidades.py
# ============================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador no puede estar vacio.")

        self.__identificador = identificador

    @property
    def identificador(self):
        return self.__identificador

    @abstractmethod
    def mostrar_informacion(self):
        """
        Metodo abstracto que debe ser implementado
        por las clases derivadas.
        """
        pass
