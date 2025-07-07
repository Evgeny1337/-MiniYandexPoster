from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    

    def __str__(self):
        return self.title



class PlaceImage(models.Model):
    image = models.ImageField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    number = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return str(self.number) + ' ' + self.place.title





