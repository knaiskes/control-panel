from django.db import models
import paho.mqtt.client as paho
from json import load

try:
    with open('../config.json') as json_file:
        data = load(json_file)

    username = data['mqtt']['username']
    password = data['mqtt']['password']

except FileNotFoundError:
    print('Could not open config file')


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
            self.client_name.username_pw_set(username=username, password=password)
            self.client_name.on_publish = self.on_publish
            self.client_name.connect(self.broker, self.port)
            ret = self.client_name.publish(self.topic, command)
        except ConnectionRefusedError:
            # TODO return error message and render it to dashboard
            pass

class MqttRelay(Mqtt):
    def send(self, state):
        if state:
            state = 'ON'
        else:
            state = 'OFF'

        super().send(state)
