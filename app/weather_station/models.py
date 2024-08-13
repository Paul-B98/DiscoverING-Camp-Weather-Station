from django.db import models


class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.temperature:.3}°C, {self.humidity:.3}%'