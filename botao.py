import RPi.GPIO as gpio
import time as delay

gpio.setmode(gpio.BOARD)

LedVermelho, LedVerde, botao = 11, 12, 18

gpio.setup(LedVermelho, gpio.OUT)
gpio.setup (LedVerde, gpio.OUT)
gpio.setup(botao, gpio.IN)

gpio.output(LedVermelho, False)
gpio.output(LedVerde, False)

Contador = 0
i = 0

while True:
    if gpio.input(botao) == True:
        Contador = Contador + 1
        delay.sleep(0.5)
        i = 0

    while i < Contador:
        gpio.output(LedVerde, True)
        delay.sleep(0.5)
        gpio.output(LedVerde, False)
        delay.sleep(0.5)
        i = i + 1