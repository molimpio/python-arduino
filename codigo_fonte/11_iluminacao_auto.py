"""
Exemplo que acende o led conforme acionamento do sensor
"""

from pyfirmata import Arduino, util
from constantes import PORTA_COMUNICACAO, ANALOG_0, PINO_13

arduino = Arduino(PORTA_COMUNICACAO)

iterator = util.Iterator(arduino)
iterator.start()

arduino.analog[ANALOG_0].enable_reporting()

while True:
    valor = str(arduino.analog[ANALOG_0].read())

    if valor != "None":
        valor = float(valor)

        if valor < 0.001:
            arduino.digital[PINO_13].write(1)
        else:
            arduino.digital[PINO_13].write(0)

        arduino.pass_time(1)