
import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise DatosInvalidosError(
                "El nombre debe contener al menos tres caracteres."
            )

        if not isinstance(documento, str) or not documento.isdigit() or len(documento) < 5:
            raise DatosInvalidosError(
                "El documento debe contener minimo cinco digitos."
            )

        if not isinstance(correo, str) or not re.match(
            r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", correo
        ):
            raise DatosInvalidosError("El correo electronico no es valido.")

        if not isinstance(telefono, str) or not telefono.isdigit() or not 7 <= len(telefono) <= 15:
            raise DatosInvalidosError(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        self.__nombre = nombre.strip()
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

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

    def mostrar_informacion(self):
        return (
            f"Identificacion: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )

    def __str__(self):
        return (
            f"{self.__nombre} | Documento: {self.__documento} | "
            f"Correo: {self.__correo} | Telefono: {self.__telefono}"
        )

