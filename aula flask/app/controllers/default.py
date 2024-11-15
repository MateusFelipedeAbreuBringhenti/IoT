import RPi.GPIO as gpio
import time as delay
from app import app
from flask import render_template

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

LedVermelho, LedVerde = 11, 12
statusVermelho = ""
statusVerde = ""


gpio.setup(LedVermelho, gpio.OUT)
gpio.setup(LedVerde, gpio.OUT)

gpio.output(LedVermelho, gpio.LOW)
gpio.output(LedVerde, gpio.LOW)

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

    ocupacao_l = (distancia / lixeira_v) * 100
    ocupacao_f = 100 - ocupacao_l
    ocupacao_lixeira = ('{0:0.0f}%'.format(ocupacao_f))
    return ocupacao_lixeira

def status_led_vermelho():
    if gpio.input(LedVermelho) == 1:
        statusVermelho = 'LED vermelho ON'
    else:
        statusVermelho = 'LED vermelho OFF'
    return statusVermelho

def status_led_verde():
    if gpio.input(LedVerde) == 1:
        statusVerde = 'LED vermelho ON'
    else:
        statusVerde = 'LED vermelho OFF'
    return statusVerde


@app.route("/")
def index():
    templateData = {
        'LedRed': status_led_vermelho(),
        'LedGreen': status_led_verde(),
        'ocup_lixeira': distancia()
    }
    return render_template('index.html', **templateData)

@app.route("/led_vermelho/<action>")
def led_vermelho(action):
    if action == 'on':
        gpio.output(LedVermelho, gpio.HIGH)
    if action == 'off':
        gpio.output(LedVermelho, gpio.LOW)

    templateData = {
        'LedRed': status_led_vermelho(),
        'LedGreen': status_led_verde()
    }
    return render_template('index.html', **templateData)