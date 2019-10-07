from django.db import models

class Relay(models.Model):
    name = models.CharField(max_length=15, unique=True)
    identifier = models.CharField(max_length=15)
    state = models.BooleanField(default=False)
    mqtt_topic = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

    def update_state(self, current_state):
        # toggle
        return not current_state
