from django.urls import path

from .views import generate_test_data, index, graphic, stats, table

urlpatterns = [
    path('', index, name="index"),
    path('table/', table, name="table"),
    path('graphic/', graphic, name="graphic"),
    path('stats/', stats, name="stats"),
    path('generate-test-data/', generate_test_data),
]