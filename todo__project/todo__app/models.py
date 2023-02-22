from django.db import models


class Task(models.Model):
    name=models.CharField(max_length=300)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name
