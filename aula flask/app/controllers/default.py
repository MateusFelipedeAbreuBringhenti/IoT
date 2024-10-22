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
        'LedGreen': status_led_verde()
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