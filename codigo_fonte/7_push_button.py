"""
Exemplo que acende o led com acionamento do push button
"""

from pyfirmata import Arduino, OUTPUT, INPUT, util
from constantes import PORTA_COMUNICACAO, PINO_13, PINO_2

arduino = Arduino(PORTA_COMUNICACAO)
led = PINO_13
push_button = PINO_2

iterator = util.Iterator(arduino)
iterator.start()

arduino.digital[push_button].mode = INPUT
arduino.digital[led].mode = OUTPUT

while True:
    estado_botao = arduino.digital[push_button].read()
    arduino.digital[led].write(estado_botao)
