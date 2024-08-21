from django.http import JsonResponse
from django.shortcuts import render

from restaurant_map.models import Restaurant


# Create your views here.
def index(request):
    restaurants = Restaurant.objects.exclude(restaurant_address='x').values('restaurant_name','restaurant_address','restaurant_latitude','restaurant_longitude')
    context = {
        "restaurants": list(restaurants)
    }
    return render(request, "index.html", context)

