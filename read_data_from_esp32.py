import serial
import time
from logger import get_logger
from exceptions import ConnectionFailed

logger = get_logger()


def read_data_from_sensor(
    serial_port: int,
    baud_rate: int = 9600,
    timeout: int = 1
    ):
    """

    Args:
        serial_port (str): _description_
        baud_rate (int, optional): _description_. Defaults to 9600.
        timeout (int, optional): _description_. Defaults to 1.
    """
    logger.info("INITIALIZING SERIAL CONECTION")
    serial_conn = serial.Serial(serial_port=serial_port,
                        baud_rate=baud_rate,
                        timeout=timeout)


    if serial_conn.is_open:
        logger.info("SERIAL CONNECTION IS OPEN")
    else:
        raise ConnectionFailed("SERIAL CONECTION FAILED")

    try:
        while True:
            # Solicita dados do Arduino/ESP32
            serial_conn.write(b'GET_DATA\n')  # Comando para solicitar dados (ajuste conforme necessário)

            logger.info("reading data from esp32")
            dados = serial_conn.readline().strip().decode('utf-8')

            # Exibe os dados recebidos
            logger.info(f"DATA FROM ESP: {dados}")


            time.sleep(1)

    except KeyboardInterrupt:
        serial_conn.close()
