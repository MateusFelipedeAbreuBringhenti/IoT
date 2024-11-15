import time as delay
from urllib.request import urlopen
import requests

urlBase = 'https://api.thingspeak.com/channels/'
readKey = '/last?key=5S413VA96XJWWBMU'
channels = '2746103'
field1 = '/fields/1/'



def testaConexao():
    try:
        urlopen('https://www.materdei.edu.br/pt', timeout=1)
        return True
    except:
        return False
    

if testaConexao() == True:
    print('Conectado a internet')

    while True:
        consultaDistancia = requests.get(urlBase + channels + field1 + readKey)
        print(consultaDistancia.text)
        delay.sleep(20)

else:
    print('Sem conexao com a internet')