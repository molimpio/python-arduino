import pyfirmata
from constantes import PORTA_COMUNICACAO, PINO_13

arduino = pyfirmata.Arduino(PORTA_COMUNICACAO)
arduino.digital[PINO_13].mode = pyfirmata.OUTPUT

while True:
    arduino.digital[PINO_13].write(1)
    arduino.pass_time(0.5)
    arduino.digital[PINO_13].write(0)
    arduino.pass_time(0.5)
