from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Relay(models.Model):
    name = models.CharField(max_length=15, unique=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def update_state(self, current_state):
        # toggle
        return not current_state
