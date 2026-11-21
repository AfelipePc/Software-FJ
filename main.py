
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    CalculoInvalidoError
)
from registro_logs import registrar_evento, registrar_error


class SistemaSoftwareFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        registrar_evento("Sistema Software FJ iniciado correctamente.")

    def registrar_cliente(self):
        try:
            print("\n--- REGISTRO DE CLIENTE ---")
            identificador = input("Identificacion: ")
            nombre = input("Nombre completo: ")
            documento = input("Documento: ")
            correo = input("Correo electronico: ")
            telefono = input("Telefono: ")

            cliente = Cliente(
                identificador, nombre, documento, correo, telefono
            )

            self.clientes.append(cliente)

        except (DatosInvalidosError, ValueError) as error:
            registrar_error(f"Error al registrar cliente: {error}")
            print("No se pudo registrar el cliente:", error)

        else:
            registrar_evento("Cliente registrado correctamente.")
            print("Cliente registrado con exito.")

        finally:
            print("Operacion de registro finalizada.")

    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)

    def crear_servicio(self):
        try:
            print("\n--- CREAR SERVICIO ---")
            print("1. Reserva de sala")
            print("2. Alquiler de equipos")
            print("3. Asesoria especializada")

            opcion = input("Seleccione el tipo de servicio: ")
            nombre = input("Nombre del servicio: ")
            precio = float(input("Precio base: "))
            disponibilidad = int(input("Cantidad disponible: "))

            if opcion == "1":
                capacidad = int(input("Capacidad de la sala: "))
                servicio = ReservaSala(
                    nombre, precio, disponibilidad, capacidad
                )

            elif opcion == "2":
                tipo = input("Tipo de equipo: ")
                servicio = AlquilerEquipo(
                    nombre, precio, disponibilidad, tipo
                )

            elif opcion == "3":
                especialidad = input("Especialidad: ")
                servicio = Asesoria(
                    nombre, precio, disponibilidad, especialidad
                )

            else:
                raise DatosInvalidosError("Tipo de servicio no valido.")

            servicio.validar_parametros()
            self.servicios.append(servicio)

        except (DatosInvalidosError, ValueError) as error:
            registrar_error(f"Error al crear servicio: {error}")
            print("No se pudo crear el servicio:", error)

        else:
            registrar_evento("Servicio creado correctamente.")
            print("Servicio creado con exito.")

        finally:
            print("Operacion de servicio finalizada.")

    def mostrar_servicios(self):
        print("\n--- SERVICIOS DISPONIBLES ---")
        if not self.servicios:
            print("No hay servicios registrados.")
        else:
            for indice, servicio in enumerate(self.servicios, start=1):
                print(f"{indice}. {servicio}")

    def crear_reserva(self):
        try:
            if not self.clientes or not self.servicios:
                raise ReservaInvalidaError(
                    "Primero debe registrar clientes y servicios."
                )

            self.mostrar_clientes()
            posicion_cliente = int(input("Numero del cliente: ")) - 1

            self.mostrar_servicios()
            posicion_servicio = int(input("Numero del servicio: ")) - 1

            cliente = self.clientes[posicion_cliente]
            servicio = self.servicios[posicion_servicio]
            duracion = float(input("Duracion de la reserva: "))

            reserva = Reserva(cliente, servicio, duracion)
            self.reservas.append(reserva)

        except (ValueError, IndexError, ReservaInvalidaError) as error:
            registrar_error(f"Error al crear reserva: {error}")
            print("No se pudo crear la reserva:", error)

        else:
            registrar_evento("Reserva creada correctamente.")
            print("Reserva creada con exito.")

        finally:
            print("Operacion de reserva finalizada.")

    def mostrar_reservas(self):
        print("\n--- RESERVAS REGISTRADAS ---")
        if not self.reservas:
            print("No hay reservas registradas.")
        else:
            for indice, reserva in enumerate(self.reservas, start=1):
                print(f"{indice}. {reserva}")

    def confirmar_reserva(self):
        try:
            self.mostrar_reservas()
            posicion = int(input("Numero de la reserva: ")) - 1
            reserva = self.reservas[posicion]
            reserva.confirmar()

        except (ValueError, IndexError, ReservaInvalidaError) as error:
            registrar_error(f"Error al confirmar reserva: {error}")
            print("No se pudo confirmar la reserva:", error)

        else:
            registrar_evento("Reserva confirmada correctamente.")
            print("Reserva confirmada.")

        finally:
            print("Operacion de confirmacion finalizada.")

    def cancelar_reserva(self):
        try:
            self.mostrar_reservas()
            posicion = int(input("Numero de la reserva: ")) - 1
            reserva = self.reservas[posicion]
            reserva.cancelar()

        except (ValueError, IndexError, ReservaInvalidaError) as error:
            registrar_error(f"Error al cancelar reserva: {error}")
            print("No se pudo cancelar la reserva:", error)

        else:
            registrar_evento("Reserva cancelada correctamente.")
            print("Reserva cancelada.")

        finally:
            print("Operacion de cancelacion finalizada.")

    def procesar_reserva(self):
        try:
            self.mostrar_reservas()
            posicion = int(input("Numero de la reserva: ")) - 1
            reserva = self.reservas[posicion]

            impuesto = float(input("Porcentaje de impuesto (ej. 19): "))
            descuento = float(input("Porcentaje de descuento (ej. 0): "))

            costo = reserva.procesar(impuesto, descuento)

        except (ValueError, IndexError, CalculoInvalidoError) as error:
            registrar_error(f"Error al procesar reserva: {error}")
            print("No se pudo procesar la reserva:", error)

        else:
            registrar_evento("Reserva procesada correctamente.")
            print(f"Reserva procesada. Costo total: ${costo:.2f}")

        finally:
            print("Operacion de procesamiento finalizada.")

    def pruebas_simuladas(self):
        print("\n--- PRUEBAS SIMULADAS ---")
        operaciones = 0

        # Prueba 1: crear cliente valido
        try:
            cliente = Cliente(
                "C100", "Carlos Perez", "12345678",
                "carlos@gmail.com", "3001234567"
            )
            self.clientes.append(cliente)
            print("Prueba 1: cliente valido registrado.")
        except Exception as error:
            registrar_error(f"Prueba 1: {error}")
            print("Prueba 1 fallida:", error)
        else:
            operaciones += 1

        # Prueba 2: crear cliente con datos invalidos
        try:
            Cliente("C101", "A", "123", "correo", "12")
        except Exception as error:
            print("Prueba 2: datos invalidos detectados.")
            registrar_error(f"Prueba 2: {error}")
        else:
            operaciones += 1
            print("Prueba 2: no se detecto el error esperado.")

        # Prueba 3: crear una sala
        try:
            sala = ReservaSala("Sala principal", 50000, 3, 20)
            self.servicios.append(sala)
            print("Prueba 3: sala creada.")
        except Exception as error:
            registrar_error(f"Prueba 3: {error}")
            print("Prueba 3 fallida:", error)
        else:
            operaciones += 1

        # Prueba 4: crear alquiler de equipo
        try:
            equipo = AlquilerEquipo("Portatil", 30000, 5, "Computador")
            self.servicios.append(equipo)
            print("Prueba 4: equipo creado.")
        except Exception as error:
            registrar_error(f"Prueba 4: {error}")
            print("Prueba 4 fallida:", error)
        else:
            operaciones += 1

        # Prueba 5: crear asesoria
        try:
            asesoria = Asesoria("Asesoria Python", 80000, 4, "Programacion")
            self.servicios.append(asesoria)
            print("Prueba 5: asesoria creada.")
        except Exception as error:
            registrar_error(f"Prueba 5: {error}")
            print("Prueba 5 fallida:", error)
        else:
            operaciones += 1

        # Prueba 6: crear reserva valida
        try:
            reserva = Reserva(cliente, sala, 2)
            self.reservas.append(reserva)
            print("Prueba 6: reserva creada.")
        except Exception as error:
            registrar_error(f"Prueba 6: {error}")
            print("Prueba 6 fallida:", error)
        else:
            operaciones += 1

        # Prueba 7: confirmar reserva
        try:
            reserva.confirmar()
            print("Prueba 7: reserva confirmada.")
        except Exception as error:
            registrar_error(f"Prueba 7: {error}")
            print("Prueba 7 fallida:", error)
        else:
            operaciones += 1

        # Prueba 8: procesar reserva
        try:
            costo = reserva.procesar(19, 0)
            print(f"Prueba 8: reserva procesada. Total: ${costo:.2f}")
        except Exception as error:
            registrar_error(f"Prueba 8: {error}")
            print("Prueba 8 fallida:", error)
        else:
            operaciones += 1

        # Prueba 9: intentar confirmar nuevamente
        try:
            reserva.confirmar()
        except Exception as error:
            print("Prueba 9: operacion no permitida detectada.")
            registrar_error(f"Prueba 9: {error}")
        else:
            operaciones += 1
            print("Prueba 9: se esperaba un error.")

        # Prueba 10: cancelar una reserva procesada
        try:
            reserva.cancelar()
        except Exception as error:
            print("Prueba 10: cancelacion no permitida detectada.")
            registrar_error(f"Prueba 10: {error}")
        else:
            operaciones += 1
            print("Prueba 10: se esperaba un error.")

        print(f"\nPruebas completadas. Operaciones correctas: {operaciones}")
        registrar_evento("Finalizaron las pruebas simuladas.")

    def ejecutar(self):
        while True:
            print("\n========== SOFTWARE FJ ==========")
            print("1. Registrar cliente")
            print("2. Mostrar clientes")
            print("3. Crear servicio")
            print("4. Mostrar servicios")
            print("5. Crear reserva")
            print("6. Mostrar reservas")
            print("7. Confirmar reserva")
            print("8. Cancelar reserva")
            print("9. Procesar reserva")
            print("10. Ejecutar pruebas simuladas")
            print("0. Salir")

            try:
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    self.registrar_cliente()
                elif opcion == "2":
                    self.mostrar_clientes()
                elif opcion == "3":
                    self.crear_servicio()
                elif opcion == "4":
                    self.mostrar_servicios()
                elif opcion == "5":
                    self.crear_reserva()
                elif opcion == "6":
                    self.mostrar_reservas()
                elif opcion == "7":
                    self.confirmar_reserva()
                elif opcion == "8":
                    self.cancelar_reserva()
                elif opcion == "9":
                    self.procesar_reserva()
                elif opcion == "10":
                    self.pruebas_simuladas()
                elif opcion == "0":
                    print("Gracias por utilizar Software FJ.")
                    registrar_evento("Sistema Software FJ finalizado.")
                    break
                else:
                    print("Opcion no valida. Intente nuevamente.")

            except KeyboardInterrupt:
                print("\nEjecucion interrumpida por el usuario.")
                registrar_error("Ejecucion interrumpida por el usuario.")
                break

            except Exception as error:
                registrar_error(f"Error inesperado: {error}")
                print("Se presento un error inesperado:", error)


if __name__ == "__main__":
    sistema = SistemaSoftwareFJ()
    sistema.ejecutar()

    input("\nPresione Enter para finalizar...")


