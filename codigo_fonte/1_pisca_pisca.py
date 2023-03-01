"""
Exemplo de pisca pisca com delay de 0.5
"""

from pyfirmata import Arduino, OUTPUT
from constantes import PORTA_COMUNICACAO, PINO_13

arduino = Arduino(PORTA_COMUNICACAO)
arduino.digital[PINO_13].mode = OUTPUT

while True:
    arduino.digital[PINO_13].write(1)
    arduino.pass_time(0.5)
    arduino.digital[PINO_13].write(0)
    arduino.pass_time(0.5)
