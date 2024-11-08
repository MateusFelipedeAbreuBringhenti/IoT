import RPi.GPIO as gpio
import time as delay
import os 

gpio.setmode(gpio.BOARD)

pin_t = 15
pin_e = 16
lixeira_v = 20

gpio.setup(pin_t, gpio.OUT)
gpio.setup(pin_e, gpio.IN)

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

f = open('/root/Aula-IoT/log.txt', 'a+')
f.close()

while True:
    valorRecebido = distancia()
    print("Distancia = %.1f cm" % valorRecebido)
    espaco_d = (valorRecebido / lixeira_v) * 100
    print("Espaço disponivel = %.1f" % espaco_d, '%')
    espaco_o = 100 - espaco_d
    print("Espaço ocupado = %.1f" % espaco_o, '%')

    f = open('/root/Aula-IoT/log.txt', 'a+')
    f.write("Distancia = %.1f cm \n" % valorRecebido)
    f.write("Espaço disponivel = %.1f \n" % espaco_d)
    f.write("Espaço ocupado = %.1f \n" % espaco_o)
    f.close()

    delay.sleep(5)