"""
Exemplo de sinal de trânsito para veículos e pedestres com leds vermelho, amarelo e verde
"""

from pyfirmata import Arduino, OUTPUT
from constantes import PORTA_COMUNICACAO, PINO_13, PINO_12, PINO_11, PINO_10, PINO_9

arduino = Arduino(PORTA_COMUNICACAO)
vermelho_veiculo = PINO_13
amarelo_veiculo = PINO_12
verde_veiculo = PINO_11
verde_pedestre = PINO_10
vermelho_pedestre = PINO_9

arduino.digital[vermelho_veiculo].mode = OUTPUT
arduino.digital[amarelo_veiculo].mode = OUTPUT
arduino.digital[verde_veiculo].mode = OUTPUT
arduino.digital[verde_pedestre].mode = OUTPUT
arduino.digital[vermelho_pedestre].mode = OUTPUT

while True:
    # Livre para pedestre
    arduino.digital[vermelho_veiculo].write(1)
    arduino.digital[verde_pedestre].write(1)
    arduino.pass_time(5.0)

    # Livre para veiculo
    arduino.digital[verde_veiculo].write(1)
    arduino.digital[vermelho_pedestre].write(1)
    arduino.digital[vermelho_veiculo].write(0)
    arduino.digital[verde_pedestre].write(0)
    arduino.pass_time(5.0)

    # Amarelo para veiculo
    arduino.digital[verde_veiculo].write(0)
    arduino.digital[amarelo_veiculo].write(1)

    arduino.pass_time(5.0)
    arduino.digital[amarelo_veiculo].write(0)
    arduino.digital[vermelho_pedestre].write(0)
