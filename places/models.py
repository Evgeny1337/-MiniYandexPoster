from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    

    def __str__(self):
        return self.title
    



class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    number = models.IntegerField(blank=True,null=True, verbose_name='Позиция', default=0)

    class Meta:
        ordering = ['number']


    def __str__(self):
        return str(self.number) + ' ' + self.place.title
    






