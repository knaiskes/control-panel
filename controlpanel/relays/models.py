from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Relay(models.Model):
    name = models.CharField(max_length=15, unique=True)
    state = models.IntegerField(default=0,
            validators = [MaxValueValidator(1), MinValueValidator(0)])

    def __str__(self):
        return self.name

    def update_state(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 0
