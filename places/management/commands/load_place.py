from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage
import requests
from io import BytesIO
from PIL import Image

class Command(BaseCommand):
    help = 'The Zen of Python'

    def add_arguments(self, parser):
        parser.add_argument("url",type=str)

    def handle(self, *args, **options):
        if options['url']:
            try:
                place_response = requests.get(url=options['url'])
                place_details = place_response.json()
                image_urls = place_details['imgs']
                title = place_details['title']
                description_short = place_details['description_short']
                description_long = place_details['description_long']
                coordinates = place_details['coordinates']
                latitude = coordinates['lat']
                longitude = coordinates['lng']
                place = self.create_place(
                    title=title,
                    description_short=description_short,
                    description_long=description_long,
                    latitude=latitude,
                    longitude=longitude
                )
                if place:
                    for number,image_url in enumerate(image_urls):
                        self.create_placeimage(
                            place=place,
                            url=image_url,
                            number=number
                        )
                else:
                    self.stdout.write("Ошибка при добавлении места")
            except requests.exceptions.RequestException as err:
                self.stdout.write(f"Ошибка запроса {err}")
        else:
            self.stdout.write("Вы не передали url")

    def create_placeimage(self,place,url,number):
        try:
            image = requests.get(url)
            filename = f"{place.id}_{number}.jpg"
            if not PlaceImage.objects.filter(place=place,number=number).exists():
                image_content = ContentFile(image.content, name=filename)
                PlaceImage.objects.create(
                    image=image_content,
                    number=number,
                    place=place
                )
        except requests.exceptions.RequestException as err:
            self.stdout.write(f"Ошибка  при скачивание изображения {err}")
        

    def create_place(self,title,description_short,description_long,latitude,longitude):
        place = Place.objects.filter(
                title=title,
                latitude=latitude,
                longitude=longitude
                ).first()
        if place:
            return place
        return Place.objects.create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            latitude=latitude,
            longitude=longitude
        )

