from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    
    class Meta:
        verbose_name='Место'
        verbose_name_plural='Места'

    def __str__(self):
        return self.title
    



class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    number = models.IntegerField(blank=True,null=True, verbose_name='Позиция')

    class Meta:
        verbose_name='Изображение'
        verbose_name_plural='Изображеня'
        ordering = ['number']
        indexes = [
            models.Index(fields=['number'])
        ]


    def __str__(self):
        return '{} {}'.format(self.number,self.place.title)

    






