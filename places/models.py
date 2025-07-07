from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title
