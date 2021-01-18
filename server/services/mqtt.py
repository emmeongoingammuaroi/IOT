import json
import paho.mqtt.client as mqtt
from django.shortcuts import  get_object_or_404

from .models import Home, Room, Specs
from .constants import *


def on_publish(client, userdata, mid):
    print("Message Published ...")


def on_connect(client, userdata, flags, rc):
	print("Connect with result code", str(rc))
	client.subscribe(MQTT_SUB_TOPIC)


def on_message(client, userdata, msg):
	payload = json.loads(msg.payload)
	print("Message received: ", payload)
	try:
		home = get_object_or_404(Home, id=payload["homeId"])
		room = get_object_or_404(Room, home=home, title=payload["roomId"])
		new_specs = Specs(room=room, temperature=payload["temp"],
			            humidity=payload["hum"], gas=payload["gas"])
		new_specs.save()
		print('Saved message data to database')
	except Exception as e:
		print('aoalala', e)


# Initiate MQTT Client
client = mqtt.Client()


# Register publish callback function
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish


# Connect with MQTT Broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
