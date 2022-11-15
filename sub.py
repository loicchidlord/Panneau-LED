import subprocess
import paho.mqtt.client as mqtt
from typing import NewType


username = "chiche"
passwd = "ChicheBroker14"
port = 1112
ip_broker = "194.199.227.235"
Client = NewType('Client', mqtt )
Data = NewType('Data', str )


def on_connect(client: Client, userdata, flags, rc):
    """cette fonction permet de se connecter au broker"""
    print("Connected with result code "+ str(rc))
    client.subscribe("test")

def affiche_led(data: Data,font: str,vitesse: str, nbtour: str):
    """ fonction envoie vers l'affichage de led"""
    print('Données reçues : {}'.format(data))
    cmd = "./scrolling-text-example -f " + font + " " + data + " -s " + vitesse  + " -l " + nbtour
    #cmd = "./text-example
    subprocess.check_output(cmd,shell=True).decode("utf-8")

def on_message(client, userdata, msg):
    data = str(msg.payload)[:-1][2:]
    font="/root/rpi-rgb-led-matrix/fonts/9x18.bdf"
    vitesse = "5"
    nbtour="3"
    print("affiche led")
    affiche_led(data,font,vitesse,nbtour)


client = mqtt.Client(client_id="",clean_session=True,userdata=None,protocol=mqtt.MQTTv311,transport="tcp$
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username,passwd)
print("Please wait few moment....")
print("Connecting.....")
print("Connecting OK 100% :)")
print(" ")
print("Wating for data............")
client.connect(ip_broker, port, 10)
client.loop_forever()
