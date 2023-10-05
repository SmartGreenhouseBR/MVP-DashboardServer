from django.apps import AppConfig
from gateway.mqtt import create_mqtt_client


class GatewayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gateway'

    def ready(self):
        create_mqtt_client()
