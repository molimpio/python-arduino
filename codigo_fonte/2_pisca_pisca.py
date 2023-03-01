"""
Exemplo de pisca pisca com controle do LED pela entrada do usuario no input
"""

from pyfirmata import Arduino, OUTPUT
from constantes import PORTA_COMUNICACAO, PINO_13

arduino = Arduino(PORTA_COMUNICACAO)
arduino.digital[PINO_13].mode = OUTPUT

while True:
    estado = input("Digite 1 para ligar\nDigite 0 para desligar\nDigite 2 para finalizar\n")
    if estado == "0" or estado == "1":
        arduino.digital[PINO_13].write(int(estado))
    elif estado == "2":
        break
    else:
        print("Erro: Digite apenas 0 ou 1")

arduino.exit()
