from django.db import models
from django.utils.timezone import now

class Dht22(models.Model):
    name = models.CharField(max_length=15, unique=True)
    mqtt_topic = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Data(models.Model):
    dht22_name = models.ForeignKey(Dht22, on_delete=models.CASCADE)
    temperature = models.FloatField(null=True, blank=True, default=None)
    humidity = models.FloatField(null=True, blank=True, default=None)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.dht22_name

