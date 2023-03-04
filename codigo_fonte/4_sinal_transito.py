"""
Exemplo de sinal de transito com leds vermelho, amarelo e verde
"""

from pyfirmata import Arduino, OUTPUT
from constantes import PORTA_COMUNICACAO, PINO_13, PINO_12, PINO_11

arduino = Arduino(PORTA_COMUNICACAO)
vermelho = PINO_13
amarelo = PINO_12
verde = PINO_11

arduino.digital[vermelho].mode = OUTPUT
arduino.digital[amarelo].mode = OUTPUT
arduino.digital[verde].mode = OUTPUT

while True:
    arduino.digital[vermelho].write(1)
    arduino.pass_time(5.0)
    arduino.digital[vermelho].write(0)
    arduino.digital[verde].write(1)
    arduino.pass_time(3.0)
    arduino.digital[verde].write(0)
    arduino.digital[amarelo].write(1)
    arduino.pass_time(1.0)
    arduino.digital[amarelo].write(0)
