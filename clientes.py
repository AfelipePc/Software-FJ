
# ============================================
# SOFTWARE FJ
# Sistema Integral de Gestion de Clientes,
# Servicios y Reservas
# Archivo: clientes.py
# ============================================

import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    """
    Clase que representa a los clientes de Software FJ.
    Implementa encapsulacion y validacion de datos.
    """

    def __init__(self, nombre, documento, correo, telefono):

        # Validacion del nombre
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise DatosInvalidosError(
                "El nombre debe contener al menos 3 caracteres."
            )

        # Validacion del documento
        documento = str(documento).strip()

        if not documento.isdigit() or len(documento) < 5:
            raise DatosInvalidosError(
                "El documento debe contener al menos 5 digitos."
            )

        # Validacion del correo
        if not isinstance(correo, str) or not re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            correo.strip()
        ):
            raise DatosInvalidosError("El correo electronico no es valido.")

        # Validacion del telefono
        telefono = str(telefono).strip()

        if not telefono.isdigit() or not 7 <= len(telefono) <= 15:
            raise DatosInvalidosError(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        # Inicializacion de la clase padre
        super().__init__(documento)

        # Atributos privados
        self.__nombre = nombre.strip()
        self.__documento = documento
        self.__correo = correo.strip()
        self.__telefono = telefono

    # Metodos de acceso a los atributos privados

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # Metodo sobrescrito de la clase Entidad
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )

    def __str__(self):
        return (
            f"Cliente: {self.__nombre} | "
            f"Documento: {self.__documento} | "
            f"Correo: {self.__correo} | "
            f"Telefono: {self.__telefono}"
        )
