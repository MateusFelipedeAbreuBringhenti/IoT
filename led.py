import RPI.GPIO as GPIO
import time as delay
from urllib.request import urlopen

gpio.setmode(gpio.BOARD)

LedVermelho, LedVerde= 11, 12

gpio.setup(LedVermelho, gpio.OUT)
gpio.setup(LedVerde, gpio.OUT)

gpio.output(LedVermelho, False)
gpio.output(LedVerde, False)

def testaConexao():
    try:
        urlopen('https://www.materdei.edu.br/pt', timeout=1)
        return True
    except:
        return False
    
if testaConexao() == True:
    i = 0
    while i < 3:
        gpio.output(LedVerde, True)
        delay.sleep(1)
        gpio.output(LedVerde, False)
        delay.sleep(1)
        i = i + 1
else:
    i = 0
    while 1 <=3:
        gpio.output(LedVermelho, True)
        delay.sleep(1)
        gpio.output(LedVermelho, False)
        delay.sleep(1)
        i = i + 1
            