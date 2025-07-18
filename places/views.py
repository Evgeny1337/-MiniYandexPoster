from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def show_start(request):
    places = Place.objects.prefetch_related("images").all()
    features = []
    for place in places:
        place_details = reverse("place-detail", args=[place.id])
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": f"{place.title}",
                "detailsUrl": place_details
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, "index.html", {"geojson": geojson})


def get_place_by_id(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("images"),
        pk=place_id
    )
    place_images = [
        place_image.image.url for place_image in place.images.all() if place_image]
    place_details = {
        "title": place.title,
        "imgs": place_images,
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(place_details)
