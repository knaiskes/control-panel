from django.db import models

class Buzzer(models.Model):
    name = models.CharField(max_length=15, unique=True)
    identifier = models.CharField(max_length=15)
    mqtt_topic = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
