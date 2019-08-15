from django.db import models

class Relay(models.Model):
    name = models.CharField(max_length=15, unique=True)
    state = models.IntegerField(default=0)

    def __str__(self):
        return self.name
