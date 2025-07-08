from django.shortcuts import render
from places.models import Place
from django.templatetags.static import static
import json
def show_start(request):
    places = Place.objects.all()
    features = [{
                "type":"Feature", 
                 "geometry": { 
                     "type": "Point",
                     "coordinates": [place.latitude, place.longitude]
                     }, 
                  "properties": {
                      "title": place.title,
                      "placeId":f"{place.title}",
                      "detailsUrl": static('places/moscow_legends.json')
                      }
                } for place in places]
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'index.html', {'geojson': geojson})