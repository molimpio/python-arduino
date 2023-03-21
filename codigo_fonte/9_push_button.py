"""
Exemplo que acende os leds com acionamento do push button, conforme o botão é apertado acende os leds.
"""

from pyfirmata import Arduino, OUTPUT, INPUT, util
from constantes import PORTA_COMUNICACAO, PINO_13, PINO_2, PINO_11, PINO_12

arduino = Arduino(PORTA_COMUNICACAO)
led_1 = PINO_11
led_2 = PINO_12
led_3 = PINO_13
push_button = PINO_2
estado_anterior = False
num = 0

digito = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]

iterator = util.Iterator(arduino)
iterator.start()

arduino.digital[push_button].mode = INPUT
arduino.digital[led_1].mode = OUTPUT
arduino.digital[led_2].mode = OUTPUT
arduino.digital[led_3].mode = OUTPUT

while True:
    estado_botao = arduino.digital[push_button].read()

    if estado_botao is True and estado_anterior is False:
        num = num + 1
        if num > 7:
            num = 0
        print("Decimal: ", num, " Binário: ", str("{0:b}".format(num).zfill(3)))
        arduino.digital[led_1].write(digito[num][0])
        arduino.digital[led_2].write(digito[num][1])
        arduino.digital[led_3].write(digito[num][2])

    estado_anterior = estado_botao
    arduino.pass_time(0.05)
