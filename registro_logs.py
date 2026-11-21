
import logging
import os

# Crear la carpeta donde se guardaran los registros
os.makedirs("logs", exist_ok=True)

# Configurar el registro de eventos y errores
logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")


def registrar_evento(mensaje):
    """Registra las operaciones realizadas correctamente."""
    try:
        logger.info(mensaje)
    except Exception as error:
        print("No fue posible registrar el evento:", error)


def registrar_error(mensaje):
    """Registra los errores presentados en el sistema."""
    try:
        logger.error(mensaje)
    except Exception as error:
        print("No fue posible registrar el error:", error)
