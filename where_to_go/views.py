from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.templatetags.static import static
from django.http.response import JsonResponse
from django.urls import reverse


def show_start(request):
    places = Place.objects.prefetch_related('images').all()
    features = []
    for place in places:
        details_url = reverse('place-detail', args=[place.id])
        features.append({
                "type":"Feature", 
                 "geometry": { 
                     "type": "Point",
                     "coordinates": [place.latitude, place.longitude]
                     }, 
                  "properties": {
                      "title": place.title,
                      "placeId":f"{place.title}",
                      "detailsUrl": details_url 
                      }
                })

    print(features)
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'index.html', {'geojson': geojson})


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place,pk=place_id)
    place_images = [place_image.image.url for place_image in place.images.all() if place_image != None]
    detailsUrl = {
            "title": place.title,
            "imgs": place_images,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude
            }
    }
    return JsonResponse(detailsUrl)
   