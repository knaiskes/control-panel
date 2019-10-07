from django.db import models
from django.utils.timezone import now

class Dht22(models.Model):
    name = models.CharField(max_length=15, unique=True, primary_key=True)
    identifier = models.CharField(max_length=15)
    mqtt_topic = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    name = models.ForeignKey(Dht22, on_delete=models.CASCADE)
    temperature = models.FloatField(null=True, blank=True, default=None)
    humidity = models.FloatField(null=True, blank=True, default=None)
    date = models.DateTimeField(null=True, blank=True)
