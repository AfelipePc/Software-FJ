
# ==================================================
# SOFTWARE FJ
# Sistema Integral de Gestion de Clientes,
# Servicios y Reservas
# Archivo principal: main.py
# ==================================================

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from registro_logs import registrar_evento, registrar_error


class SistemaSoftwareFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

        registrar_evento("Sistema Software FJ iniciado.")

    def mostrar_menu(self):
        print("\n====================================")
        print("       SISTEMA SOFTWARE FJ")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Crear servicios")
        print("4. Mostrar servicios")
        print("5. Crear reserva")
        print("6. Mostrar reservas")
        print("7. Confirmar reserva")
        print("8. Cancelar reserva")
        print("9. Ejecutar pruebas del sistema")
        print("0. Salir")
        print("====================================")

    def registrar_cliente(self):
        try:
            nombre = input("Nombre del cliente: ")
            documento = input("Documento: ")
            correo = input("Correo electronico: ")
            telefono = input("Telefono: ")

            cliente = Cliente(nombre, documento, correo, telefono)
            self.clientes.append(cliente)

            registrar_evento("Cliente registrado correctamente.")
            print("Cliente registrado exitosamente.")

        except Exception as error:
            registrar_error(f"Error al registrar cliente: {error}")
            print(f"No fue posible registrar el cliente: {error}")

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        for cliente in self.clientes:
            print(cliente)

    def crear_servicios(self):
        print("\nTIPOS DE SERVICIOS")
        print("1. Reserva de salas")
        print("2. Alquiler de equipos")
        print("3. Asesorias especializadas")

        try:
            opcion = input("Seleccione un servicio: ")

            if opcion == "1":
                servicio = ReservaSala(
                    "Sala de reuniones",
                    50000,
                    10
                )

            elif opcion == "2":
                servicio = AlquilerEquipo(
                    "Computador portatil",
                    30000,
                    5
                )

            elif opcion == "3":
                servicio = Asesoria(
                    "Asesoria de software",
                    80000,
                    2
                )

            else:
                raise ValueError("Tipo de servicio incorrecto.")

            self.servicios.append(servicio)
            registrar_evento("Servicio creado correctamente.")
            print("Servicio creado exitosamente.")

        except Exception as error:
            registrar_error(f"Error al crear servicio: {error}")
            print(f"No fue posible crear el servicio: {error}")

    def mostrar_servicios(self):
        if not self.servicios:
            print("No hay servicios registrados.")
            return

        for indice, servicio in enumerate(self.servicios, start=1):
            print(f"{indice}. {servicio}")

    def crear_reserva(self):
        try:
            if not self.clientes or not self.servicios:
                print("Primero registre clientes y servicios.")
                return

            self.mostrar_clientes()

            indice_cliente = int(input("Numero del cliente: ")) - 1

            if indice_cliente < 0 or indice_cliente >= len(self.clientes):
                raise ValueError("Cliente inexistente.")

            self.mostrar_servicios()

            indice_servicio = int(input("Numero del servicio: ")) - 1

            if indice_servicio < 0 or indice_servicio >= len(self.servicios):
                raise ValueError("Servicio inexistente.")

            duracion = float(input("Duracion del servicio: "))

            reserva = Reserva(
                self.clientes[indice_cliente],
                self.servicios[indice_servicio],
                duracion
            )

            self.reservas.append(reserva)

            registrar_evento("Reserva creada correctamente.")
            print("Reserva creada exitosamente.")

        except Exception as error:
            registrar_error(f"Error al crear reserva: {error}")
            print(f"No fue posible crear la reserva: {error}")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return

        for indice, reserva in enumerate(self.reservas, start=1):
            print(f"{indice}. {reserva}")

    def cambiar_estado_reserva(self, confirmar=True):
        try:
            self.mostrar_reservas()

            if not self.reservas:
                return

            numero = int(input("Numero de reserva: ")) - 1

            if numero < 0 or numero >= len(self.reservas):
                raise ValueError("Reserva inexistente.")

            reserva = self.reservas[numero]

            if confirmar:
                reserva.confirmar()
                print("Reserva confirmada.")
            else:
                reserva.cancelar()
                print("Reserva cancelada.")

            registrar_evento("Estado de reserva actualizado.")

        except Exception as error:
            registrar_error(f"Error al modificar reserva: {error}")
            print(f"No fue posible modificar la reserva: {error}")

    def ejecutar(self):
        while True:
            try:
                self.mostrar_menu()
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    self.registrar_cliente()

                elif opcion == "2":
                    self.mostrar_clientes()

                elif opcion == "3":
                    self.crear_servicios()

                elif opcion == "4":
                    self.mostrar_servicios()

                elif opcion == "5":
                    self.crear_reserva()

                elif opcion == "6":
                    self.mostrar_reservas()

                elif opcion == "7":
                    self.cambiar_estado_reserva(True)

                elif opcion == "8":
                    self.cambiar_estado_reserva(False)

                elif opcion == "9":
                    print("Las pruebas se implementaran en el modulo correspondiente.")

                elif opcion == "0":
                    registrar_evento("Sistema Software FJ finalizado.")
                    print("Gracias por utilizar Software FJ.")
                    break

                else:
                    print("Opcion no valida. Intente nuevamente.")

            except Exception as error:
                registrar_error(f"Error general del sistema: {error}")
                print(f"Se presento un error controlado: {error}")


if __name__ == "__main__":
    sistema = SistemaSoftwareFJ()
    sistema.ejecutar()

