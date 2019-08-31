from django.db import models
import paho.mqtt.client as paho

class Mqtt(models.Model):
    broker = "localhost"
    port = 1883

    def on_publish(client, userdata, result):
        pass

    def send_relay_command(self, topic, state):
        command = 'OFF'

        if state:
            command = 'ON'

        try:
            relay_client = paho.Client()
            relay_client.on_publish = self.on_publish
            relay_client.connect(self.broker, self.port)
            ret = relay_client.publish(topic, command)

        except ConnectionRefusedError:
            # TODO return error message and render it to dashboard
            pass
