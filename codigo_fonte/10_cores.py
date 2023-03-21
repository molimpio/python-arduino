"""
Exemplo que acende os leds com acionamento do push button.
"""

from pyfirmata import Arduino, PWM
from constantes import PORTA_COMUNICACAO, PINO_9, PINO_6, PINO_5
from random import random

arduino = Arduino(PORTA_COMUNICACAO)
vermelho = PINO_9
azul = PINO_6
verde = PINO_5

arduino.digital[vermelho].mode = PWM
arduino.digital[azul].mode = PWM
arduino.digital[verde].mode = PWM

while True:
    arduino.digital[vermelho].write(random())
    arduino.digital[azul].write(random())
    arduino.digital[verde].write(random())
    arduino.pass_time(2.0)
