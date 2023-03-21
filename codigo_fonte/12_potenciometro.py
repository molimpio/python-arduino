"""
Exemplo que pisca o led conforme giro do potenciometro.
"""

from pyfirmata import Arduino, OUTPUT, util
from constantes import PORTA_COMUNICACAO, ANALOG_0, PINO_9

arduino = Arduino(PORTA_COMUNICACAO)

iterator = util.Iterator(arduino)
iterator.start()

arduino.analog[ANALOG_0].enable_reporting()
arduino.digital[PINO_9].mode = OUTPUT

estado = True

while True:
    valor = str(arduino.analog[ANALOG_0].read())

    if valor != "None":
        arduino.digital[PINO_9].write(estado)
        valor = float(valor)
        estado = not estado
        arduino.pass_time(valor)
