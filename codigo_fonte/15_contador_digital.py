"""
Exemplo usando display de 7 segmentos com push button
"""

from pyfirmata import Arduino, util
from constantes import PORTA_COMUNICACAO

import random

anterior = False
digito = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
]

arduino = Arduino(PORTA_COMUNICACAO)
iterator = util.Iterator(arduino)
iterator.start()

botao = arduino.get_pin("d:2:i")
seg = list()
seg.append(arduino.get_pin("d:7:o"))
seg.append(arduino.get_pin("d:8:o"))
seg.append(arduino.get_pin("d:9:o"))
seg.append(arduino.get_pin("d:10:o"))
seg.append(arduino.get_pin("d:11:o"))
seg.append(arduino.get_pin("d:12:o"))
seg.append(arduino.get_pin("d:13:o"))


def exibir_numero(numero):
    for i in range(0, 7):
        seg[i].write(digito[numero][i])


def limpar():
    for i in range(0, 7):
        seg[i].write(0)


while True:
    valor = botao.read()
    if valor is True and anterior is False:
        exibir_numero(random.randint(0, 5))
        arduino.pass_time(2.0)
        limpar()
    anterior = False
    arduino.pass_time(0.05)
