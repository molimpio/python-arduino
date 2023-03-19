"""
Exemplo que acende o led com acionamento do push button, o push button faz o toggle do led conforme é apertado.
"""

from pyfirmata import Arduino, OUTPUT, INPUT, util
from constantes import PORTA_COMUNICACAO, PINO_13, PINO_2

arduino = Arduino(PORTA_COMUNICACAO)
led = PINO_13
push_button = PINO_2
estado_anterior = False
estado_atual = False

iterator = util.Iterator(arduino)
iterator.start()

arduino.digital[push_button].mode = INPUT
arduino.digital[led].mode = OUTPUT

while True:
    estado_botao = arduino.digital[push_button].read()

    if estado_botao is True and estado_anterior is False:
        estado_atual = not estado_atual
        arduino.digital[led].write(estado_atual)

    estado_anterior = estado_botao
    arduino.pass_time(0.05)
