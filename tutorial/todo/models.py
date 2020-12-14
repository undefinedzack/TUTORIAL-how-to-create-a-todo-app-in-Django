from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task}"