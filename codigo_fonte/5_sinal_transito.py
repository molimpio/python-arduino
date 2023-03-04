"""
Exemplo de sinal de trânsito para veículos com leds vermelho, amarelo e verde utilizando método get_pin
"""

from pyfirmata import Arduino
from constantes import PORTA_COMUNICACAO

arduino = Arduino(PORTA_COMUNICACAO)
vermelho = arduino.get_pin("d:13:o")
amarelo = arduino.get_pin("d:12:o")
verde = arduino.get_pin("d:11:o")

while True:
    vermelho.write(1)
    arduino.pass_time(5.0)
    vermelho.write(0)
    verde.write(1)
    arduino.pass_time(3.0)
    verde.write(0)
    amarelo.write(1)
    arduino.pass_time(1.0)
    amarelo.write(0)
