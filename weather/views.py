from django.shortcuts import render
import requests
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&id=524901&appid=a3201c3b97b4e1c44658bef2a7da0f7a'
    city = 'Kolkata'
    r = requests.get(url.format(city)).json()

    print(r)
    city_info = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }
    return render(request, 'weather/index.html', city_info)

