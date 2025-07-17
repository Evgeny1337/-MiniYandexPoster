import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Загрузчик туристических мест'

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def handle(self, *args, **options):
        if options['url']:
            try:
                place_response = requests.get(url=options['url'])
                place_response.raise_for_status()
                place_details = place_response.json()
                image_urls = place_details['imgs']
                title = place_details['title']
                short_description = place_details['short_description']
                long_description = place_details['long_description']
                coordinates = place_details['coordinates']
                latitude = coordinates['lat']
                longitude = coordinates['lng']
                place = self.create_place(
                    title=title,
                    description_short=short_description,
                    description_long=long_description,
                    latitude=latitude,
                    longitude=longitude
                )
                if place:
                    for number, image_url in enumerate(image_urls):
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

    def create_placeimage(self, place, url, number):
        try:
            image = requests.get(url)
            image.raise_for_status()
            filename = f"{place.id}_{number}.jpg"
            PlaceImage.objects.get_or_create(
                place=place,
                number=number,
                defaults={
                    'image': ContentFile(image.content, name=filename)
                }
            )
        except requests.exceptions.RequestException as err:
            self.stdout.write(f"Ошибка  при скачивание изображения {err}")

    def create_place(
            self,
            title,
            short_description,
            long_description,
            latitude,
            longitude):
        place, created = Place.objects.get_or_create(
            title=title,
            latitude=latitude,
            longitude=longitude,
            defaults={
                "short_description": short_description,
                "long_description": long_description
            }
        )
        return place
