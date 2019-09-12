from django.db import models
import paho.mqtt.client as paho

class Mqtt(models.Model):
    broker = "localhost"
    port = 1883

    def __init__(self, client_name, topic):
        self.client_name = client_name
        self.topic = topic

    def on_publish(client, userdata, result):
        pass

    def send(self, command):
        try:
            self.client_name = paho.Client()
            self.client_name.on_publish = self.on_publish
            self.client_name.connect(self.broker, self.port)
            ret = client_name.publish(self.topic, command)
        except ConnectionRefusedError:
            # TODO return error message and render it to dashboard
            pass


    #def send_relay_command(self, topic, state):
    #    command = 'OFF'

    #    if state:
    #        command = 'ON'

    #    try:
    #        relay_client = paho.Client()
    #        relay_client.on_publish = self.on_publish
    #        relay_client.connect(self.broker, self.port)
    #        ret = relay_client.publish(topic, command)

    #    except ConnectionRefusedError:
    #        # TODO return error message and render it to dashboard
    #        pass

class MqttRelay(Mqtt):
    def send(self, state):
        if state:
            state = 'ON'
        else:
            state = 'OFF'

        super().send(state)
