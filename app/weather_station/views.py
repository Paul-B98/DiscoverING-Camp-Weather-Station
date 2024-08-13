import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse


def generate_test_data(request: HttpRequest) -> HttpResponse:
    """
    Generate test data for the weather station.
    """
    return JsonResponse({
        'temperature': random.uniform(-50, 50),
        'humidity': random.uniform(0, 100),
    })


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the weather station index page.
    """
    context = {}
    return render(request, 'weather_station/index.html', context=context)