import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import json
import configparser
from pygame.locals import *
import pygame


def som():
    pygame.mixer.init()
    pygame.mixer.music.load("applause.ogg")
    pygame.mixer.music.play()
    pygame.time.wait(1200)


def on_message(client, userdate, message):

    dados = json.loads(str(message.payload.decode()))
    print("Detectei {0}".format(dados['field1']))
    if float(dados['field1']) == 1.00:
        print("ABRIU")
        som()
    elif float(dados['field1']) == 0.00:
        print("FECHOU")
        pygame.mixer.music.stop()

broker = "mqtt.thingspeak.com"
port = 1883
config = configparser.ConfigParser()
config.read('conf')
topico = config['THINGSPEAK']['TOPICO_SUBSCRIBE']
username = config['THINGSPEAK']['USERNAME']
password = config['THINGSPEAK']['MQTT_API_KEY']
subscribe.callback(on_message, qos=0, topics=topico, hostname=broker, port=port, client_id="clisub",
                   auth={'username': username, 'password': password})
while (True):
    time.sleep(20)
