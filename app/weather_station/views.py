import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import WeatherData


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


def table(request: HttpRequest) -> HttpResponse:
    """
    Render the weather station index page.
    """
    context = {"data": WeatherData.objects.all()}
    return render(request, 'weather_station/table.html', context=context)


def graphic(request: HttpRequest) -> HttpResponse:
    """
    Render the weather station index page.
    """
    context = {"data": WeatherData.objects.all()}
    return render(request, 'weather_station/graphic.html', context=context)


def stats(request: HttpRequest) -> HttpResponse:
    """
    Render the weather station index page.
    """
    temperatures = WeatherData.objects.values_list('temperature', flat=True)
    humdities = WeatherData.objects.values_list('humidity', flat=True)

    context = {"data": {
        "temperature": {
            "min": min(temperatures),
            "max": max(temperatures),
            "avg": sum(temperatures) / len(temperatures),
            "len": len(temperatures),
        },
        "humidity": {
            "min": min(humdities),
            "max": max(humdities),
            "avg": sum(humdities) / len(humdities),
            "len": len(humdities),
        },
    }}
    return render(request, 'weather_station/stats.html', context=context)
