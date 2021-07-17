from django.shortcuts import render
import requests

from .models import(
    City
)
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&id=524901&appid=a3201c3b97b4e1c44658bef2a7da0f7a'

    form = CityForm(request.GET)
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()

        city_info = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_info)
    context = {'weather_data': weather_data, 'form': form }
    return render(request, 'weather/index.html', context)

