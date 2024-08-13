from django.urls import path

from .views import generate_test_data, index

urlpatterns = [
    path('', index),
    path('generate-test-data/', generate_test_data),
]