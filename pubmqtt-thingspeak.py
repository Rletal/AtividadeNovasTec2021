import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser
broker="mqtt.thingspeak.com" #broker ThingSpeak
port=1883 #porta
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_PUBLISH']
valor_temperatura=0

#Documentação API MQTT https://www.mathworks.com/help/thingspeak/publishtoachannelfeed.html
while(True):
    valor_temperatura= random.randint(0,1)

    dados="field1={:.2f}&status=MQTTPUBLISH".format(valor_temperatura)
    publish.single(payload=dados,topic=topico,port=port,hostname=broker)
    print(dados)
    time.sleep(20)
