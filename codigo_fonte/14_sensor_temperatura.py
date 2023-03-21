"""
Exemplo de leitura de temperatura com conversão para graus Kelvin e Celsius
"""

from pyfirmata import Arduino, util
from math import log
from constantes import PORTA_COMUNICACAO, ANALOG_0

arduino = Arduino(PORTA_COMUNICACAO)

iterator = util.Iterator(arduino)
iterator.start()

arduino.analog[ANALOG_0].enable_reporting()

while True:
    valor = str(arduino.analog[ANALOG_0].read())

    if valor != "None":
        valor = float(valor)
        print("VALOR: ", valor)
        tempK = log(10000.0 * (1.0 / valor - 1))
        tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK)) * tempK)
        tempC = tempK - 273.15
        print("TEMP CELSIUS", tempC)
        arduino.pass_time(5.0)
