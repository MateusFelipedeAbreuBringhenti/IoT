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




@app.route("/")
def index():


