import Rpi.GPIO as gpio
import time as delay
from urllib.request import urlopen
import resquests

gpio.setmode(gpio.BOARD)

LedVermelho, LedVerde = 11, 12
pin_e = 16
pin_t = 15

gpio.setup(LedVermelho, gpio.OUT)
gpio.setup(LedVerde, gpio.OUT)
gpio.setup(pin_t, gpio.OUT)

gpio.setup(pin_e, gpio.IN)

gpio.output(LedVermelho, False)
gpio.setup(LedVerde, gpio.OUT)

urlBase = 'https://api.thingspeak.com/update?api_key='
keyWrite = 'M2K8MXLK5X5QMFLQ'
sensorDistancia = '&field1='

def testeConexao():
    try:
        urlopen('https://www.materdei.edu.br/pt', timeout=1)
        return True
    except:
        return False
    

def distancia():
    gpio.output(pin_t, True)
    delay.sleep(0.00001)
    gpio.output(pin_t, False)
    tempo_i = delay.time()
    tempo_f = delay.time()

    while gpio.input(pin_e) == False:
        tempo_i = delay.time()
    while gpio.input(pin_e) == True:
        tempo_f = delay.time()

    temp_d = tempo_f - tempo_i
    distancia = (temp_d * 34300) / 2
    return distancia


if testeConexao() == True:
    i = 0
    while i <= 3:
        gpio.output(LedVerde, True)
        delay.sleep(0.2)
        gpio.output(LedVerde, False)
        delay.sleep(0.2)
        i = i + 1

    while True:

        urlDados = (urlBase + keyWrite + sensorDistancia + str(distancia()))
        retorno =resquests.post(urlDados)
        if retorno.status_code == 200:
            print('Dados enviados com sucesso')
        else:
            print('Dados nao enviados'+ retorno.status_code)
        delay.sleep(20)

else:
    i = 0
    while i <= 3:
        gpio.output(LedVermelho, True)
        delay.sleep(0.2)
        gpio.output(LedVermelho, False)
        delay.sleep(0.2)
        i = i + 1