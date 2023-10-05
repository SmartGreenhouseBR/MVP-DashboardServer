import json
import paho.mqtt.client as mqtt
from django.conf import settings

from gateway.adapters import on_connect, on_message


def create_mqtt_client():
    print("Instanciado")
    client = mqtt.Client(userdata={})
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(
        settings.MQTT_BROKER_ADDRESS,
        settings.MQTT_PORT,
        settings.MQTT_KEEPALIVE
    )
    client.loop_start()

    return client
