import paho.mqtt.client as mqtt
import random

import time
import json

broker="broker.hivemq.com" #broker público - http://www.mqtt-dashboard.com/
port=1883 #porta
topico="par/sala01" #Tópico. Nesse tópico iremos armazenar se temperatura e humidade, por exemplo

cliente=mqtt.Client("cliente01")
cliente.connect(host=broker,port=port)
valor_temperatura=0

while(True):
    valor_temperatura= random.randint(0,1)
    dados_sensores={'ABRIU':valor_temperatura}
    dados=json.dumps(dados_sensores)#Transforma dicionário Python em JSON
    cliente.publish(topic=topico,payload=dados,qos=1)
    print(dados)
    time.sleep(20)
